inputList = input()
l = [int(v) for v in inputList.split(" ")]
result = 0
minimum = l[0]
maximum = l[0]

def findAverage(l):
    global result
    global minimum
    global maximum
    result += l[0]
    minimum = min(minimum, l[0])
    maximum = max(maximum,l[0])
    if(len(l) > 1):
        return findAverage(l[1:])
    return (result/10), maximum, minimum

print(findAverage(l))