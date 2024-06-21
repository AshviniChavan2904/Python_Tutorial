#This is used to print any message if user didn't provide any input
user_name=input("Enter your name: ")
if user_name:
    print(f"Hello, {user_name}")
else: 
    print("You have not entered anything")