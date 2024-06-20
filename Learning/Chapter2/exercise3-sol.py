# Input: AshvinI,i
user_name,single_char=input("Enter your name & the character to count from the provided name seperated bycomma: ").split(",")
print(f"Length of {user_name} is: {len(user_name)}.\nThe occurance of {single_char} in {user_name} count is: {(user_name.lower()).count(single_char)}")