# Solution

list1=[1,2,3,4,5]
list2=[1,2,5,6,7]

def common_element(list1,list2):
    output_list=[]
    for i in list1:
        if i in list2:
            output_list.append(i)
    return output_list

print(common_element(list1,list2))