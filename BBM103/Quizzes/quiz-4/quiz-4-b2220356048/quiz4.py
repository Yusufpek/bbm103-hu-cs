import sys

messages = {}
messageIDs = [] 
packets = {}

def getArguments():
    #get command line arguments, look for input and output file names 
    try:
        inputFileName = sys.argv[1]
        outputFileName = sys.argv[2]
        return (inputFileName, outputFileName)
    except IndexError:
        print("Give me more informationas, the command line arguments are less then expected")
        return False

def readData(fileName):
    #read input file
    datas = []
    try:
         with open(fileName, "r") as f:
            datas = [line.replace("\n","") for line in f.readlines()]
    except IOError:
        print(f"IO ERROR: i can not read input file with named {fileName}")
    return datas

def splitData(datas):
    #split the input data
    #use messageIDs and packets for sorting values
    global messages
    global messageIDs
    global packets
    for data in datas:
        splitedData = data.split("\t")
        messageID, packetId, message = splitedData
        if(messages.__contains__(messageID)):
            messages[messageID][packetId] = message
            packets[messageID].append(int(packetId))
        else:
            messageIDs.append(int(messageID))
            messages[messageID] = {packetId: message}
            packets[messageID] = [int(packetId)]

def sortData():
    #sort the data by converting them to integer
    messageIDs.sort()
    for id in messageIDs:
        packets[str(id)].sort()

def writeData(fileName):
    #write the data to output file
    output = ""
    def addOutput(text):
        #add output variable to text and new line character
        nonlocal output
        output+= text + "\n"
    #add the all messages to output by sorted packets ids and message ids
    index = 1
    for id in messageIDs:
        addOutput(f"Message\t{index}")
        for packet in packets[str(id)]:
            message = messages[str(id)][str(packet)]
            addOutput(f"{id}\t{packet}\t{message}")  
        index+=1
    #delete the last empty line
    output = output[:-1]
    try:
        with open(fileName, "w") as f:
            f.writelines(output)
    except IOError:
        print(f"IO ERROR: i can not write the outputs to file with named {fileName}")

#Main Program
#if the command lines is less than expected the program does not work
inputs = getArguments()
if(inputs != False):
    inputFileName, outputFileName = inputs
    data = readData(inputFileName)
    splitData(data)
    sortData()
    writeData(outputFileName)