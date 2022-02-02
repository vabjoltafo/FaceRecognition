
#Utility File with functions that help converting

def getTheDateFromDictionary(date):
    dateFormat = ''
    if date :
        day = date['day_selected']
        month = date['month_selected']
        year = date['year_selected']
        dateFormat = str(year) + '-'+ str(month) + '-' + str(day)
    return dateFormat

# From m-d-y to m/d/y
def formatDate(date):
    list = str(date).split('/')
    return list[2]+'-'+list[1]+'-'+list[0]

# list with full name of employees
def getEmployeeFullNameList(list):
    newList = ["",]
    for i in list:
        if i[0] is not None:
            string = i[0]+ ' ' + i[1]
            newList.append(string)
    return newList

def getEmployeeFullNameList2(list):
    newList = []
    for i in list:
        if i[0] is not None:
            string = i[0]+ ' ' + i[1]
            newList.append(string)
    return newList


def formatDateFromTimestamp(date):
    string = date.split('-')
    return string[2]+'/'+string[1]+'/'+string[0]


def formatDateDayMonth(date):
    string = date.split('-')
    return string[2] + '/' + string[1]


def getTimeFromTimestamp(datetime):
    string = datetime.split(' ')
    time = string[1].split(':')
    return time[0] + ':' + time[1] + ':' + time[2]


def editListOfActivities(list):
    new_list = []
    for i in list:
        smallList=[]
        for j in range(len(i)):
            if j is 3:
                if i[3] is not None:
                    editedDate = formatDateFromTimestamp(str(i[3]))
                    smallList.append(editedDate)
                else:
                    smallList.append('')
            elif j is 4:
                if i[4] is not None:
                    editedEntranceTime = getTimeFromTimestamp(str(i[4]))
                    smallList.append(editedEntranceTime)
                else:
                    smallList.append('')
            elif j is 5:
                if i[5] is not None:
                    editedExitTime = getTimeFromTimestamp(str(i[5]))
                    smallList.append(editedExitTime)
                else:
                    smallList.append('')
            else:
               smallList.append(i[j])
        new_list.append(smallList)
    return new_list


def editListOfEntrance(list):
    new_list = []
    for i in list:
        smallList=[]
        for j in range(len(i)):
            if j is 2:
                if i[2] is not None:
                    editedDate = getTimeFromTimestamp(str(i[2]))
                    smallList.append(editedDate)
                else:
                    smallList.append('')
            else:
               smallList.append(i[j])
        new_list.append(smallList)
    return new_list