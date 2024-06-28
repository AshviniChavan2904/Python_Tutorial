num1,num2=input("Enter two numbers: ").split(",")
print(f"{num1} {num2}")
def greater_num(num1,num2):
    if int(num1)>int(num2):
        return num1
    return num2
print(f"The number greater between {num1} and {num2} is: {greater_num(num1,num2)}")