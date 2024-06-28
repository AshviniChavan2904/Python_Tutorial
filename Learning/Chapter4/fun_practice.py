# Print last character of name
name=input("Enter your name: ")
def last_char(name):
    return name[-1]
print(f"The last character of your name is: {last_char(name)}") 

# Print odd or even number
num=int(input("Enter any number: "))
def odd_even(num):
    if num%2 == 0:
        print(f"{num} is even!")
    else:
        print(f"{num} is odd!")
odd_even(num)

# Is even
num=int(input("Enter any number: "))
def is_even(num):
    return num%2==0
print(f"Is even: {is_even(num)}")

# Parameter is that we used while defining the function
# Argument is that we used while calling the function

# Print song
def song_fun():
    return "Happy Birthday!"
print(song_fun())