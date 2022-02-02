import psycopg2


def connectToDatabase():
    try:
        connection = psycopg2.connect(database="facemob", user="postgres", password="12345678",
                                      host="127.0.0.1", port="5432")

    except psycopg2.Error as err:
        print("Error with DB")

    else:
        print("Connection estabilished!")

    return connection


def getAllKontribute():
    cursor = connectToDatabase().cursor()
    cursor.execute("SELECT * FROM kontribute")
    records = cursor.fetchone()
    return records


def insertFirstKontribut(kShendetsore, kShoqerore, tap1, tap2, tap3):

    try:
        connection = psycopg2.connect(database="facemob", user="postgres", password="12345678",
                                          host="127.0.0.1", port="5432")

    except psycopg2.Error as err:
            print("Error with DB")

    else:
            print("Connection estabilished!")


    cursor = connection.cursor()

    cursor.execute('INSERT INTO kontribute VALUES(%s, %s, %s, %s, %s, %s)',
                    (int(1), kShendetsore, kShoqerore, tap1, tap2, tap3))

    connection.commit()
    connection.close()



def updateKontribute(kShendetsore, kShoqerore, tap1, tap2, tap3):

    try:
        connection = psycopg2.connect(database="facemob", user="postgres", password="12345678",
                                      host="127.0.0.1", port="5432")

    except psycopg2.Error as err:
        print("Error with DB")

    else:
        print("Connection estabilished!")


    cursor = connection.cursor()

    cursor.execute('UPDATE kontribute SET kontribute_shendetsore=%s, '
                   'kontribute_shoqerore=%s, tap1=%s, tap2=%s, tap3=%s WHERE'
                   ' id=1',
                   (kShendetsore, kShoqerore, tap1, tap2, tap3))

    connection.commit()
    connection.close()

# print(getAllKontribute())