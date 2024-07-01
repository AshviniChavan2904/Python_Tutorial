# When you return two value in function by default it returns as a tuple
def func(num1,num2):
    add = num1 + num2
    multiply = num1 * num2
    return add, multiply

# print(func(2,3))
add, multiply = func(2,3)
print(add)
print(multiply)

