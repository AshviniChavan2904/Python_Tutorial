user_name,age=input("Enter your name and age seperated by space: ").split()
if (user_name[0] == 'a' or user_name[0] == 'A') and int(age) >=10:
    print("You can watch COCO movie!")
else:
    print("You cannot watch COCO movie!")