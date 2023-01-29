#Problem1: Sum of digits of x raised to n

import sys 

#sys.argv = [program name, base, power]
base = int(sys.argv[1])
power = int(sys.argv[2])

output = ""
output += str(base) + "^" + str(power) + " = "
number = str(base ** power) # change the number's type to string for taking digits
output += number
sumOfNumberDigits = 0

while(len(number) > 1):
    sumOfNumberDigits = 0
    output += " = "
    for i in range(len(number)):
        sumOfNumberDigits += int(number[i])
        if(i != len(number) -1 ):
            output += number[i]+" + "
        else:
            output += number[i] + " = "
    number = str(sumOfNumberDigits) # for addition's results digits
    output += number

print(output)