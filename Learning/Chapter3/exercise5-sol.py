#Ashvini Chavan
#user_name[0]=A,user_name[1]=s,---,user_name[13]=n
#temp_var=""
#temp_var=temp_var+user_name[0]=A
#temp_var=temp_var+user_name[1]=As
#temp_var=temp_var+user_name[2]=Ash
#temp_var=temp_var+user_name[3]=Ashv
#temp_var=temp_var+user_name[4]=Ashvi
#temp_var=temp_var+user_name[5]=Ashvin
#temp_var=temp_var+user_name[6]=Ashvin    
# If if condition, we use not in keyword to check if the character exists in string or not. If it's present it will not add that in the string
user_name=input("Enter your full name: ").lower()
temp_var=""
i=0
while i < len(user_name):
    if user_name[i] not in temp_var: #If the character is not present in temp_var then add it in temp_var and print it's count
        temp_var=temp_var+user_name[i]
        print(f"{user_name[i]}: {user_name.count(user_name[i])}")
    i=i+1