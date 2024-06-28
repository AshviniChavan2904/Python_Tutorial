#Solution

numbers=list(range(1,11))

def odd_even(mylist):
    even_list=[]
    odd_list=[]
    for i in mylist:
        if i%2 == 0:
            even_list.append(i)
        if i%2 != 0:
            odd_list.append(i)
    odd_even_list=[even_list,odd_list]
    return odd_even_list

print(odd_even(numbers))