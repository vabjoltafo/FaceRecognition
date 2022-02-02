import datetime
import psycopg2
from Utilities.Convertors import formatDate


def connectToDatabase():
    try:
        connection = psycopg2.connect(database = "facemob", user = "postgres", password = "12345678",
                    host = "127.0.0.1", port = "5432")

    except psycopg2.Error as err:
        print("Error with DB")

    else:
        print("Connection estabilished!")

    return connection


def getAllEmployeeNameAndSurname():
    cursor = connectToDatabase().cursor()
    cursor.execute("SELECT name, surname FROM employee ")
    records = cursor.fetchall()
    return records


def getTheInfomationFromEmployees():
    cursor = connectToDatabase().cursor()
    cursor.execute("SELECT id, name, surname, position, birth_date, phone, email FROM employee")
    records = cursor.fetchall()
    return records


def getEmployeeById(id):
    cursor = connectToDatabase().cursor()
    cursor.execute("SELECT id, name, surname, position, birth_date, phone, email, gender "
                   "FROM employee where id=%s", (id,))
    records = cursor.fetchone()
    return records


def getEmployeesByName(name):
    cursor = connectToDatabase().cursor()
    cursor.execute("SELECT id, name, surname, position, birth_date, phone, email "
                       "FROM employee WHERE name ILIKE %s", (name,))
    records = cursor.fetchall()
    return records


def getTheIdOfEmployee(name, surname):
    cursor = connectToDatabase().cursor()
    cursor.execute("SELECT id FROM employee WHERE name=%s AND surname =%s ", (name, surname))
    records = cursor.fetchone()
    return records


def hasTheEmployeeEnteredForToday(label):
    array = label.split(' ')
    name = array[0]
    surname = array[1]

    idOfTheStudent = getTheIdOfEmployee(name, surname)
    cursor = connectToDatabase().cursor()
    cursor.execute('SELECT * FROM  presence WHERE employee_id = %s '
                   'AND date =%s', (idOfTheStudent, str(datetime.date.today())))

    records = cursor.fetchall()
    if records is None or len(records) is 0:
        return False

    return True


def hasTheEmployeeExitedForToday(label):
    array = label.split(' ')
    name = array[0]
    surname = array[1]

    idOfTheStudent = getTheIdOfEmployee(name, surname)
    cursor = connectToDatabase().cursor()
    cursor.execute('SELECT exit_time FROM  presence WHERE employee_id = %s '
                   'AND date =%s', (idOfTheStudent, str(datetime.date.today())))

    records = cursor.fetchall()

    if len(records) is not 0:
        lastEmployeeRecord = records[len(records) - 1]

        if lastEmployeeRecord[0] is None or lastEmployeeRecord[0] is '':
            return False

    return True


def getTheLastIdFromEmployee():
    cursor = connectToDatabase().cursor()
    cursor.execute("SELECT id FROM employee ORDER BY id DESC")
    records = cursor.fetchone()
    if records:
        return records[0]
    return 0


def insertEmployee(name, surname, gender, age, position, phone, email):

        try:
            connection = psycopg2.connect(database="facemob", user="postgres", password="12345678",
                                          host="127.0.0.1", port="5432")

        except psycopg2.Error as err:
            print("Error with DB")

        else:
            print("Connection estabilished!")

        birthDate = formatDate(age)

        cursor = connection.cursor()

        cursor.execute('INSERT INTO employee(name, surname, email, gender, position, birth_date, phone) VALUES( %s, %s, %s, %s, %s, %s, %s)',
                       (name, surname, email, gender, position, birthDate , phone))

        connection.commit()
        connection.close()


def deleteWageByEmployee(id):
    try:
        connection = psycopg2.connect(database="facemob", user="postgres", password="12345678",
                                      host="127.0.0.1", port="5432")

    except psycopg2.Error as err:
        print("Error with DB")

    else:
        print("Connection estabilished!")

    cursor = connection.cursor()

    cursor.execute('Delete from employee_wage  WHERE employee_id=%s', (id, ))

    connection.commit()
    connection.close()


def updateEmployee(id, name, surname, gender, age, position, phone, email):

    global connection
    try:
        connection = psycopg2.connect(database="facemob", user="postgres", password="12345678",
                                      host="127.0.0.1", port="5432")

    except psycopg2.Error as err:
        print("Error with DB")

    else:
        print("Connection estabilished!")

    birthDate = formatDate(age)

    cursor = connection.cursor()

    cursor.execute('UPDATE employee SET name =%s, surname=%s, position=%s, birth_date=%s, phone=%s, email=%s, gender=%s '
                   'where id= %s',
                   (name, surname,position,birthDate, phone, email, gender, id))

    connection.commit()
    connection.close()


def deleteEmployee(id):

    try:
        connection = psycopg2.connect(database="facemob", user="postgres", password="12345678",
                                      host="127.0.0.1", port="5432")

    except psycopg2.Error as err:
        print("Error with DB")

    else:
        print("Connection estabilished!")
    cursor = connection.cursor()
    cursor.execute("DELETE  FROM employee WHERE id=%s",(id,))
    connection.commit()
    connection.close()
    deleteWageByEmployee(id)


def insertPresenceOfEmployee(label):
    array = label.split(' ')
    name = array[0]
    surname = array[1]
    idOfTheStudent = getTheIdOfEmployee(name, surname)

    try:
        connection = psycopg2.connect(database="facemob", user="postgres", password="12345678",
                                      host="127.0.0.1", port="5432")

    except psycopg2.Error as err:
        print("Error with DB")

    else:
        print("Connection estabilished!")


    cursor = connection.cursor()
    cursor.execute('INSERT INTO presence( employee_id, date, entrance_time) '
                   'VALUES( %s, %s, %s)',
                   (idOfTheStudent , str(datetime.date.today()), str(datetime.datetime.now())))

    connection.commit()
    connection.close()


def exitEmployee(label):

    array = label.split(' ')
    name = array[0]
    surname = array[1]
    idOfEmployee = getTheIdOfEmployee(name, surname)
    try:
        connection = psycopg2.connect(database="facemob", user="postgres", password="12345678",
                                      host="127.0.0.1", port="5432")

    except psycopg2.Error as err:
        print("Error with DB")

    else:
        print("Connection estabilished!")

    cursor = connection.cursor()

    cursor.execute(
        'UPDATE presence SET exit_time=%s '
        'where employee_id = %s and exit_time is Null '
        'and date = %s',
        (str(datetime.datetime.now()), idOfEmployee, str(datetime.date.today())))

    connection.commit()
    connection.close()


def getActivityOfEmployeesByName(fullname):
    array = fullname.split(' ')
    idOfEmployee = getTheIdOfEmployee(array[0], array[1])
    cursor = connectToDatabase().cursor()
    cursor.execute(
    "select employee.name, employee.surname,  employee.position,"
    "presence.date, presence.entrance_time, "
    "presence.exit_time from employee "
    "inner join  presence " 
    "on employee.id = presence.employee_id "
    "where employee.id =%s", (idOfEmployee,))
    records = cursor.fetchall()
    return records


def getActivityOfEmployeesByDate(date):
    cursor = connectToDatabase().cursor()
    formatedDate = formatDate(date)
    cursor.execute(
    "select employee.name, employee.surname,  employee.position, "
    "presence.date, presence.entrance_time, "
    "presence.exit_time from employee "
    "inner join  presence "
    "on employee.id = presence.employee_id "
    "where presence.date = %s", (formatedDate,))
    records = cursor.fetchall()
    return records

def getActivityOfEmployeesByNameAndDate(fullname, date):
    array = fullname.split(' ')
    idOfEmployee = getTheIdOfEmployee(array[0], array[1])
    cursor = connectToDatabase().cursor()
    formatedDate = formatDate(date)
    cursor.execute(
        "select employee.name, employee.surname,  employee.position,"
        "presence.date, presence.entrance_time,"
        "presence.exit_time from employee "
        " inner join  presence"
        " on employee.id = presence.employee_id"
        " where employee.id =%s and presence.date=%s", (idOfEmployee, formatedDate))
    records = cursor.fetchall()
    return records

def getActivityOfEmployees():
    cursor = connectToDatabase().cursor()
    cursor.execute(
        "select employee.name, employee.surname, employee.position, "
        " presence.date, presence.entrance_time, "
        " presence.exit_time from employee "
        " inner join  presence "
        " on employee.id = presence.employee_id")
    records = cursor.fetchall()
    return records

def getTheHoursOfEmployeesByMonth(fullName, year, month):
    cursor = connectToDatabase().cursor()
    array = fullName.split(' ')
    id = getTheIdOfEmployee(array[0], array[1])
    cursor.execute(
        "select  employee.name, employee.surname, "
        "presence.date, sum(extract (hours from "
        "(presence.exit_time - presence.entrance_time))) "
        "from employee inner join presence "
        "on employee.id = presence.employee_id "
        "where extract(year from date)=%s "
        "and extract(month from date)=%s "
        "and presence.employee_id=%s "
        "group by presence.date, employee.name, employee.surname", (year, month, id))
    records = cursor.fetchall()
    return records

def get10LatestEmployees():
    cursor = connectToDatabase().cursor()
    cursor.execute(
        "select  name, surname, position "
        " from employee order by id desc"
        " LIMIT 10")
    records = cursor.fetchall()
    return records

def getAllLoggedInEmployeesForToday():
    cursor = connectToDatabase().cursor()
    cursor.execute(
        "select  distinct employee.name,  employee.surname, presence.entrance_time"
        " from employee inner join"
        " presence on employee.id = presence.employee_id"
        " where presence.date = %s ", (str(datetime.date.today()), ))
    records = cursor.fetchall()
    return records

def getMaleEmployees():
    cursor = connectToDatabase().cursor()
    cursor.execute(
        "select  count(*)"
        " from employee where"
        " gender=%s", ('Mashkull',))
    records = cursor.fetchall()
    if records:
        return records[0][0]
    return 0

def getFemaleEmployees():
    cursor = connectToDatabase().cursor()
    cursor.execute(
        "select  count(*)"
        " from employee where"
        " gender=%s", ('Femër',))
    records = cursor.fetchall()
    if records:
        return records[0][0]
    return 0

def getNumberOfEmployeesPerDay(date):
    cursor = connectToDatabase().cursor()
    cursor.execute(
        "select  count(Distinct employee_id)"
        " from presence where"
        " date=%s", (date,))
    records = cursor.fetchall()
    if records:
        return records[0][0]
    return 0


def getAllPositionsOfEmployees():
    cursor = connectToDatabase().cursor()
    cursor.execute(
        "select  Distinct position "
        "from employee ")
    records = cursor.fetchall()
    return records

def getTheNumberForEachPosition(position):
    cursor = connectToDatabase().cursor()
    cursor.execute(
        "select  count(*) "
        " from employee where"
        " position =%s", (position,))
    records = cursor.fetchall()
    if records:
        return records[0][0]
    return 0

def getFullNameById(id):
    cursor = connectToDatabase().cursor()
    cursor.execute(
        "select  name, surname "
        " from employee where id=%s",(id,))
    records = cursor.fetchone()
    return records[0]+" "+records[1]
