# Write logic to reverse a string
# Define one variable which will store the result of reverse string
my_string=input("Enter a string to check if it's palindrome or not: ").lower()

def is_palindrome(my_string):
    if my_string == my_string[::-1]:
        return True
    return False

# Below code also does the same in short
# def is_palindrome(my_string):
#     return my_string == my_string[::-1]

print(f"Original string after converting it into lowercase: {my_string}\nReverse string: {my_string[::-1]}\nIs Palindrome result: {is_palindrome(my_string)}")