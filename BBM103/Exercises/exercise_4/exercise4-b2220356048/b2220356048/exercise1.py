number = int(input("Write a number N: "))
sumOfOdds = 0
averageOfEvens = 0
countOfEvens = 0
if(number % 2 == 0):
    countOfEvens = number / 2
else:
    countOfEvens = (number - 1) / 2
for i in range(number+1):
    if(i % 2 == 0):
        averageOfEvens += i
    else:
        sumOfOdds += i
averageOfEvens /= countOfEvens
print("Sum of odds: " + str(sumOfOdds))
print("Average of evens: " + str(averageOfEvens))
