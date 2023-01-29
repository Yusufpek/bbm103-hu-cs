# get a number and convert to it binary form
number = int(input("Number: "))
power = 0
result = "0"
while number > 0:
    while (2**power) <= number:
        power += 1
    power -= 1
    number -= 2 ** power
    _result = "1" + "0" * (power)
    result = str(int(_result) + int(result))
    power = 0
print(result)
