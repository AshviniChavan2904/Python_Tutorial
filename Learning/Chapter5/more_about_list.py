# Generate list with range function
numbers=list(range(1,11))
print(numbers)

# More about pop method: It returns the pop value
pop_item=numbers.pop()
print(numbers)
print(pop_item)

# index method
fruits=["apple","banana","kiwi","papaya","jackfruit","grapes","papaya"]
print(fruits.index("papaya"))
print(fruits.index("papaya",4))
print(fruits.index("papaya",4,7))

# pass list to a function
numbers=[1,2,3,4,5,6,7,8,9,10]
def neg_list(list):
    neg=[]
    for i in list:
        neg.append(-i)
    return neg
print(neg_list(numbers))