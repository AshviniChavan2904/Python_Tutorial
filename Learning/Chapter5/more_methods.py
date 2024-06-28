# To insert the item in list at any position as per our convinience
fruits = ["mango","banana","grapes"]
for i in range(len(fruits)):
    print(f"Position of {fruits[i]}: {i}")

print("\nAfter inserting new item orange at index 1\n")
fruits.insert(1,"orange")
for i in range(len(fruits)):
    print(f"Position of {fruits[i]}: {i}")

print("\nConcatenate two lists\n")  
fruit1=["grapes","banana","apple"]
fruit2=["orange","pipeapple","apple"]
print(fruit1+fruit2)

#Different between append and extend is that append adds list inside list and extend adds item in other list
print("\nTo add items of fruit2 into fruit1\n")  
fruit1=["grapes","banana","apple"]
fruit2=["orange","pipeapple","apple"]
fruit1.extend(fruit2)
print(fruit1)
print(fruit2)