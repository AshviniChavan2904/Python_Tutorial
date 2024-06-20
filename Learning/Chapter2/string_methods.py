name="Ashvini"
#len() function: Also counts spaces
#Below are methoths. The difference between function and method is in method we use . to call method while in function we use ()
#lower() method: changes string to lowercase
#upper() method: changes string to uppercase
#title() method: changes first character to uppercase
#count() method: counts a particular characters occurance in a string
print(f"The length of {name} is: {len(name)}")
print(f"Lowercase of {name} is {name.lower()}")
print(f"Uppercase of {name} is {name.upper()}")
print(f"Title of {name} is {name.title()}")
print(f"Count occurance of {name[4:5]} is {name.count("i")}")