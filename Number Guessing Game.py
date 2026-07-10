import random
print("🎲-------Welcome to Guessing Game-------🎲")
computer_number = random.randint(1,10)
tries = 0
attempts = 5
while True:
    if attempts != 0:
            tries += 1
            print(f"you have {attempts} more tries")
            user_number = int(input("Enter a number betwen (1 and 10): "))
            if user_number < 11 and user_number > 0:
                if user_number == computer_number:
                    print(f"💯Congratulations you won!\nYou guess the number in {tries} treis\n\tthe nubmer was ({computer_number})")
                    break
                elif user_number > computer_number:
                    print("⬇️  Too high! Try again ⬇️")
                elif user_number < computer_number:
                    print("⬆️  Too low! Try again ⬆️")
                attempts -= 1
            else:
                print("Invaild choice..... Try again ")
                continue
    else:
        print(f"Sorry you lose! the computer chose was {computer_number}")
        break