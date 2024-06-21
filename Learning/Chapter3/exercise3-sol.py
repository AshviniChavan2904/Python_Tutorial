user_num=int(input("Enter any natural number:"))
i,total=1,0
while i<=user_num:
    total+=i
    i+=1
print(f"Total of numbers from 1 to {user_num} is: {total}")