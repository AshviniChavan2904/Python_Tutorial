# We use count method to print the occurance of particular element in list
fruits=["apple","banana","mango","orange","jackfruit"]
print(fruits.count("apple"))

# We use sort method to print the item in list in alphabetical order
numbers=[100,68,58,99,23]
numbers.sort()
print(numbers)

# We use sorted function when we don't want to our list but want the item in sorted order
numbers=[100,68,58,99,23]
print(sorted(numbers))
print(numbers)

# To clear the list we use clear method
numbers=[100,68,58,99,23]
numbers.clear()
print(numbers)

# Make make copy of your list
numbers=[100,68,58,99,23]
number2=numbers.copy()
print(numbers)
print(number2)