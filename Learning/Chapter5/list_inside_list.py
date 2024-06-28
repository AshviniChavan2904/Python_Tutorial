# List inside list
matrix=[[1,2,3],[4,5,6],[7,8,9]] # 2D list, there can be 3D list as well
print(matrix[0])

#To print items of matrix
print("Print sublist")
for sublist in matrix:
    print(sublist)
    for element in sublist:
        print(element)

# To print only particular element inside the list
matrix=[[1,2,3,[4,5,6]],[7,8,9,[10,11,12]],[13,14,15,[16,17,18]]]
print("Particular element in list")
print(matrix[0][3][2])

# To check the data type
print(type(matrix))
my_string="Ashvini"
print(type(my_string))

