#We can use if elif else statement where we want to check for multiple conditions
#You can take example of ticket price rates as per age to watch a movie
# 1 to 5 (free)
# 6 to 10 (150)
# 11 to 18 (200)
# 19 to 60 (250)
# above 60 (200)
my_string="movie ticket booking"
print(f"{(my_string.upper()).center(len(my_string)+10,"*")}")
age=int(input("Enter your age: "))
if age <=0:
    print("You cannot watch movie!")
elif  1<= age <=5:
    print("Ticket price: Free")
elif 6<= age <=10:
    print("Ticket price: 150")
elif 11<= age <=18:
    print("Ticket price: 200")
elif 19<= age <=60:
    print("Ticket price: 250")
else: 
    print("Ticket price: 200")