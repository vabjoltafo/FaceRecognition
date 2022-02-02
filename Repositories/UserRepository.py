import psycopg2


def connectToDatabase():
    try:
        connection = psycopg2.connect(database = "facemob", user = "postgres", password = "12345678",
                    host = "127.0.0.1", port = "5432")

    except psycopg2.Error as err:
        print("Error with DB")

    else:
        print("Connection estabilished!")

    return connection




#gjen perdoruesin gjate logimit
def findTheUser(username, password):
    cursor = connectToDatabase().cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    records = cursor.fetchone()
    return records

def getAllUsers():
    cursor = connectToDatabase().cursor()
    cursor.execute("SELECT name, surname, username, password, user_type FROM users")
    records = cursor.fetchall()
    return records


def getTheLastIdFromUsers():
    cursor = connectToDatabase().cursor()
    cursor.execute("SELECT id FROM users ORDER BY id DESC")
    records = cursor.fetchone()
    if records:
        return records[0]
    return 0


def insertUser(name, surname, username, password, userType):

    idOfTheuser = 0

    if getTheLastIdFromUsers() is not None:
        idOfTheuser = getTheLastIdFromUsers() + 1

    try:
        connection = psycopg2.connect(database="facemob", user="postgres", password="12345678",
                                          host="127.0.0.1", port="5432")

    except psycopg2.Error as err:
            print("Error with DB")

    else:
            print("Connection estabilished!")


    cursor = connection.cursor()

    cursor.execute('INSERT INTO users(id, name, surname, username, password, user_type) VALUES(%s, %s, %s, %s, %s, %s)',
                    (int(idOfTheuser), name, surname, username, password, userType))

    connection.commit()
    connection.close()


def deleteUser(id):

    try:
        connection = psycopg2.connect(database="facemob", user="postgres", password="12345678",
                                      host="127.0.0.1", port="5432")

    except psycopg2.Error as err:
        print("Error with DB")

    else:
        print("Connection estabilished!")
    cursor = connection.cursor()
    cursor.execute("DELETE  FROM users WHERE id=%s", (id,))
    connection.commit()
    connection.close()


def updateUser(id, name, surname, username, password, userType):
    try:
        connection = psycopg2.connect(database="facemob", user="postgres", password="12345678",
                                      host="127.0.0.1", port="5432")

    except psycopg2.Error as err:
        print("Error with DB")

    else:
        print("Connection estabilished!")

    cursor = connection.cursor()

    cursor.execute(
        'UPDATE users SET name=%s, surname=%s, username=%s, password=%s, user_type=%s '
        'where id= %s ',
        (name, surname, username, password, userType, id))

    connection.commit()
    connection.close()
