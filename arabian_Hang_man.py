import random
import os
def clear():
    os.system("cls" if os.name == 'nt' else "clear")
clear()

ascii_art = """

                                        ,%%%%%%%%,
                                      %%%%%o%%/%%%%%%
                                     %%%%%%%\%%%<%%%%%
                                    %%%%%%%>%%%/%%%%o%%
                                     %%%%%%%%o%%\%%//%
                                     '%%%\o%\%%/%o/%%'
                                        '%%\ `%/%%%'
                                         '%||%|%'
                                            | | (O
                                            | | |\\
                                            | | >>
                                            | |
                                           /   \\
                        -----------------------------------------------------

                             _                                             
                            | |                                            
                            | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
                            | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
                            | | | | (_| | | | | (_| | | | | | | (_| | | | |
                            |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                                __/ |                      
                                            |___/                       
"""
Hangmanpics = ['''
  +---+
      |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''']
arab_countries = [
    "egypt",
    "sudan",
    "libya",
    "tunisia",
    "algeria",
    "morocco",
    "saudi-arabia",
    "yemen",
    "oman",
    "qatar",
    "kuwait",
    "bahrain",
    "jordan",
    "lebanon",
    "syria",
    "iraq",
    "palestine",
    "somalia",
    "djibouti",
    "comoros",
    "mauritania",
    "uae"
]
print("\n                    😵--------Welcome to arabian Hangman Game--------😵")
print(ascii_art)
word = random.choice(arab_countries)
spaces = []
tries = len(Hangmanpics) 
used_letters = []
for x in word:
    spaces.append("_")
input("\n\n                           💫-----Press Enter To Start-----💫")
while "_" in spaces and tries > 0:
    clear()
    print(Hangmanpics[len(Hangmanpics)-tries])
    print(f"🔢 number of letters ({len(word)}) 🔢")
    print(f"🔄️ You have ({tries}) more tries 🔄️")
    print(f"({",".join(spaces)})")
    print("👾 If there is space in the conutry (space = \" - \") 🛰️")
    letter_guess = input("🤷 Enter a letter to guess or type (stop) to exit 🤷: ").lower()
    if letter_guess.lower() == "stop":
        break
    else:
        if len(letter_guess) == 1 and letter_guess.isalpha() or letter_guess == "-" :
            if letter_guess not in used_letters:
                if letter_guess in word:
                    for num in range(len(word)):
                        if letter_guess == word[num]:
                            spaces[num] = letter_guess
                else:
                    tries -= 1
                used_letters.append(letter_guess)
                
            else:
                clear()
                print (f"👀 You alreday use ({letter_guess}) 👀")
                input("💫-----Press Enter To Continue-----💫")  
        else:
            clear()
            print(f"🫥  Invalid Input......({letter_guess}) 🫥")
            input("💫-----Press Enter To Continue-----💫")   
            
if letter_guess == "stop":
    print(f"😕 Ok but the conutry was {word} 😕")
elif "_" in spaces:
    clear()
    
    print('''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''')
    print("""
         *********************
       (X﹏X)   YOU LOSE   (X﹏X)
         *********************
""")
    print(f"🤦 The word was ({word}) 😑\n")
else:
    clear()
    print("""
              *********************
           (❁´◡`❁) YOU WIN  (❁´◡`❁)
              *********************
    """)
    print(Hangmanpics[len(Hangmanpics)-tries])
    print(f"\n              🫡  The word was {word} 🫡\n")