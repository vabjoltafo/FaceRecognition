from datetime import datetime, timedelta

from Enums import Months
from Repositories.EmployeeRepository import getNumberOfEmployeesPerDay, getAllPositionsOfEmployees, \
    getTheNumberForEachPosition, getTheInfomationFromEmployees, getAllEmployeeNameAndSurname, \
    getTheHoursOfEmployeesByMonth
from Repositories.KontributeRepository import getAllKontribute
from Repositories.WageEmployeeRepository import selectWageOfEmployee, hasOrarWage
from Utilities.Convertors import getEmployeeFullNameList, getEmployeeFullNameList2


def getInformation():
    dates = []
    number = []
    new_list=[]
    for i in range(15):
        dateTime = datetime.today() - timedelta(days=i)
        dates.append(dateTime.date())
        number.append(getNumberOfEmployeesPerDay(dateTime.date()))
    new_list.append(dates)
    new_list.append(number)
    return new_list


def extractPositions():
    new_List =[]
    list = getAllPositionsOfEmployees()

    for i in list:
        new_List.append(i[0])

    return new_List


def getDataForEmployeePosition():
    positionList = extractPositions()
    numberPerPosition  = []
    full_list = []

    for i in positionList:
        numberPerPosition.append(getTheNumberForEachPosition(i))

    full_list.append(positionList)
    full_list.append(numberPerPosition)

    return full_list

def isNumber(num):
    if isinstance(num, int) or isinstance(num, float):
        return True
    return False

def isANumber(number):
    for i in list(str(number)):
        if i is not '1' and i is not '0' and\
            i is not '2' and i is not '3' and\
            i is not '4' and i is not '5' and i is not '6' and \
            i is not '7' and i is not '8' and i is not '9':
            return False
    return True

def filterData(filter, list):
    newlist=[]
    for i in list:
        if str(filter).lower() in (str(i).lower()):
            newlist.append(i)
    return newlist


def insertCrudOperations(list):
    new_list = []

    for i in list:
        item = []
        for j in range(len(i)):
            item.append(i[j])
        item.append("Ndrysho")
        item.append("Elemino")
        new_list.append(item)
    return new_list

def getAllEmployeeSalary(month, year):
    int_month = Months.MONTHS_DICT[month]
    full_list = []
    employeeList = getEmployeeFullNameList2(getAllEmployeeNameAndSurname())

    for i in employeeList:
        data_list = getDataForEmployeeSalary(i, getTheHoursOfEmployeesByMonth(i, float(year), float(int_month)))
        wage = "-"

        if hasOrarWage(i):
            wage = data_list[1]

        new_list = [str(i).split(" ")[0], str(i).split(" ")[1], wage, data_list[0], data_list[8]]
        full_list.append(new_list)

    return full_list


def getDataForEmployeeSalary(employeeName, record):
    totalHours = 0

    for i in record:
        for j in range(len(i)):
            if j == 3:
                if i[j] is not None:
                    totalHours = totalHours + int(i[j])
                else:
                    totalHours = totalHours + 0

    wage = 0.0

    pagaBruto = 0.0


    # kontroll nqs punonjesi eshte
    # me page orare
    if hasOrarWage(employeeName):
        wage = selectWageOfEmployee(employeeName)
        pagaBruto = (float)(wage[0]) * float(totalHours)
    else:
        if selectWageOfEmployee(employeeName) is None:
            pagaBruto = 0.0
        else:
            pagaBruto = float(selectWageOfEmployee(employeeName)[0])

    kontribute = getAllKontribute()

    kontribute_shendetsore_value = (float(kontribute[1]) / 100) * float(pagaBruto)
    kontribute_shendetsore_string = str((kontribute[1]) / 100) + ' * ' + str(pagaBruto) + ' = ' + str(kontribute_shendetsore_value)

    kontribute_shoqerore_value = (float(kontribute[2]) / 100) * float(pagaBruto)
    kontribute_shoqerore_string = str((kontribute[2]) / 100) + ' * ' + str(pagaBruto) +' = ' + str(kontribute_shoqerore_value)

    tap1_value = 0
    tap1_string = ''

    tap2_value = 0
    tap2_string = ''

    tap3_value = 0
    tap3_string = ''

    if pagaBruto < 30000:
        tap1_value = (float(kontribute[3]) / 100) * float(pagaBruto)
        tap1_string = str((kontribute[3]) / 100) + ' * ' + str(pagaBruto) + ' = ' + str(tap1_value)

    elif 30000 <= pagaBruto < 150000:
        tap2_value = (float(kontribute[4]) / 100) * (float(pagaBruto) - 30000)
        # tap2_string = str((kontribute[4]) / 100) +' * ' + '('+pagaBruto +' - '+' 30000) = '+ str(tap2_value)

    elif pagaBruto >= 150000:
        tap2_value = (float(kontribute[4]) / 100) * (float(pagaBruto) - 30000)
        tap3_value = (float(kontribute[5]) / 100) * (float(pagaBruto) - 150000)
        # tap3_string = str((kontribute[4]) / 100) + ' * ' + '(' + str(pagaBruto) + ' - ' + ' 30000) = ' + str(tap2_value)

    pagaNeto = pagaBruto - (kontribute_shendetsore_value + kontribute_shoqerore_value + tap1_value + tap2_value + tap3_value)

    list = [totalHours, wage, '%.2f' % pagaBruto, '%.2f' % kontribute_shoqerore_value, '%.2f' % kontribute_shendetsore_value, '%.2f' % tap1_value, '%.2f' % tap2_value, '%.2f' % tap3_value, '%.2f' % pagaNeto]

    return list

