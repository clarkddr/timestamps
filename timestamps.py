from datetime import datetime, timedelta

def welcome():    
    menuSelected = showMainMenu()
    while menuSelected:
        if(menuSelected == 1):
            showTimestamps(False)  # when True, shows enumerated items.          
            welcome()
            break        
        elif(menuSelected == 2):
            insertTimestamp()
            welcome()
            break
        elif(menuSelected == 3):
            deleteTimestamp()
            welcome()
            break
        elif(menuSelected == 4):
            deleteSection()
            welcome()
            break        
        elif(menuSelected == 5):
            print('Adios')
            exit()
        else:            
            print('\n')
            print('==============================')        
            print('El numero seleccionado no es válido')
            print('==============================')
            print('\n')        

def showMainMenu():
    print('Ingresa la opción deseada')
    print('1. Mostrar Timestamps')
    print('2. Agregar Timestamp')
    print('3. Eliminar Timestamp')
    print('4. Eliminar sección')
    print('5. Salir')
    option = getInputMenu()
    return option

def getInputTime():
    while True:
        time = input("Introduce el tiempo en formato 'mm:ss' o 'hh:mm:ss' (Ejemplo: 1:30 o 1:15:30): ")
        parts = time.split(':')
        if len(parts) == 2:
            minute = parts[0]
            second = parts[1]
            if minute.isdigit() and second.isdigit() and int(minute) < 60 and int(second) < 60:
                return ''.join([minute,':', second.zfill(2)])
        if len(parts) == 3:
            hour = parts[0]
            minute = parts[1]
            second = parts[2]
            if hour.isdigit() and minute.isdigit() and second.isdigit() and int(minute) < 60 and int(second) < 60:
                return ''.join([hour, ':', minute.zfill(2), ':', second.zfill(2)])
        print("Formato inválido. Intentalo de nuevo.")

def getInputMenu():
    while True:
        option = input()
        availableOptions = ['1','2','3','4','5']
        if option.isdigit() and option in availableOptions:    
            return int(option)
        print('Opción inválida. Intentalo de nuevo.')
    
def showTimestamps(withNumber):
    def listTsList():
        for index,element in enumerate(tsList):
            if withNumber:
                idx = str(index +1) + ' '
            else:
                idx = ''
            textToShow = ''.join([idx, formatTimeToShow(str(element['time'])),' ',element['name']])
            print(textToShow)
    print('\n')
    print('Timestamps')
    print('==============================')
    if(len(tsList) > 0):
        listTsList()
    else:
        print('Aun no hay timestamps')              
    print('==============================')
    print('\n')

def convertToTimedelta(time):
    timeSplitted = time.split(':')
    if len(timeSplitted) == 3:
        time = datetime.strptime(time, "%H:%M:%S")
        deltaTime = timedelta(hours=time.hour,minutes=time.minute,seconds=time.second)            
    if len(timeSplitted) == 2:
        time = datetime.strptime(time, "%M:%S")
        deltaTime = timedelta(minutes=time.minute,seconds=time.second)        
    return deltaTime        

def isTimeGreater(lastTs,newTs):
    last = convertToTimedelta(lastTs).total_seconds()
    new = convertToTimedelta(newTs).total_seconds()
    return new >= last
    
def getLastTsTime(lista):
    if len(lista) == 0:
        return "0:00"
    index = len(lista) -1
    time = lista[index]['time']
    return time

def insertTimestamp():
    timestamp = {}    
    timestamp['name'] = input('Nombre del Timestamp ')
    if len(tsList) == 0:        
        timestamp['time'] = "0:00"        
    else:
        timestamp['time'] = getInputTime()
    lastTsTime = getLastTsTime(tsList)    
    print('\n')
    print('==============================')
    if isTimeGreater(lastTsTime,timestamp['time']):
        try:
            tsList.append(timestamp)
            print('El Timestamp ha sido agregado exitosamente.\n')
            showTimestamps(False)
        except:
            print('El Timestamp no ha podido agregarse, intente de nuevo.\n')
    else:
        print('El tiempo del timestamp no es mayor al ultimo, intente de nuevo.')

def deleteTimestamp():  
    def updateTimesDeletingElement(list):
        prev_value = None
        for index,element in enumerate(list):
            curr_value = element['time']
            if prev_value is not None:
                element['time'] = prev_value
            prev_value = curr_value
    if (len(tsList) == 0):
        text = '\n'\
               '================================\n'\
               'No hay timestamps para eliminar.\n'\
               '================================\n'\
               '\n'
        return print(text) 
    showTimestamps(True)
    tsToDelete = input('¿Cual timestamp deseas eliminar? ')
    tsToDelete = int(tsToDelete) -1
    updateTimesDeletingElement(tsList[tsToDelete:])
    del tsList[tsToDelete]
    print('Timestamp eliminado con éxito.')       
    showTimestamps(False)    

def deleteSection():
    if (len(tsList) == 0):
        text = '================================\n'\
                'No hay timestamps para eliminar.\n'\
                '================================\n'\
                '\n'
        return print(text) 
    print('¿De cuanto tiempo es la sección que quieres borrar?')
    duration = convertToTimedelta(getInputTime())
    print('¿A partir de que parte quieres eliminar la sección?')
    fromTime = convertToTimedelta(getInputTime())
    lastTsTime = convertToTimedelta(getLastTsTime(tsList))
    if fromTime >= lastTsTime:
        return print('No se puede eliminar esa sección de tiempo.')        
    for element in tsList:
        time = convertToTimedelta(element['time'])
        newTime = time - duration        
        if newTime > fromTime:
            element['time'] = newTime
    
def formatTimeToShow(time):
    time = convertToTimedelta(time)
    time = datetime.strptime(str(time), "%H:%M:%S")
    hour = time.hour
    minute = time.minute
    second = time.second
    if hour == 0:
        result = str(minute) + ':' + str(second).zfill(2)
        return result
    result = str(hour) + ':' + str(minute).zfill(2) + ':' + str(second).zfill(2)
    return result

"""tssList = [
    {'name':'Cero','time':'0:00'},
    {'name':'Inicio','time':'1:00'},
    {'name':'Introduccion','time':'2:00'},
    {'name':'Seccion 1','time':'3:00'},
    {'name':'Seccion 2','time':'4:00'},
    {'name':'Seccion 3','time':'5:00'},
    {'name':'Seccion 4','time':'6:00'},
    {'name':'Seccion 5','time':'7:00'},
          ]
"""

print('Bienvenido a Timestamp Manager.')
tsList = []
welcome()