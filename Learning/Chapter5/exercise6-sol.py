# Solution

mylist=[1,2,3,4,[1,2,3],["a","b","c"],[3,4,5]]

def find_list(mylist):
    count = 0
    for i in mylist:
        if type(i) == list:
            count+=1
    return count

print(find_list(mylist))