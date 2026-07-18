import random
def win(user_option,computer_result):
    print(f"\n🔥 Awesome! You beat the computer!\n you chose:\n{option}\ncomputer chose:\n{result}")
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
while True:
    user_chose = input("Please 🎮 Choose your move (Rock🪨 , Paper📄, Scissors ✂️ ): ").lower()
    if user_chose in choices:
        if user_chose == "rock":
            option = rock
        elif user_chose == "paper":
            option = paper 
        else:
            option = scissors
        if user_chose == computer_choice:
            print(f"\nIts a tie! you chose:\n{option}\ncomputer chose:\n{result}")
            break
        elif user_chose != computer_choice:
            if user_chose == "rock" and computer_choice == "scissors":
                win(user_option = option , computer_result = result)
                break
            elif user_chose == "paper" and computer_choice == "rock":
                win(user_option = option , computer_result = result)
                break
            elif user_chose == "scissors" and computer_choice == "paper":
                win(user_option = option , computer_result = result)
                break
            else:
                print(f"\nOhhh. 😅 You lost this round. Try again!\nyou chose:\n{option}\ncomputer chose:\n{result}")
                break
    else:
        print(f"\n(Obss.Invaild choice....... ({user_chose}) is not the Right word. Try again.)\n")
        continue