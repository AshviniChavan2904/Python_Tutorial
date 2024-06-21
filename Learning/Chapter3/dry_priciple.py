import random
win_num=random.randint(1,100)
game_over=False
guess_count=1

while not game_over:
    user_num=int(input("Guess a correct number between 1 to 100: "))
    if user_num == win_num:
        print(f"You Win, You guess the number in {guess_count} times!")
        break
    else:
        if user_num < win_num:
            print("Too low!")
        else:
            print("To high!")
        guess_count+=1
        continue