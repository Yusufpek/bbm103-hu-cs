import os
import sys

#constanst
studentFare = 10
fullFare = 20
seasonFare = 250
commandsDic = {
    "create":"CREATECATEGORY",
    "sell":"SELLTICKET",
    "cancel": "CANCELTICKET",
    "balance": "BALANCE",
    "show": "SHOWCATEGORY"}
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
seatSymbols = {"student":"S", "season": "T", "full":"F"}
#
commands = []
categories = {}

# file functions
currentDirectory = os.getcwd()
outpuFileName = "output.txt"
outputFilePath = os.path.join(currentDirectory, outpuFileName)
def readInputFile():
    fileName = sys.argv[1]
    filePath = os.path.join(currentDirectory, fileName)
    global datas
    with open(filePath, "r") as _file:
        while True:
            command = _file.readline()
            if command == "":  # last line check
                break
            else:
                # delete \n which is end of the line
                command = command.replace("\n", "")
                commands.append(command)

def createOutputFile():
    _file = open(outputFilePath, "w")  # write text to the file
    _file.write("")
    _file.close()

def write(text, line=True):
    _file = open(outputFilePath, "a")  # append text to the file
    if(line):
        text += "\n" 
    print(text, end='')
    _file.write(text)
    _file.close()

#commands
def checkCategory(categoryName): #check category existance
    return (categories.__contains__(categoryName))

def checkSeat(categoryName, seat):
    return(categories[categoryName]["seats"].__contains__(seat))

def checkColumnOrRow(categoryName,seats):
    columnExist = True
    rowExist = True
    _seats = seats
    #in selling send a list example: D4-54 -> ["D4", "54"]
    #in cancelling send a string example: "U32" for checking row and column convert to list for this item -> ["U32", "32"] 
    if(not (type(seats) is list)): 
        seats = [seats, seats[1:]]
    # for example seats: D4-54
    if(checkSeat(categoryName,seats[0][0] + "0")): #check D0
        #if row's first column is exist but the given index does not exist
        columnExist = False
    if(checkSeat(categoryName, "A" + seats[1])): #check A54
        rowExist = False
    text = ""
    if((not columnExist) and (not rowExist)):
        text = "row and column"
    elif(not columnExist):
        text = "column"
    elif(not rowExist):
        text = "row"
    #for printing make a string like D4-54 or U32
    if((type(_seats) is list)):
       _seats = seats[0] + "-" + seats[1] 
    write("Error: The category '{}' has less {} than the specified index {}!".format(categoryName, text, _seats))

def createCategory(categoryName, rowsAndColumns):
    if  not (checkCategory(categoryName)):
        (rows,columns) = map(int, rowsAndColumns.split("x")) #split row and column counts and convert to int
        if(rows <= 26):
            seats = {}
            for i in range(rows):
                for j in range(columns):
                    seats[letters[i] + str(j)] = "X"
            categoryNamesInformations = {"student": 0, "full": 0, "season":0, "seats": seats, "row": rows ,"column": columns}
            categories[categoryName] = categoryNamesInformations
            write("The category '{}' having {} seats has been created".format(categoryName,rows*columns))
        else:
            write("Error: the rows count is bigger thane 26")
    else: 
        write("Warning: Cannot create the category for the second time. The stadium has already {}".format(categoryName))

def sellTicket(name, ticketType, categoryName, seats):
    if(checkCategory):
        for seat in seats:
            if(len(seat) == 2):
                    if(checkSeat(categoryName,seat)):
                        if(categories[categoryName]["seats"][seat] == "X"):
                            categories[categoryName]["seats"][seat] = seatSymbols[ticketType]
                            categories[categoryName][ticketType] += 1
                            write("Success: {} has bought {} at {}".format(name, seat, categoryName))
                        else:
                            write("Warning: The seat "+seat+" cannot be sold to alex since it was already sold") 
                    else:
                        write("Error: The category '{}' has not the specified index {} seat!".format(categoryName,seat))
            else:
                isExist = True
                isSold = False
                _seats = seat.split("-")
                countRange = int(_seats[1]) - int(_seats[0][1]) + 1 # Example: C9-12: C9,C10,C11,C12
                for i in range(countRange): #check for existance
                    _seat = _seats[0][0] + str(int(_seats[0][1]) + i)
                    if not (checkSeat(categoryName, _seat)):
                        isExist = False
                        break
                if(isExist):
                    for j in range(countRange): # cehck for not sold
                        _seat = _seats[0][0]+str(int(_seats[0][1]) + j)
                        if(categories[categoryName]["seats"][_seat] != "X"):
                            isSold = True
                            break
                    if(isSold):
                        write("Warning: The seats {} cannot be sold to {} due some of them have already been sold".format(seat,name))
                    else:
                        #sell the tickets
                        for k in range(countRange):
                            _seat = _seats[0][0]+str(int(_seats[0][1]) + k)
                            categories[categoryName]["seats"][_seat] = seatSymbols[ticketType]
                            categories[categoryName][ticketType] += 1
                        write("Success: {} has bought {} at {}".format(name, seat, categoryName))
                else:
                    checkColumnOrRow(categoryName,_seats)
    else:
        write("Error: The category '{}' is not exsist".format(categoryName))

def cancelTicket(categoryName, seats):
    for seat in seats:
        if(checkCategory(categoryName)):
            if(checkSeat(categoryName,seat)):
                if(categories[categoryName]["seats"][seat] != "X"):
                    ticketType = categories[categoryName]["seats"][seat]
                    index = list(seatSymbols.values()).index(ticketType)
                    _type = list(seatSymbols)[index]
                    categories[categoryName][_type] -= 1
                    categories[categoryName]["seats"][seat] = "X"
                    write("Success: The seat {} at {} has been canceled and now ready to sell again".format(seat, categoryName))
                else:
                    write("Error: The seat {} at '{}' has already been free! Nothing to cancel".format(seat,categoryName))
            else:
                checkColumnOrRow(categoryName, seat)
        else:
            write("Error: The category '{}' is not exsist".format(categoryName))

def balance(categoryName):
    infos = categories[categoryName]
    students = infos["student"]
    full = infos["full"]
    season = infos["season"]
    revenues = students * studentFare + full * fullFare + season * seasonFare
    write("Sum of students = {}, Sum of full pay = {}, Sum of season ticket = {}, and Revenues = {} Dollars".format(students, full, season, revenues))

def showCategory(categoryName):
    seats = categories[categoryName]["seats"]
    row = categories[categoryName]["row"]
    col = categories[categoryName]["column"]
    write("Printing category layout of "+categoryName)
    for i in range(row,-1,-1):
        i -= 1
        if(i > -1): write(letters[i] + " ", line= False)
        for j in range(col):
            if(i > -1):
                write(seats[letters[i]+ str(j)], line = False)
                if(j < col - 1): write("  ", line= False)
            else:
                blanketCount = (3 - len(str(j)))
                write( blanketCount * " "+ str(j), line=False)
        write("")
    write("Category report of '{}'".format(categoryName))
    write("-------------------------------")

#main program
readInputFile()
createOutputFile() #clear output file
for command in commands:
    _command = command.split(" ")
    if (_command[0] == commandsDic["create"]):
        createCategory(_command[1],_command[2])
    elif (_command[0] == commandsDic["sell"]):
        sellTicket(_command[1], _command[2], _command[3], _command[4:])
    elif (_command[0] == commandsDic["cancel"]):
        cancelTicket(_command[1], _command[2:])
    elif (_command[0] == commandsDic["balance"]):
        balance(_command[1])
    elif (_command[0] == commandsDic["show"]):
        showCategory(_command[1])