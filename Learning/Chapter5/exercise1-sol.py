# Define a function to find square of numbers in list
numbers=list(range(1,11))

def square_num(list):
    sq_num=[]
    for i in list:
        sq_num.append(i**2)
    return sq_num  

print(numbers)
print(square_num(numbers))