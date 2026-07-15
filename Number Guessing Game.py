import random
print("🎲-------Welcome to Guessing Game-------🎲")
computer_number = random.randint(1,10)
attempets = 0
tries = 5
while True:
    if tries != 0:
            attempets += 1
            print(f"you have {tries} more tries")
            user_number = int(input("Enter a number betwen (1 and 10): "))
            if user_number < 11 and user_number > 0:
                if user_number == computer_number:
                    print(f"💯Congratulations you won!\nYou guess the number in {attempets} treis\n\tthe nubmer was ({computer_number})")
                    break
                elif user_number > computer_number:
                    print("⬇️  Too high! Try again ⬇️")
                elif user_number < computer_number:
                    print("⬆️  Too low! Try again ⬆️")
                tries -= 1
            else:
                print("Invaild choice..... Try again ")
                continue
    else:
        print(f"Sorry you lose! the computer chose was {computer_number}")
        break