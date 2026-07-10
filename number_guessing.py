import random
print("🎲Welcome to th Number Guessing Game!")
tries = 6
computer_guess = random.randint(1,10)
user_guess = int(input("Guess a number betwen (1 and 10): "))
if user_guess > 0 and user_guess < 11:
    while user_guess != computer_guess and tries != 0:
        tries -= 1
        print(f"You have {tries} more tries")
        if user_guess > computer_guess:
            print("⬇️ Too high! Try again.⬇️")
        else:
            print("⬆️ Too low! Try again.⬆️")
        user_guess = int(input("Guess a number betwen (1 and 10): "))
    if user_guess == computer_guess:
        print(f"\n💯 Correct! You guessed the number in {tries} tries")
    else:
        print(f"Sorry you lose! You tries {tries} times...........")
else:
    print("Invalid Choice...... Plese Enter a number betwen(1 and 10)")