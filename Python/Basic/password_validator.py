password = input("Enter Your Psassword: ")
if(len(password)<8):
    print("Passwprd is too short")
elif not any(char.isdigit() for char in password):
    print("Password should have atleast one digit: ")
elif not any(char.isupper() for char in password):
    print("password sholud have atleast one uppercase letter")
elif not any(char.islower() for char in password):
    print("password sholud have atleast one lowercase letter")
else: 
    print("Password is valid")
