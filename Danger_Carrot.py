import random
print("\n            {--------Welcome To Danger Carrot--------}\n")
rulse ="""
          ________________THE RULSE________________ 
         |                                         |
         | 1. You Chose 4 Carrots.                 |
         | 2. If One Of Them is TNT You Well Dide. |
         | 3. You Can't Chose The Same Carrot.     |
         |                                         |
        =============================================
"""
def tree(x):
    print(f"\n       column!\n       1  2  3")
    i = 1
    for number in range(len(x)):
        
        print("row",i," ".join(x[number]))
        i += 1
while True:
    Rulse = input("If you want see the Rulse or not type (Yes , No): ")
    if Rulse.lower() == "yes":
        print(rulse)
        break
    elif Rulse.lower() == "no":
        print("\nOK no proplem\n")
        break
    else:
        print("\nWHHHHAT........{}\nPlease type (Yes or No)".format(Rulse))
level = 4
trees = [['🥕', '🥕', '🥕'],['🥕', '🥕', '🥕'],['🥕', '🥕', '🥕']]
random_row = random.randint(0,2)
random_column = random.randint(0,2)
answer = []
while level > 0:
    stop = input("\nIF YOU WANT TO (EXIT) TYPE (EXIT) OR (ENTER) TO CONTINUE: ").lower()
    if stop == "exit":
        break
    else:
        if stop:
            print("\nARE YOU CRAZY..{}".format(stop))
            continue
    tree(trees)
    user_row = input("\nEnter the number of row🐰: ")
    
    user_column = input("Enter the number of column🐰: ")
    
    if user_column.isdigit() and user_row.isdigit() and len(user_column) == 1 and len(user_row) == 1 and int(user_column) <= len(trees) and int(user_column) > 0 and int(user_row) <= len(trees) and int(user_row) > 0:
        if [user_column,user_row] not in answer:
            answer.append([user_column,user_row])
            if int(user_row) == random_row+1 and int(user_column) == random_column+1:
                trees[int(user_row)-1][int(user_column)-1] = "☠️ "
                tree(trees)
                print(f"\nYou lose You eat the TNT")
                break
            else:
                trees[int(user_row)-1][int(user_column)-1] = "🐰"
                print("===========================")
                tree(trees)
                print("===========================")
                level -= 1
        else:
             print("You already use these: ")
    else:
        print("Invalid choice............ Try again")
if level == 0:
    print("""
    &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    &&&&&&&&&&&&&& YOU WIN &&&&&&&&&&&&&&
    &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    """)
    print("The TNT was there!")
    trees[random_row][random_column] = "💣"
    tree(trees)
    print("\nCongratulations!\n")
elif stop.capitalize() == "Exit":
    print("\nOk GOOOOOOOD Byeeeeeeee\n")
else:
    print("HAHAHAHAHA LOSER")
while True:
    تقييم = int(input("Enter your Evaluation (1-5): "))
    if str( تقييم).isdigit() :
        if تقييم ==1:
            print("😢😢😢🫨")
            break
        elif تقييم ==2:
            print("🤨🤔🤨🤔")
            break
        elif تقييم ==3:
            print("😐😐😐")
            break
        elif تقييم ==4:
            print("🫡 🫡 🫡")
            break
        elif تقييم ==5:
            print("\n😮😲🤩🤩🤩 Thanks.....\n")
            break
        else:
            print("\nNO NO NO Please Enter (1-5)..........Try again\n")
    else:
        print("ARE YOU CARZY (1-5).............................................")