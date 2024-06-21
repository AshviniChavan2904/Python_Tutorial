user_num=input("Enter a number more than 1 digit and calculate it's sum: ")
total,i=0,0                 #As indexing starts from 0 123 012
while i< len(user_num):
    total+=int(user_num[i])
    i+=1
print(f"Sum of {user_num} is: {total}")