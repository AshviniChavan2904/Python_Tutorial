# Delete data from list: pop
# By default pop deletes item at last index
# You can also pass index number to delete element at particular index
 
fruits=["apple","banana","mango","orange","jackfruit"]
print(f"before popping item from list: {fruits}")
print(f"Popped item is: {fruits.pop()}")
print(f"after popping item from list: {fruits}")
print("\Before deleting all items from list\n")
fruits=["apple","banana","mango","orange","jackfruit"]
for i in range(len(fruits)):
    print(f"Item at index {i} is: {fruits[i]}")

print("\nAfter deleting all items from list\n")
for i in range(len(fruits)):
    print(f"Popped item: {fruits.pop()}")
print(fruits)

# del operator
fruits=["apple","banana","mango","orange","jackfruit"]
del fruits[1]
print(fruits)

# When you don't know the index of particular element in list but wanted to delete then we can use remove method
fruits=["apple","banana","mango","orange","jackfruit"]
fruits.remove("orange")
print(fruits)