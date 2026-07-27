import random

def win(user, computer):
    print(f"\n🏆🔥 Awesome! You beat the computer! 🎉🎊\n\n🫵 You chose:\n{user}\n\n🤖 Computer chose:\n{computer}")

def again(user):
    return bool(user)

def point(wins, lose, tie):
    print(f"\n📊 Scoreboard 📊")
    print(f"🏆 Your number of wins: ({wins})")
    print(f"❌ Your number of losses: ({lose})")
    print(f"🤝 Your number of ties: ({tie})")

choices = ["rock", "paper", "scissors"]

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

    user_chose = input("🎮 Please choose your move (🪨 Rock, 📄 Paper, ✂️ Scissors): ").lower().strip()

    if user_chose in choices:

        if user_chose == "rock":
            option = rock
        elif user_chose == "paper":
            option = paper
        else:
            option = scissors

        if user_chose == computer_choice:
            Number_of_Tie += 1
            print(f"\n🤝 It's a tie! 😄\n\n🫵  You chose:\n{option}\n\n🤖 Computer chose:\n{result}")
            point(Number_of_Wins, Number_of_Lose, Number_of_Tie)

            if again(user=input("🔄 Do you want to play again? (Type anything or press Enter to quit): ").strip().lower()):
                continue
            else:
                print("👋 Goodbye! Thanks for playing! 🎮")
                break

        elif user_chose != computer_choice:

            if user_chose == "rock" and computer_choice == "scissors":
                Number_of_Wins += 1
                win(option, result)
                point(Number_of_Wins, Number_of_Lose, Number_of_Tie)

                if again(user=input("🔄 Do you want to play again? (Type anything or press Enter to quit): ").strip().lower()):
                    continue
                else:
                    print("👋 Goodbye! Thanks for playing! 🎮")
                    break

            elif user_chose == "paper" and computer_choice == "rock":
                Number_of_Wins += 1
                win(option, result)
                point(Number_of_Wins, Number_of_Lose, Number_of_Tie)

                if again(user=input("🔄 Do you want to play again? (Type anything or press Enter to quit): ").strip().lower()):
                    continue
                else:
                    print("👋 Goodbye! Thanks for playing! 🎮")
                    break

            elif user_chose == "scissors" and computer_choice == "paper":
                Number_of_Wins += 1
                win(option, result)
                point(Number_of_Wins, Number_of_Lose, Number_of_Tie)

                if again(user=input("🔄 Do you want to play again? (Type anything or press Enter to quit): ").strip().lower()):
                    continue
                else:
                    print("👋 Goodbye! Thanks for playing! 🎮")
                    break

            else:
                Number_of_Lose += 1
                print(f"\n😢💥 Oh no! You lost this round.\n\n🫵 You chose:\n{option}\n\n🤖 Computer chose:\n{result}")
                point(Number_of_Wins, Number_of_Lose, Number_of_Tie)

                if again(user=input("🔄 Do you want to play again? (Type anything or press Enter to quit): ").strip().lower()):
                    continue
                else:
                    print("👋 Goodbye! Thanks for playing! 🎮")
                    break

    else:
        print(f"\n🚫 Oops! Invalid choice. ❌\n📝 '{user_chose}' is not a valid option.\n🎮 Please try again! 😊\n")
        continue