import sys

#sys.argv = [program name, "number1,number2,..."]
numbers = sys.argv[1].split(",")

index = 1 # first number is 1 so take the next number
while(index < len(numbers)):
    number = int(numbers[index])
    innerIndex = number - 1 # -1 is for index
    while (innerIndex < len(numbers)):
        numbers.pop(innerIndex) # delete innerIndex^th number
        innerIndex += number - 1
    if(numbers[index] == str(number)): 
        index+= 1 #if the number is not removed at this index: increase the index

output = ""
for item in numbers:
    output += item + " "

print(output.strip()) #for last blanket