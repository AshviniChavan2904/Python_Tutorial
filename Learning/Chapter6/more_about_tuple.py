days=('mon','tues','wed','thurs','fri','sat','sun')

for i in days:
    print(i)

# Tuple with element
# days=('mon')  Consider this as an string by default in Python to make the data type to tuple we use , after the element
days=('mon',)
print(type(days))

# Tuple without parenthesis
days='mon','tues','wed','thurs','fri','sat','sun'
print(type(days))

# Tuple unpacking
students_data=('Ashvini','Pooja','Pradnya')
stud1,stud2,stud3=students_data
print(stud3)

# List inside tuple
favorites=('southern mangolia',['Tokyo Ghoul Theme','landscape'])
favorites[1].pop()
favorites[1].append('Ashvini')
print(favorites)

# Functions with tuples
mixed=(1,2,4,3.0,3.8,4.9)
print(min(mixed))
print(max(mixed))
print(sum(mixed))