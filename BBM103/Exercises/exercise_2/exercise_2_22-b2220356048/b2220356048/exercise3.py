b = int(input("b: "))
c = int(input("c: "))
# x2 + bx + c roots
delta = b * b - 4 * c
root1 = ((-1 * b) + (delta ** 0.5)) / 2
root2 = ((-1 * b) - (delta ** 0.5)) / 2
print(root1, root2)
