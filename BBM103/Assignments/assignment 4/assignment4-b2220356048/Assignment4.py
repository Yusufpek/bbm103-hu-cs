from io import TextIOWrapper# for defining file variable
import sys                  # for getting command line arguments
import string               # for getting alpahet
import copy                 # for copying just values of a initial dictionary

outputFileName = "Battleship.out"       # output file name
alpahet = list(string.ascii_uppercase)  # alpahet list
initialBoats = {
    #keys are: first letters of {size, counts, names, indexes}
    'C': {'s': 5, 'c': 1, 'n': 'Carrier\t' , 'i': []},
    'B': {'s': 4, 'c': 2, 'n': 'Battleship', 'i': []},
    'D': {'s': 3, 'c': 1, 'n': 'Destroyer', 'i': []},
    'S': {'s': 3, 'c': 1, 'n': 'Submarine', 'i': []},
    'P': {'s': 2, 'c': 4, 'n': 'Patrol Boat', 'i': []},
}

class Player:
    def __init__(self, position_txt, moves_in): # get input files name
        self.position_txt = position_txt
        self.moves_in = moves_in
    
    def createPlayer(self, name):  # create player
        self.index = 0
        self.name = name
        self.positions =splitStartPosition(readInputFile(self.position_txt))
        self.moves = splitMoves(readInputFile(self.moves_in))
        self.board = [["-" for i in range(10)]for j in range(10)]
        self.boats = self.getBoatsIndex()
        self.groupingBoats()

    def getBoatsIndex(self):
        boats = copy.deepcopy(initialBoats) # just get initial values
        for i in range(10):
            for j in range(10):
                data = self.positions[i][j]
                if(data != "-"):
                    boats[data]['i'].append(str(i)+str(j))
        return boats
    
    def checkRowOrColumn(self,boatsIndexes:list, item:int, size:int, row = True):
        _range : range
        if(row): 
            _range = range(item, item + size)
        else: 
            _range = range(item, (item + size * 10), 10)
        for j in _range:
            j = str(j)
            if(len(j) < 2): j = "0" + j
            if(boatsIndexes.__contains__(j)):
                isFound = True
            else:
                isFound = False
                break

        if(isFound):
            newIndexes = []
            for i in _range:
                i = str(i)
                if(len(i) < 2): i = "0" + i
                newIndexes.append(str(i))
                boatsIndexes.remove(str(i))
            return newIndexes
        return []
    
    def groupingBoats(self): # grouping the boats/ get indexes and group them
        for boat in initialBoats:
            size = initialBoats[boat]['s'] 
            i = 0
            newIndexes = []
            while(i < len(self.boats[boat]['i'])):
                item = self.boats[boat]['i'][i]
                #check for same row
                row = self.checkRowOrColumn(self.boats[boat]['i'], int(item), size)
                if(row):  
                    newIndexes.append(row)
                    i = 0
                    continue
                #check for same column
                column = self.checkRowOrColumn(self.boats[boat]['i'], int(item), size, row=False)
                if(column): 
                    newIndexes.append(column)
                    i = 0 
                else: 
                    i += 1
            self.boats[boat]['i'] = newIndexes    

    def checkBoats(self): # check for the remaining boats - game over control
        for boat in initialBoats:
            if(self.boats[boat]['c'] != 0):
                return True
        return False

player1 : Player
player2 : Player

def getArguments(): # get command line arguments
    global player1
    global player2
    try:
        player1_txt = sys.argv[1]
        player2_txt = sys.argv[2]
        player1_in = sys.argv[3]
        player2_in = sys.argv[4]
        player1 = Player(player1_txt, player1_in)
        player2 = Player(player2_txt, player2_in)
        return True
    except:
        writeOutput("command line arguments error !")
        return False

def readInputFile(fileName):
    dataList = []
    try:
        with open(fileName,"r") as _file:
            dataList = [line.replace("\n","") for line in _file.readlines()]
    except IOError:
        return []
    return dataList

def splitStartPosition(dataList):
    positions = []
    splittedData = [data.split(";") for data in dataList]
    linesPositions = []
    for data in splittedData:
        for _data in data:
            if(len(_data) == 0): linesPositions.append("-")
            else: linesPositions.append(_data)
        positions.append(linesPositions)
        linesPositions = []
    return positions

def splitMoves(dataList):
    #moves are in just one line
    moves = dataList[0].split(";")[:-1] # delete last empty input
    if(moves == [""]): moves = []
    return moves

def checkInputs(): # check for input files can readable
    inputs = [player1.position_txt, player1.moves_in, player2.position_txt, player2.moves_in]
    wrongInputs = ""
    for _input in inputs:
        if(not readInputFile(_input)):
            wrongInputs += _input + ", "
    if(len(wrongInputs) == 0):
        return True
    else:
        writeOutput(f"IOError: input file(s) {wrongInputs[:-2]} is/are not reachable.")
        return False

def checkMove(player):
    move = player.moves[player.index]
    splittedMove = move.split(",")
    try:
        if(len(splittedMove) < 2): 
            raise IndexError # the expected input must have 2 items (e: 1,E) not less 
        if(len(splittedMove) > 2): 
            raise ValueError # the expected input must have 2 items (e 7,J) not more
        moveIndex = int(splittedMove[0]) #if the value is wrong this gives value error
        if(moveIndex > 10 or alpahet.index(splittedMove[1]) > 9): 
            raise AssertionError 
        if(player.moves[: player.index].__contains__(move)):
            raise AssertionError
        return True
    except IndexError:
        writeOutput(f"Index Error: Move Input {move} has less index than expected !")
    except ValueError:
        writeOutput(f"Value Error: Move Input {move} is wrong !")
    except AssertionError:
        writeOutput("AssertionError: Invalid Operation.")
    except:
        writeOutput("kaBOOM: run for your life!")
    return False

def hitBoat(dic, indexes, item):
    indexes.remove(item)
    _count = 0
    for item in dic['i']:
        if (len(item) > 0):
            _count += 1
    dic['c'] = int(_count)

def gameOver(playerName = "player",isDraw = False):
    if(isDraw):
        writeOutput("It is a Draw!")
    else:
        writeOutput(f"{playerName} Wins!\n")
    printBoards(final = True)

def gameRound(round):
    players= [player1,player2]
    try:
        for i in range(len(players)):
            playerIndex = (i + 1) % 2 # other player 
            writeOutput(f"{players[i].name}'s Move\n")
            writeOutput(f"Round : {round + 1}"+ "\t" * 5 + "Grid Size: 10x10\n")
            printBoards()
            moves = players[i].moves[players[i].index]
            writeOutput(f"\nEnter your move: {moves}")
            while( not checkMove(players[i])): # form is incorrect look for correct move
                players[i].index += 1
                moves = players[i].moves[players[i].index]
                writeOutput(f"Enter your move: {moves}")
            move = moves.split(",")
            index1, index2=(int(move[0]) - 1, alpahet.index(move[1]))
            indexStr = str(index1) + str(index2)
            data = players[playerIndex].positions[index1][index2]
            dataBoard = players[playerIndex].board[index1][index2]
            if(data == "-" and dataBoard == "-"):
                players[playerIndex].board[index1][index2] = "O"
            elif(data != "-" and dataBoard == "-"):
                if(players[playerIndex].boats[data]['c'] > 0):
                    for inner in players[playerIndex].boats[data]['i']:
                        if(inner.__contains__(indexStr)):
                            hitBoat(players[playerIndex].boats[data] ,inner, indexStr)
                players[playerIndex].board[index1][index2] = "X"
            writeOutput("")
        isPlayer1Finish = not player1.checkBoats()
        isPlayer2Finish = not player2.checkBoats()
        if(isPlayer1Finish and isPlayer2Finish):
            gameOver(isDraw = True)
        elif(isPlayer1Finish):
            gameOver(player2.name)
        elif(isPlayer2Finish):
            gameOver(player1.name)
        else:
            return True
        return False # if game is over return false
    except IndexError:
        writeOutput("Index Error")
    except ValueError:
        writeOutput("Value Error")
    return False

def printBoards(final = False):
    def printBoard(player):
        board = player.board
        if(final):
            for boat in player.boats:
                dic = player.boats[boat]
                if(dic['c'] > 0):
                    for index in dic['i']:
                        for inner in index:
                            player.board[int(inner[0])][int(inner[1])] = boat
        for j in range(11):
            if(i == 0 and j == 0):
                writeOutput(" ",end="")
                continue
            if(i == 0): #write letters 
                writeOutput(" " +alpahet[j-1], end="")
            if(j == 0 and i>0): # write numbers
                writeOutput(str(i), end= " " * (2-len(str(i))))
            if(i > 0 and j > 0): # write indexes
                blanket = 1
                if(j == 10): blanket = 0
                writeOutput(board[i-1][j-1],end=" " * blanket)
    def printBoats():
        players = [player1, player2]
        for boat in initialBoats:
            for i in range(2):
                playerBoatCount = players[i].boats[boat]['c']
                output = ""
                output += (initialBoats[boat]['c'] - playerBoatCount) * "X "
                output += playerBoatCount * "- "
                if(i == 1):
                    tabCount = 0
                else:
                    if(boat == "P"):
                        tabCount = 3
                    else: tabCount = 4
                writeOutput((initialBoats[boat]['n']+ "\t" +output.rstrip() + "\t" * tabCount), end = "")
            writeOutput("")
    if(final):
        writeOutput("Final Information\n")
        output = f"{player1.name}'s Board\t\t{player2.name}'s Board"
    else:
        output = f"{player1.name}'s Hidden Board\t\t{player2.name}'s Hidden Board"
    writeOutput(output)
    for i in range(11):
        printBoard(player1)
        writeOutput("\t\t", end="")
        printBoard(player2)
        writeOutput("")
    writeOutput("")
    printBoats()

def createOutputFile():
    _file = open(outputFileName, "w")  # write text to the file
    _file.write("")
    _file.close()

outputFile: TextIOWrapper
def writeOutput(text, end = "\n"):
    outputFile.write(text + end) # append text to the file
    print(text, end=end) # write the command line

def mainProgram():
    global outputFile
    createOutputFile()
    outputFile = open(outputFileName, "a") # open the output file in append mode
    if(getArguments() and checkInputs()):
        player1.createPlayer("Player1")
        player2.createPlayer("Player2")
        writeOutput("Battle of Ships Game\n")
        i = 0
        while(player1.index < len(player1.moves) and player2.index < len(player2.moves)):
            if(not gameRound(i)):
                return "Kaboom"
            i += 1
            player1.index += 1
            player2.index += 1
        writeOutput("No Winner !")
        printBoards(final=True)
        return "Kaboom"
    else:
        return "Kaboom !"

mainProgram()
outputFile.close() # end of the program, close the output file 