from __future__ import print_function

import pickle
import threading
from _tkinter import TclError
from tkinter import messagebox as msg, Label

import cv2
import face_recognition
import imutils
import numpy as np
from PIL import Image
from PIL import ImageTk

from Repositories.EmployeeRepository import hasTheEmployeeExitedForToday, exitEmployee
from Utilities.VoiceTTS import playMessage


class ExitFaceFrame:
	def __init__(self, vs, root, width, height, x):
		self.vs = vs
		self.frame = None
		self.thread = None
		self.stopEvent = None
		self.width = width
		self.height = height
		self.x = x
		self.root = root
		self.panel = None
		self.encoding = ".//FacialRecognition//pickles//encoding1.pickle"

		try:
			self.data = pickle.loads(open(self.encoding, "rb").read())
		except:
			msg.showerror('Kujdes!', 'Nuk ka te dhena per punonjesit')
		self.stopEvent = threading.Event()
		self.thread = threading.Thread(target=self.videoLoop, args=())
		self.thread.start()
		self.root.wm_protocol("WM_DELETE_WINDOW", self.onClose)

	def videoLoop(self):

		if self.encoding is not None:
			try:
				while not self.stopEvent.is_set():
					self.frame = self.vs.read()
					self.frame = imutils.resize(self.frame, width= self.width, height=self.height)
					r = self.frame.shape[1] / float(self.frame.shape[1])

					boxes = face_recognition.face_locations(self.frame, model="hog")
					encodings = face_recognition.face_encodings(self.frame, boxes)
					names = []

					for self.encoding in encodings:
						matches = face_recognition.compare_faces(np.array(self.encoding), np.array(self.data["encodings"]))
						name = "I Panjohur"

						if True in matches:
							matchedIdxs = [i for (i, b) in enumerate(matches) if b]
							counts = {}

							for i in matchedIdxs:
								name = self.data["names"][i]
								counts[name] = counts.get(name, 0) + 1
								name = max(counts, key=counts.get)
						names.append(name)

					for ((top, right, bottom, left), name) in zip(boxes, names):
						top = int(top * r)
						right = int(right * r)
						bottom = int(bottom * r)
						left = int(left * r)
						cv2.rectangle(self.frame, (left, top), (right, bottom), (0, 255, 0), 2)
						y = top - 15 if top - 15 > 15 else top + 15

						if name is not "I Panjohur":
							fname = name.split('//')
							name = fname[2]

							if hasTheEmployeeExitedForToday(name) is not True:
								exitEmployee(name)
								firstName = name.split(' ')
								messageToPlay ='Mirupafshim ' + firstName[0]
								message = 'Mirupafshim ' + name + ', ju dolet me sukses!'
								cv2.putText(self.frame, message, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(21, 110, 180), 2)
								# threadUpdate = threading.Thread(target=playMessage, args=(messageToPlay,))
								# threadUpdate.start()
								playMessage(messageToPlay)

						cv2.putText(self.frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)


					image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
					image = Image.fromarray(image)
					image = ImageTk.PhotoImage(image)

					if self.panel is None:
						self.panel = Label(image=image, width= self.width, height=600)
						self.panel.image = image
						# self.panel.pack(side="left", padx=10, pady=10)
						self.panel.place(x= self.x, y=0)

					else:
						try:
							self.panel.configure(image=image)
							self.panel.image = image
						except TclError:
							pass

			except RuntimeError as e:
				print("[INFO] caught a RuntimeError")


	def onClose(self):
		print("[INFO] closing...")
		self.stopEvent.set()
		self.vs.stop()
		self.root.quit()