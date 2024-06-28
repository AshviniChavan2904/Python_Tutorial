# If we do not pass any parameters during runtime we will encounter an error
# To resolve this we pass some default arguments but we can pass it for the last aru only
# If you are passing any default value in between then you also need to pass the default parameter value for subsequent else you will face an error

def print_details(first_name="Unknown",last_name='Unknown',age=None):
    print(f"Your first name is: {first_name}\nYour last name is: {last_name}\nYour age is: {age}")

print_details("Ashvini","Chavan",26) #def print_details(first_name,last_name,age): Runs successfully
print_details("Ashvini","Chavan")    #def print_details(first_name,last_name,age): Throws an error missing arg
print_details("Ashvini","Chavan")    #def print_details(first_name,last_name,age=None): Will run program with default age value
print_details("Ashvini",23)          #def print_details(first_name,last_name='Unknown',age): Throws an error stating parameter without default follows parameter with default. To resolve this pass a default value to age also
print_details("Ashvini")             #def print_details(first_name,last_name='Unknown',age=None): Throws an error stating parameter without default follows parameter with default
print_details("Rahul","Dravid",50)   #def print_details(first_name,last_name='Unknown',age=None): Overrides the value, runs successfully
print_details()                      #def print_details(first_name="Unknown",last_name='Unknown',age=None): Runs successfully
