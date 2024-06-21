#We use in keyword to check for a presence of character in a string
user_name=input("Enter your name: ")
if 'a' in user_name.lower():
    print(f"a is present in {user_name}")
else:
    print(f"a is not present in {user_name}")