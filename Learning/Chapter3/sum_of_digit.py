user_num=input("Enter any number: ")
total=0
for i in range(0,len(user_num)):
    total+=int(user_num[i])
print(f"Sum of {user_num} digit's is: {total}")