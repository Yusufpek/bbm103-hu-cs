n = int(input("Disk Count: "))

def printMove(n, f, t):
    print("Move disk {} from source {} to destination {}".format(n,f,t))

def move(diskCount, _from, to, other):
    if(diskCount == 0): return
    move(diskCount-1, _from,other, to)
    printMove(diskCount, _from, to)
    move(diskCount-1, other, to, _from)

move(n, "A", "C", "B")
