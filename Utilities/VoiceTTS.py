from gtts import gTTS
from playsound import playsound

def playMessage(message):
    myobj = gTTS(text= message, lang='it', slow=False)
    myobj.save("./Utilities/read.mp3")
    playsound("./Utilities/read.mp3")

