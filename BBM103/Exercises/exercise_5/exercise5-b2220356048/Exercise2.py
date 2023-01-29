givenList = list(map(int, input("List: ").replace(
    "[", "").replace("]", "").split(", ")))
n = int(input("N: "))


def findTheElement(n, l):
    print("My list:", l)
    l.sort()
    print("My sorted list:", l)
    l = l[-n:]
    print("Last n="+str(n)+" element of list:", l)
    l = l[:1]
    print("Take the nth element of list:", l)
    l = l[0]
    print("Make it to a single element:", l)


def findTheElementByDic(n):
    givenList.sort()
    givenList.reverse()  # we are looking for last elements
    dic = {i: givenList[i] for i in range(len(givenList))}
    return dic[n]


findTheElement(n, givenList)  # find element by using list
print(findTheElement(n))  # find element by using dictionary and list
