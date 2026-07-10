import random
print("🎲-------Welcome to Guessing Game-------🎲")
computer_choice = random.randint(1,10)
user_choice = int(input("Enter a number betwen (1 and 10): "))
lives = 6
while user_choice != computer_choice and lives > 0 and user_choice >=1 and user_choice <=10:
    lives -= 1
    print(f"you have {lives} more tries")
    if user_choice > computer_choice:
        print("⬇️ Too high! Try again ⬇️")
    else:
        print("⬆️ Too low! Try again ⬆️")
    user_choice = int(input("Enter a number betwen (1 and 10): "))
if lives == 0 and user_choice != computer_choice:
    print(f"Sorry you lose! the computer chose was {computer_choice}")
elif user_choice >10 or user_choice < 0:
    print("Invaild choice..... \nplease Enter a number betwen (1 and 10) ")
else:
    print(f"💯Congraulition you won!\nthe computer chose was {computer_choice}")