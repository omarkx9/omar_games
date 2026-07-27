import random
def win(user,computer):
    print(f"\n🔥 Awesome! You beat the computer!\n you chose:\n{user}\ncomputer chose:\n{computer}")
def again(user):
    return bool(user)
def point(wins,lose,tie):
    print(f"Your namber of win Is ({wins})")
    print(f"Your namber of lose Is ({lose})")
    print(f"Your namber of tie Is ({tie})")
choices = ["rock","paper","scissors"]
Number_of_Wins = 0
Number_of_Lose = 0
Number_of_Tie = 0
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
while True:
    computer_choice = random.choice(choices)
    if computer_choice == "rock":
        result = rock
    elif computer_choice == "paper":
        result = paper
    else:
        result = scissors
    user_chose = input("Please 🎮 Choose your move ( Rock🪨 , Paper📄, Scissors ✂️ ): ").lower().strip()
    if user_chose in choices:
        if user_chose == "rock":
            option = rock
        elif user_chose == "paper":
            option = paper 
        else:
            option = scissors
        if user_chose == computer_choice:
            Number_of_Tie +=1
            print(f"\nIts a tie! you chose:\n{option}\ncomputer chose:\n{result}")
            point(Number_of_Wins,Number_of_Lose,Number_of_Tie)
            if again(user = input("Enter Do You Want To Play Again (Yes Or Press Enter)?: ").strip().lower()):
                continue
            else:
                print("Good bye")
                break
        elif user_chose != computer_choice:
            if user_chose == "rock" and computer_choice == "scissors":
                Number_of_Wins += 1
                win(option,result)
                point(Number_of_Wins,Number_of_Lose,Number_of_Tie)
                if again(user = input("Enter Do You Want To Play Again (Yes Or Press Enter)?: ").strip().lower()):
                    continue
                else:
                    print("Good bye")
                    break
            elif user_chose == "paper" and computer_choice == "rock":
                Number_of_Wins += 1
                win(option,result)
                point(Number_of_Wins,Number_of_Lose,Number_of_Tie)
                if again(user = input("Enter Do You Want To Play Again (Yes Or Press Enter)?: ").strip().lower()):
                    continue
                else:
                    print("Good bye")
                    break
            elif user_chose == "scissors" and computer_choice == "paper":
                Number_of_Wins += 1
                win(option,result)
                point(Number_of_Wins,Number_of_Lose,Number_of_Tie)
                if again(user = input("Enter Do You Want To Play Again (Yes Or Press Enter)?: ").strip().lower()):
                    continue
                else:
                    print("Good bye")
                    break
            else:
                Number_of_Lose +=1
                print(f"\nOhhh. 😅 You lost this round. \nyou chose:\n{option}\ncomputer chose:\n{result}")
                point(Number_of_Wins,Number_of_Lose,Number_of_Tie)
                if again(user = input("Enter Do You Want To Play Again (Yes Or Press Enter)?: ").strip().lower()):
                    continue
                else:
                    print("Good bye")
                    break
    else:
        print(f"\n(Obss.Invaild choice....... ({user_chose}) is not the Right word. Try again.)\n")
        continue