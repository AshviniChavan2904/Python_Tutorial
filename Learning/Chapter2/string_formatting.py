#Here we will learn how to use string formatting
name="Ashvini"
age=26
#Before
print("Hello, "+name+". Your age is "+str(age))
#New way
print("Hello, {}. Your age is {}".format(name,age)) #Python3
print(f"Hello, {name}. Your age is {age}")          #Python3.6