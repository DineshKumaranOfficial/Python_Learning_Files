userName = input("Enter the UserName : ")
password = input("Enter your Password : ")
passwordLength = len(password)
secretPassword = '*' * passwordLength
print(f"Hi {userName}, Your Password {secretPassword} is {passwordLength} letters long")
