year = int(input("Year: "))
result = ""
if ((year % 4) == 0) & ((year % 100) != 0) | ((year % 400) == 0):
    result = " is a leap year."
else:
    result = " is not a leap year."
print(year, result)
