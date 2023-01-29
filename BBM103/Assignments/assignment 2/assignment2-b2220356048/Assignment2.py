import os

datas = []
patients = []

# file functions
currentDirectory = os.getcwd()
outpuFileName = "doctors_aid_outputs.txt"
outputFilePath = os.path.join(currentDirectory, outpuFileName)

def readInputFile():
    fileName = "doctors_aid_inputs.txt"
    filePath = os.path.join(currentDirectory, fileName)
    global datas
    with open(filePath, "r") as _file:
        while True:
            data = _file.readline()
            if data == "":  # last line check
                break
            else:
                # delete \n which is end of the line
                data = data.replace("\n", "")
                datas.append(data)

def createOutputFile():
    _file = open(outputFilePath, "w")  # write text to the file
    _file.write("")
    _file.close()

def writeFile(text, line=True):
    _file = open(outputFilePath, "a")  # append text to the file
    if(line):
        text += "\n"
    _file.write(text)
    _file.close()

# datas funcitons
def checkPatient(patientName):
    for patient in patients:
        if(patient[0] == patientName):
            return True
    return False

def getIndexOfPatient(patientName):
    if checkPatient(patientName):
        for i in range(len(patients)):
            if(patients[i][0] == patientName):
                return i
    return -1

def createNewPatient(patient):
    patientName = patient[0]
    if(checkPatient(patientName)):
        writeFile("Patient {} cannot be recorded due to duplication.".format(patientName))
    else:
        patients.append(patient)
        writeFile("Patient {} is recorded.".format(patientName))

def removePatient(patientName):
    index = getIndexOfPatient(patientName)
    if(index != -1):
        patients.pop(index)
        writeFile("Patient {} is removed.".format(patientName))
    else:
        writeFile("Patient {} cannot be removed due to absence.".format(patientName))

def calculateProbability(index):
    _diseaseInsidence = patients[index][3].split("/")
    diseaseInsidence = int(_diseaseInsidence[0]) / int(_diseaseInsidence[1])
    diagnosisAccuracy = float(patients[index][1])
    probability =  (diseaseInsidence / ((1-diagnosisAccuracy) + diseaseInsidence))
    probability = str(probability)[:6] #for % i multiply the value with 100 and take 4 digits so i return 6 digits
    return probability

def recommendation(patientName):
    index = getIndexOfPatient(patientName)
    if(index != -1):
        _probability = float(calculateProbability(index))
        if(_probability > float(patients[index][5])):
            writeFile("System suggests {} to have the treatment.".format(patients[index][0]))
        else:
            writeFile("System suggests {} NOT to have the treatment.".format(patients[index][0]))
    else:
        writeFile("Recommendation for {} cannot be calculated due to absence.".format(patientName))

def probability(patientName):
    index = getIndexOfPatient(patientName)
    if(index != -1):
        probability = calculateProbability(index)
        probability = str(float(probability) * 100)
        if(probability[-1] == '0'):
            probability = probability[:-2] # delete .0 
        probability += "%"
        writeFile("Patient {} has a probability of {} of having {}.".format(patientName, probability,patients[index][2].lower()))
    else:
        writeFile("Probability for {} cannot be calculated due to absence.".format(patientName))

def listPatients():
    writeFile("Patient\tDiagnosis\tDisease\t\t\tDisease\t\tTreatment\t\tTreatment")
    writeFile("Name\tAccuracy\tName\t\t\tIncidence\tName\t\t\tRisk")
    writeFile("-------------------------------------------------------------------------")
    for patient in patients:
        for i in range(len(patient)):
            tabCount = 0
            tabCount -= len(patient[i]) // 4 # change the tab count by lenght of the item
            if(i == 0 and patient[i] == "Su"):
                tabCount += 2 # 2*4 = 8 character
                writeFile(patient[i]+("\t"*tabCount), line=False)
            elif(i == 1):
                value = str(float(patient[1]) * 100)
                if(len(value)< 5): #4 numbers 1 .
                    value += "0" *(5 - len(value)) 
                writeFile(value + "%\t\t",line=False)
            elif(i == 2 and patient[i]):
                tabCount += 4
                writeFile(patient[i]+("\t"*tabCount), line=False) 
            elif(i == 4):
                tabCount += 4
                writeFile(patient[i]+("\t"*tabCount), line=False) 
            elif(i == len(patient) - 1):
                text = str(float(patient[i]) * 100) 
                if(text.__contains__(".0")):
                    text = text[:-2]
                writeFile(text+ "%") #end of the line
            else:
                writeFile(patient[i]+"\t",line=False)

# main program
readInputFile()  # read all lines of file and add to the "datas" array
createOutputFile()  # creat empty output file
for data in datas:
    command = data.split()[0]
    if(command == "list"):
        listPatients()
    elif (command == "create"):
        data = data.split(", ")
        data[0] = data[0].split(" ")[1]
        createNewPatient(data)
    else:
        data = data.split(" ")
        data.pop(0)
        if(command == "remove"):
            removePatient(data[0])
        elif(command == "probability"):
            probability(data[0])
        elif(command == "recommendation"):
            recommendation(data[0])

'''
Yusuf İpek
2220356048
'''