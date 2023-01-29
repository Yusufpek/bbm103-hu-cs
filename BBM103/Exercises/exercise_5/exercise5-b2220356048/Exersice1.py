n = int(input("Enter the number N value: "))
dic = {i: list(i*"*") for i in range(1,n+1)}
print(dic)