# Define a function to return reverse of list

#With reverse method
numbers=list(range(1,11))

def reverse_list(mylist):
    numbers.reverse()
    return mylist

print(reverse_list(numbers))

#With list slicing
numbers=list(range(1,11))

def reverse_list(mylist):
    return numbers[::-1]

print(reverse_list(numbers))

#With pop and append method
numbers=list(range(1,11))

def reverse_list(mylist):
    rev_list=[]
    for i in range(len(mylist)):
        pop_item=numbers.pop()  
        rev_list.append(pop_item)   
    return rev_list

print(reverse_list(numbers))
