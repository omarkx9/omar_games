import string
import os
def play_again():
    x = input("🔄️Do you want to play again? (Y/N)🔄️: ").strip().lower()
    if x == "y":
        return True
    else:
        return False
lower = string.ascii_lowercase*2
upper = string.ascii_uppercase*2
lock = """
            .-""-.
           / .--. \\
          / /    \\ \\
          | |    | |
          | |.-""-.|
         ///`.::::.`\\
        ||| ::/  \\:: ;
        ||; ::\\__/:: ;
         \\\ '::::' /
          `=':-..-'`
 
"""
unlock = """
        .-""-.
       / .--. |
      | /   | |
            | |.-""-.
            ///`.::::.`\\
           ||| ::/  \\:: ;
           ||; ::\\__/:: ;
            \\\ '::::' /
             `=':-..-'`
"""
def clear():
    os.system("cls" if os.name == 'nt' else "clear")
clear()

while True:
    new_message = ""
    clear()
    welcome = "Welcome to the Caesar Cipher App!".center(47,"-")
    print(f"\n🔒{welcome}🔓")
    app = input("\n1_Encrypt🔐\n2_Decrypt🔓\n\n💬Before Start Chose👊 an App🗨️: ").strip().lower()
    if app == "1":
        clear()
        print(lock)
        input("🌠----Press Enter To Continue----🌠")
        clear()
        message = input("Enter a message: ").strip()
        while True:
            clear()
            shift = input("Enter a shift number: ").strip()
            if shift.isdigit():
                break
            else:
                print("👺...Invalid Choice Shift Most To Be Number...👺")
                input("🌠----Press Enter To Continue----🌠")
        shift = int(shift)
        for x in message:
            if x in lower:
                num = lower.index(x)
                new_message += lower[num+shift]
            elif x in upper:
                num = upper.index(x)
                new_message += upper[num+shift]
            else:
                new_message += x
        print(f"🔐Encrypted🔐 Message: {new_message} ")
        if play_again():
            continue
        else:
            print("🙋‍♂️🙋‍♂️Goodbye👋👋👋")
            break

    elif app == "2":
        new_message = ""
        clear()
        print(unlock)
        input("🌠----Press Enter To Continue----🌠")
        clear()
        message = input("Enter a message: ").strip()
        while True:
            clear()
            shift = input("Entre a shift number: ")
            if shift.isdigit():
                shift = int(shift)
                break
            else:
                print("👺...Invalid Choice Shift Most To Be Number...👺")
                input("🌠----Press Enter To Continue----🌠")
        for x in message:
            if x in lower:
                num = lower.index(x)
                new_message += lower[num-shift]
            elif x in upper:
                num = upper.index(x)
                new_message += upper[num-shift]
            else:
                new_message += x
        print(f"Here is the original message:\n***********")
        print()
        print(f"{new_message}\n\n************")
        if play_again():
            continue
        else:
            print("🙋‍♂️🙋‍♂️Goodbye👋👋👋")
            break
    else:
        clear()
        print("👺Invalid Choice....Please Entre (1 or 2) Try.again...👺")
        input("🌠----Press Enter To Continue----🌠")
