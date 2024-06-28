# Create a function to find out a number greater between 3 numbers
num1,num2,num3=input("Enter three numbers seperated by space: ").split()
a,b,c=int(num1),int(num2),int(num3)
def gretest_fun(a,b,c):
    if (a > b) and (a > c):
        return a
    elif (b > a) and (b > c):
        return b
    return c
print(f"The greatest number between {a}, {b} & {c} is: {gretest_fun(a,b,c)}")