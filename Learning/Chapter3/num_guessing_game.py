import random
win_num=random.randint(1,100)
game_over=False
guess_count=1
user_num=int(input("Guess a correct number between 1 to 100: "))
while not game_over:
    if user_num == win_num:
        print(f"You Win, You guess the number in {guess_count} times!")
        game_over=True
    else:
        if user_num < win_num:
            print("Too low!")
            guess_count+=1
            user_num=int(input("Guess again: "))
        else:
            print("To high!")
            guess_count+=1
            user_num=int(input("Guess again: "))
