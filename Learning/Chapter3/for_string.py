# #Normal way
# name="Ashvini"
# print("Normal way")
# for i in range(len(name)):
#     print(name[i])

# #Python way
# print("Python way")
# for i in name:
#     print(i)

#Sum of digit example
total=0
user_num=input("Enter any number: ")
for i in user_num:
    total+=int(i)
print(f"Sum of digits: {total}")