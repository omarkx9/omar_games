import random
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
print("\n😵--------Welcome to arabian Hangman Game--------😵")
computer_choice = random.choice(arab_countries)
spaces = []
tries = len(Hangmanpics) 
used_letters = []
for x in computer_choice:
    spaces.append("_")

while "_" in spaces and tries > 0:
    print(Hangmanpics[len(Hangmanpics)-tries])
    print(f"🔢 number of letters ({len(computer_choice)}) 🔢")
    print(f"🔄️ You have ({tries}) more tries 🔄️")
    print(f"({",".join(spaces)})")
    print("👾 If there is space in the conutry (space = \" - \") 🛰️")
    letter_guess = input("🤷 Enter a letter to guess or type (stop) to exit 🤷: ").lower()
    if letter_guess.lower() == "stop":
        print("👋 Good bye 👋")
        break
    else:
        if len(letter_guess) == 1 and letter_guess.isalpha() or letter_guess == "-" :
            number = -1
            for i in computer_choice:
                number += 1
                if letter_guess == i:
                    spaces[number] = letter_guess
            if letter_guess not in computer_choice and letter_guess not in used_letters:
                tries -= 1
            else:
                if letter_guess in used_letters:
                    print (f"👀 You alreday use ({letter_guess}) 👀")
            used_letters.append(letter_guess)
        else:
            print(f"🫥  Invalid Input......({letter_guess}) 🫥")
if letter_guess == "stop":
    print(f"😕 Ok but the conutry was {computer_choice} 😕")
elif "_" in spaces:
    
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
    print(f"🤦 The word was ({computer_choice}) 😑\n")
else:
    print("""
              *********************
           (❁´◡`❁) YOU WIN  (❁´◡`❁)
              *********************
    """)
    print(Hangmanpics[len(Hangmanpics)-tries])
    print(f"\n              🫡  The word was {computer_choice} 🫡\n")