import sys

# Problem1: Basketball Score Calculator
# The first argument is program name "Quiz2.py" so i started with 1 to get inputs
try:
    countOf2Point = int(sys.argv[1])
    countOf3Points = int(sys.argv[2])
    countOfFT = int(sys.argv[3])
    score = (countOf2Point*2)+(countOf3Points*3)+countOfFT  # calculate score
    print(score)
except:
    score = -1  # set score -1 for wrong inputs
    pass


# Problem2: Body Mass Index Calculator
def healthStatus(height, mass):
    bmi = mass / (height ** 2)
    if(bmi > 30):
        return "obese"
    elif bmi > 24.9:
        return "overweight"
    elif bmi > 18.5:
        return "healthy"
    else:
        return "underweight"


''' 
Yusuf İpek
2220356048
'''
