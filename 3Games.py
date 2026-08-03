import random
import os
import time

def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()

def Continue():

    input("💫.......Press Enter To Continue......💫: ")

twenty_one = """
                   {♣️♦️--------Welcome To Twenty One--------♥️♠️}

        /ʅ
      .'   `.
     '       `.
  .'           `.
 {              }
  ~-...-||-...-~   
        ||
       '__`
     
 _________          ________ _    _ _________     __         ____   _   _   ______    
|__   __\ \        / /  ____| \  | |__   __\ \   / /        / __ \ | \ | | |  ____|
   | |   \ \  /\  / /| |___ |  \ | |  | |   \ \_/ /        | |  | ||  \| | |  |__ 
   | |    \ \/  \/ / |  __| |  . ` |  | |    \   /         | |  | ||  \| | |  ___|      
   | |     \  /\  /  | |____| | \  |  | |     | |          | |__| || |\  | | |____
   |_|      \/  \/   |______|_|  \_|  |_|     |_|           \____/ |_| \_| |______|  
       
"""

name = input("📛 Before Start What is your name 📛?: ").strip().capitalize()

def deal_cards():
    """ترجع بطاقه عشوائيه من البطاقات"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)



def caclute_score(cards):
    """ان كان هناك بلاك جاك تقوم بارجاع صفر وايضا تقوم بتدعديل رقم 11 اذا كان مجموع الارقام اكثر من 21"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    else:
        if 11 in cards and sum(cards) > 21:
            for x in cards:
                if x == 11:
                    cards[cards.index(x)] = 1
    return sum(cards)


def compare(user_cards,computer_cards,name):
    total_user = caclute_score(user_cards)
    total_computer = caclute_score(computer_cards)
    results = {
        "draw" : f"👍Its a tie💥 Good luck {name} next time💥",
        "win" : f"🎉👏👏🎉Congratulations!! {name} You Win👑🥇🏆🌟😎!!!!!!",
        "lose" : f"😔Sorry🙏 '{name}' You Lose!!😞 Good luck next time 😕",
        "black jack win" : f"🎉Wow {name}👏👏🎉Congratulations!!!!!!!!BLACK JACK!!!!!!!!You Win👑🥇🏆🌟😎!!!!!!",
        "black jack lose" : f"😔Sorry🙏 '{name}' You Lose!!😞 Computer Get The !!!BLACK JACK!!! Good luck next time 😕",
        "went 21 win" : f"🎉👏👏🎉Congratulations!! {name} You Win👑🥇 Computer went 21 🏆🌟😎!!!!!!",
        "went 21 lose" : f"😔Sorry🙏 '{name}' You Lose!!😞 You went 21 Good luck next time 😕",
    }
    if total_computer == total_user:
        return results["draw"]
    elif total_user == 0 :
        return results["black jack win"]
    elif total_computer == 0:
        return results["black jack lose"]
    elif total_user == 21:
        return results["win"]
    elif total_computer == 21:
        return results["lose"]
    elif total_user > 21:
        return results["went 21 lose"]
    elif total_computer > 21:
        return results["went 21 win"]
    elif total_user > total_computer:
        return results["win"]
    else:
        return results["lose"]
    

def Game21():
    clear()
    print("🎮Starting game🎮...............🎮")
    time.sleep(3)
    clear()
    print(twenty_one)
    Continue()
    clear()

    user_cards = [deal_cards() for _ in range(2)]
    computer_cards = [deal_cards() for _ in range(2)]
    game_con = True
    
    while game_con:
        clear()
        user_score = caclute_score(user_cards)
        computer_score = caclute_score(computer_cards)
        print(f"🫵 Your cards are {user_cards}, current score is ♠️ {sum(user_cards)}")
        print(f"🤖 Computer's first card is ♠️ [{computer_cards[0]}] ")
        if user_score == 0 or computer_score == 0 or user_score >= 21 or computer_score >= 21:
            game_con = False
        else:
            another_card = input("Get another card? (Y/N): ").strip().lower()
            if another_card == "y":
               user_cards.append(deal_cards())
            else:
                game_con = False
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = caclute_score(computer_cards)
    input("♠️.......Press Enter To See The Result......💫 ")
    clear()
    print(f"🃏 🫵 Your final hand: {user_cards} with score📊 {sum(user_cards)}")
    print(f"🖥️ Computer's final hand: {computer_cards} with score📊 {sum(computer_cards)}")

    print(compare(user_cards,computer_cards,name))

    Continue()

    clear()
    play_again = input("🔄️ Do You Want To Play Again? ✅(Y/N): ").strip().lower()
    if play_again == "y":
        Game21()
    else:
        print(f"🥹🥹 Oh No Now I Have To say Goodbye To Youe Mr.{name} 👋👋👋😢")



while True:
    clear()
    print(f"👋All Right {name} Choose🤏 a game to start.....")
    print("1- Froggy")
    print("2- Twenty one")
    print("3- Snake")
    print("--------------")
    print()
    game = input("🎮Chose a Game🎮: ").strip().lower()
    print()
    if game == "twenty one" or game == "21":
        Game21()
        print()
        chose_another_game = input("🔄️ Do You Want to chose🤏 another game🎮 (Y/N)? : ").strip().lower()
        if chose_another_game == "y":
            continue
        else:
            print("❌❌❌❌❌❌❌❌❌❌❌❌")
            print("❌❌❌❌❌❌❌❌❌❌❌❌")
            print("❌❌❌❌❌❌❌❌❌❌❌❌")
            print("❌❌❌❌❌❌❌❌❌❌❌❌")
            print("❌❌❌❌❌❌❌❌❌❌❌❌")
            break
    else:
        print("Coming son....")
        Continue()