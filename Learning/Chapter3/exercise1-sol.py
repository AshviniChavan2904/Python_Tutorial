import random
win_num=random.randint(1,100)
# print(win_num)
my_string="number guessing game"
print(f"{(my_string.upper()).center(len(my_string)+10,"*")}")
user_num=int(input("Guess a number between 1 to 100: "))
if user_num == win_num:
    print("You Win!")
#Below is called as nested if else
else:
    if user_num < win_num:
        print("You have entered a number lower than winning number")
    else:
        print("You have entered a number higher than winning number")   