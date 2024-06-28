# We used the already define function in python already like below
user_name="Ashvini"
print(f"Length of {user_name} is: {len(user_name)}")

# Function to define sum of 2 numbers
# We use def keyword in python to define function
# Syntax:
# def fun_name(arg1,arg2,..argn):
#     return arg
def add_two(a,b):
    return a+b
total=add_two(5,5)
print(f"The sum of two numer is: {total}")
print(f"The sum of two numer is: {add_two(5,9)}")

#Take the user input for addition
def add_two(num1,num2):
    return num1+num2
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(f"Sum of {a} and {b} is: {add_two(a,b)}")

#Take user input to concatenate string
first_name=input("Enter first name: ")
last_name=input("Enter last name: ")
def con_string(first_name,last_name):
    return first_name+" "+last_name
print(f"Your full name is: {con_string(first_name,last_name)}")