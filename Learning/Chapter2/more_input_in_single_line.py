# Here we will learn to enter more than one input in a single line we will make use of split function
# split function requires a seperator either space or comma. By default it consider space
# If you want to provide comma you can add it in split function
name,age=input("Enter your name & age seperated by space:").split()
print("Hello, "+name+" Your age is: "+str(age))
name,age=input("Enter your name & age seperated by comma:").split(",")
print("Hello, "+name+" Your age is: "+str(age))