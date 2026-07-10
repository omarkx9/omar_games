import random
def win(user_option,computer_result):
    print(f"🔥 Awesome! You beat the computer!\n you chose:\n{option}\ncomputer chose:\n{result}")
choices = ["rock","paper","scissors"]
Number_of_Wins = 0
rock = """ 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
computer_choice = random.choice(choices)
if computer_choice == "rock":
    result = rock
elif computer_choice == "paper":
    result = paper
else:
    result = scissors
user_choice = input("Please 🎮 Choose your move (Rock, Paper, or Scissors): ").lower()
if user_choice in choices:
    if user_choice == "rock":
        option = rock
    elif user_choice == "paper":
        option = paper 
    else:
        option = scissors
    if user_choice == computer_choice:
        print(f"\nIts a tie! you chose:\n{option}\ncomputer chose:\n{result}")
    elif user_choice != computer_choice:
        if user_choice == "rock" and computer_choice == "scissors":
            win(user_option = option , computer_result = result)
        elif user_choice == "paper" and computer_choice == "rock":
            win(user_option = option , computer_result = result)
        elif user_choice == "scissors" and computer_choice == "paper":
            win(user_option = option , computer_result = result)
        else:
            print(f"\n😅 You lost this round. Try again!\nyou chose:\n{option}\ncomputer chose:\n{result}")
else:
    print(f"{user_choice} is Invaild choice\nPlease Choose your move (Rock, Paper, or Scissors):")
# testt