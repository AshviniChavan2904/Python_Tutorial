# Understand the scope of variable in function
# Scenario 1: name 'x' is not defined
def func1():
    x=5             #Local variable
    return x

def func2():
    print(x)

func2()

# Scenario 2: name 'x' is not defined
def func1():
    x=5
    return x

print(x)

# Scenario 3: Will print output as 5 10
x=10                #Global variable
def func1():
    x=5
    return x

print(func1())
print(x)

# Scenario 4: To use a global variable in function. Normally we don't do like that as it becomes difficult to maintain the variable 
x=10                #Global variable
def func1():
    global x
    x=5
    return x

print(func1())
print(x)

# Scenario 5: Here we will get output as 10 5 because the value of variable will change when we will call a function
x=10                #Global variable
def func1():
    global x
    x=5
    return x

print(x)            
print(func1())
print(x)


