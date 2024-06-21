user_name=input("Enter you username: ").lower()
temp_var=""
for i in range(0,len(user_name)):
    if user_name[i] not in temp_var:
        temp_var=temp_var+user_name[i]
        print(f"{user_name[i]}: {user_name.count(user_name[i])}")