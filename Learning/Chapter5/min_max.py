# Min and Max function

numbers=list(range(1,11))

print(min(numbers))
print(max(numbers))

#Define a function which will return difference of greater number and lower number from the list

numbers=[90,99,100]

def greater_num(list):
    return max(list)-min(list)

print(greater_num(numbers))