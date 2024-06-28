# Solution

mylist=["abc","xyz","pqr"]

def rev_list(mylist):
    new_list=[]
    for i in mylist:
        new_list.append(i[::-1])
    return new_list

print(rev_list(mylist))