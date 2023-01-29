def isValidEmail(email):
    return(email.__contains__("@") and email.__contains__("."))


email = input("Enter your e-mail addres: ")
if(isValidEmail(email)):
    print("This is a valid e-mail address")
else:
    print("This is NOT a valid e-mail address")
