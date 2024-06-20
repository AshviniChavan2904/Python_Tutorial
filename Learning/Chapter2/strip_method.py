#In last exercise we saw that if we enter a character with space like this " h"
#It looks for a space followed by h and hence provides count as 0
#To solve this issue we have strip method
name="     Ashvini     "
dots="................." #Added this to see the space of right side
#lstrip(): to remove left side space
#rstrip(): to remove right side space
#strip(): removes both left and right side space
print(name+dots)
print(name.lstrip()+dots)
print(name.rstrip()+dots)
print(name.strip()+dots)
#Now consider scenario where your string contains space like "Ash       vini"
#To resolve this issue we use replace("what to replace","what to replace with") method
name="Ash       vini"
print(name)
print(name.replace(" ",""))

# exercise 3 revise with strip method
# Input: AshvinI,i
# user_name,single_char=input("Enter your name & the character to count from the provided name seperated bycomma: ").split(",")
# #Strip solution: Input AshvinI, i
# print(f"Length of {user_name} is: {len(user_name)}.\nThe occurance of {single_char} in {user_name} count is: {(user_name.lower()).count((single_char.strip()).lower())}")