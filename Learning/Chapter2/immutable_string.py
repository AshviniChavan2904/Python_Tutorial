#Strings are immutable in Python means you can't change the characters in a string once defined
name="Sona"
print(name[0])
#If I do below changes it will throw error as we can't change the characters in string
# name[0]="M"
# print(name)
#To change the characters we can use replace. It does not change the string it creates new one
new_name=name.replace("S","M")
print(f"Previous name: {name}\nNew name: {new_name}")