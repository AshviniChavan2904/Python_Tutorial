# Define a function inside functionn to find greatest between 3 numbers
num1,num2,num3=input("Enter three numbers seperated by space: ").split()
a,b,c=int(num1),int(num2),int(num3)
def greater(a,b):
    if a > b:
        return a
    return b

#Way 1
def greatest(a,b,c):
    bigger = greater(a,b)
    return (bigger,c)

#Way 2
def greatest(a,b,c):
    return greater(greater(a,b),c)

print(f"The number greatest between {a}, {b} and {c} is: {greatest(a,b,c)}")