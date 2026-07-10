import random
print("Welcome to the hardest game in the world")
computer_choice = random.randint(1,10)
user_choice = int(input("Enter a number betwen (1 and 10): "))
lives = 3
if user_choice >=1 and user_choice <=10:
    while user_choice != computer_choice and lives > 0:
        if user_choice < computer_choice:
            print("higher")
        else:
            print("lower")
        print(f"you have {lives} more tries")
        user_choice = int(input("Enter a number betwen (1 and 10): "))
        lives -= 1
    if lives == 0 and user_choice != computer_choice:
        print(f"Sorry you lose! the computer chose was {computer_choice}")
    else:
        print(f"Congraulition you won!\nthe computer chose was {computer_choice}")
else:
    print("Invaild choice..... \nplease Enter a number betwen (1 and 10) ")
