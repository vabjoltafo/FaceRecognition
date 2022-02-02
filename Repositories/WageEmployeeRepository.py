import psycopg2
from Repositories.EmployeeRepository import getTheIdOfEmployee


def connectToDatabase():
    try:
        connection = psycopg2.connect(database = "facemob", user = "postgres", password = "12345678",
                    host = "127.0.0.1", port = "5432")

    except psycopg2.Error as err:
        print("Error with DB")

    else:
        print("Connection estabilished!")

    return connection

def selectWageByEmployeeId(fullname):
    array = fullname.split(' ')
    employeeId = getTheIdOfEmployee(array[0], array[1])
    cursor = connectToDatabase().cursor()
    cursor.execute("SELECT * FROM employee_wage where employee_id =%s", (employeeId,))
    records = cursor.fetchone()
    return records

def selectWageOfEmployee(fullname):
    array = fullname.split(' ')
    employeeId = getTheIdOfEmployee(array[0], array[1])
    cursor = connectToDatabase().cursor()
    cursor.execute("SELECT paga_orare FROM employee_wage where employee_id =%s", (employeeId,))
    records = cursor.fetchone()
    return records

def selectWageById(id):

    cursor = connectToDatabase().cursor()
    cursor.execute("SELECT * FROM employee_wage where id =%s", (id,))
    records = cursor.fetchone()
    return records

def hasOrarWage(fullname):
    array = fullname.split(' ')
    employeeId = getTheIdOfEmployee(array[0], array[1])
    cursor = connectToDatabase().cursor()
    cursor.execute("SELECT orar FROM employee_wage where employee_id =%s", (employeeId,))
    records = cursor.fetchone()
    if records is not None and records[0] == '1':
        return True
    return False

def insertWageOfEmployee(fullname, wage, orare):
    array = fullname.split(' ')
    employeeId = getTheIdOfEmployee(array[0], array[1])

    try:
        connection = psycopg2.connect(database="facemob", user="postgres", password="12345678",
                                      host="127.0.0.1", port="5432")

    except psycopg2.Error as err:
        print("Error with DB")

    else:
        print("Connection estabilished!")

    cursor = connection.cursor()

    cursor.execute('INSERT INTO employee_wage(employee_id, paga_orare, orar) VALUES(%s, %s, %s) ', (employeeId, wage, orare))

    connection.commit()
    connection.close()

def selectDataToDisplay():
    cursor = connectToDatabase().cursor()
    cursor.execute(
        "select  employee.name, employee.surname,  employee.position,"
        " employee_wage.paga_orare "
        " from employee "
        "inner join  employee_wage "
        "on employee.id = employee_wage.employee_id ")
    records = cursor.fetchall()
    return records


def updateWage(id, wage, orare):
    try:
        connection = psycopg2.connect(database="facemob", user="postgres", password="12345678",
                                      host="127.0.0.1", port="5432")

    except psycopg2.Error as err:
        print("Error with DB")

    else:
        print("Connection estabilished!")

    cursor = connection.cursor()

    cursor.execute('UPDATE  employee_wage  SET paga_orare=%s, orar=%s WHERE id=%s', (wage, orare, id))

    connection.commit()
    connection.close()

def deleteWage(id):
    try:
        connection = psycopg2.connect(database="facemob", user="postgres", password="12345678",
                                      host="127.0.0.1", port="5432")

    except psycopg2.Error as err:
        print("Error with DB")

    else:
        print("Connection estabilished!")

    cursor = connection.cursor()

    cursor.execute('Delete from employee_wage  WHERE id=%s', (id, ))

    connection.commit()
    connection.close()



