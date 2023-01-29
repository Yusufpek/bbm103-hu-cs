import sys

operandsFile = ""
compareFile = ""

def getArguments():
    global operandsFile
    global compareFile
    try:
        operandsFile = sys.argv[1]
        compareFile = sys.argv[2]
        return True
    except IndexError:
        print("IndexError: number of input files less than expected.")
        return False

def readInputFile(fileName):
    dataList = []
    try:
        with open(fileName,"r") as _file:
            dataList = [line.replace("\n","").strip() for line in _file.readlines()]
    except IOError:
        print(f"IOError: cannot open {fileName}")
        return False
    return dataList

def checkInputFiles():
    _operands = readInputFile(operandsFile)
    _compareResults = readInputFile(compareFile)
    if(not _operands or not _compareResults):
        return False , ""
    else:
        return _operands, _compareResults
def roundImp(number):
    if(float(number) == int(float(number))):
        # it is int number
        return int(number)
    else:
        n,d = number.split(".")
        if(int(d[0]) >= 5):
            n = int(n) + 1
        return int(n)

def calculate(numbers):
    results = ""
    givenInput = f"Given input: {numbers}"
    try:
        _numbers = [roundImp(number) for number in numbers.split(" ")]
        if(len(_numbers) < 4):
            raise IndexError
        div, nonDiv, _from, to = _numbers
        while(_from <= to):
            if(_from % div == 0 and _from % nonDiv != 0):
                results += str(_from) + " "
                _from += div
            else:
                _from += 1
        return results.strip()
    except ValueError:
        return "ValueError: only numeric input is accepted.\n" + givenInput
    except IndexError:
        return "IndexError: number of operands less than expected.\n" + givenInput
    except ZeroDivisionError:
        return "ZeroDivisionError: You can't divide by 0.\n" + givenInput
    except:
        return "kaBOOM: run for your life!"

def compare(myResult, givenResult):
    try:
        assert myResult == givenResult
        return "Goool !!!"
    except AssertionError:
        return "AssertionError: results don't match."

def main():
    if(getArguments()):
        operands, compareResults = checkInputFiles()
        if(not operands):
            return "kaboom"
        else:
            for i in range(len(operands)):
                print("------------")
                myResult = calculate(operands[i])
                if(not myResult.__contains__("Error") and not myResult.__contains__("kaBOOM")):
                    print(f"My results: {myResult}")
                    print(f"Results to compare: {compareResults[i]}")
                    response = compare(myResult, compareResults[i])
                else:
                    response = myResult
                print(response)
    else:
        return "kaboom"

main()
print("˜Game Over ˜")