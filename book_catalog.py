import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def co():
    input("🔥 Press Enter To Continue: ")

books = {}

while True:
    clear()
    print("""
📚🔥 Menu:
1. ➕📖 Add Book
2. 📤📕 Check Out Book
3. 📥📗 Check In Book
4. 📚👀 List Books
5. 🚪 Exit
""")
    move = input("🎮🔥 Enter Your Choice: ").strip()

    if move.isdigit():
        move = int(move)

        if move < 6 and move > 0:

            if move == 1:
                while True:
                    clear()
                    isbn = input("🔢📖 Enter ISBN: ").strip()

                    if isbn.isdigit():

                        if isbn not in books:
                            title = input("📕 Enter The Title: ").strip()
                            author = input("✍️ Enter The Author: ").strip()

                            books[isbn] = {
                                "title": title,
                                "author": author,
                                "available": True
                            }

                            print(f"✅📚 Book '{title}' by {author} added to the datalog with\n")
                            co()

                            while True:
                                clear()
                                another = input("📚➕ Do you want to add another book? (y/n): ".title()).strip().lower()

                                if another == "y":
                                    break

                                elif another == "n":
                                    break

                                else:
                                    print("❌⚠️ Must Answer By (y,n)")
                                    co()

                            if another == "n":
                                break

                            continue

                        else:
                            print("❌📖 There are already this ISBN. Type another one".title())
                            co()

                    else:
                        print("❌🔢 The ISBN Must Be Number")
                        co()

            elif move == 4:
                if books:
                    clear()
                    print("📚🔥 Library Catalog:")

                    for x in books:
                        print(f"🆔 ISBN: {x}, 📖 Title: {books[x]["title"]}, ✍️ Author: {books[x]["author"]}, 📊 Available: {books[x]["available"]}")

                    choice = input("🔙 Do you want to go back to the main menu? (y/n): ").strip().lower()

                    if choice == "n":
                            print("😈😂 No You Will Back hahahah")
                            co()

                else:
                    print("📭😱 You Don't Have Any Books????.....")
                    co()

            elif move == 3:
                if books:
                    while True:
                        clear()
                        check_isbn = input("📥📖 Enter ISBN to check in or (Enter) To Consle: ").strip()
                        if check_isbn:
                            if check_isbn in books:
                                if books[check_isbn]["available"] == False:
                                    books[check_isbn]["available"] = True

                                    print(f"✅📚 Book '{books[check_isbn]["title"]}' Checked in successfully. ")
                                    co()

                                    while True:
                                        clear()
                                        again = input("📥📚 Do you want to check in another book? (y/n): ").strip().lower()

                                        if again == "y":
                                            break

                                        elif again == "n":
                                            break

                                        else:
                                            print("❌⚠️ Invalid choice. Please Enter (Y/N)")
                                            co()

                                    if again == "n":
                                        break

                                    continue
                                else:
                                    print("😑😑That's Book Is Already Out😐😐")
                                    co()
                            else:
                                print(f"❌🔎 {check_isbn} NOT Found!!!!!!")
                                co()
                        else:
                            break
                else:
                    print("📭😱 You Don't Have Any Books????.....")
                    co()

            elif move == 2:
                if books:
                    while True:
                        clear()
                        check_isbn = input("📤📖 Enter ISBN to check out or (Enter) To Consle: ").strip()
                        if check_isbn:
                            if check_isbn in books:
                                if books[check_isbn]["available"] == True:
                                    books[check_isbn]["available"] = False

                                    print(f"✅📚 Book '{books[check_isbn]["title"]}' Checked out successfully. ")
                                    co()

                                    while True:
                                        clear()
                                        again = input("📤📚 Do you want to check out another book? (y/n): ").strip().lower()

                                        if again == "y":
                                            break

                                        elif again == "n":
                                            break

                                        else:
                                            print("❌⚠️ Invalid choice. Please Enter (Y/N)")
                                            co()

                                    if again == "n":
                                        break

                                    continue
                                else:
                                    print("😑😑That's Book Is Already Out😐😐")
                                    co()

                            else:
                                print(f"❌🔎 {check_isbn} NOT Found!!!!!!")
                                co()
                        else:
                            break
                else:
                    print("📭😱 You Don't Have Any Books????.....")
                    co()

            else:
                print("👋🚪 Goodbye!")

                break

        else:
            print("❌⚠️ Invalid Choice. Please Enter Number between 1-5")
            co()

    else:
        print("❌🔢 Invalid Choice. Please Enter A Number")
        co()


clear()

while True:
    clear()
    print("⭐🔥 Now Evaluate Our App: ")

    evalute = input("⭐🔥 Enter Your Evaluation (1-5): ").strip()

    if evalute.isdigit():
        evalute = int(evalute)

        if evalute < 6 and evalute > 0:

            if evalute == 1:
                print("😵😢😢😢😢😳")
                break

            elif evalute == 2:
                print("🥺🥺🥺🥺🥺🥺🥺")
                break

            elif evalute == 3:
                print("🤔🤔🤔🤔")
                break

            elif evalute == 4:
                print("🫡 👌👌👌")
                break

            else:
                print("🤩🤩🤩😲🫡 🤩👍👌")
                break

        else:
            print("❌🔥 OHHHHHHHHHHHHHHHHHHHH Just (1-5)")
            co()

    else:
        print("❌💀 OH NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO....Numberrrrrrrrrrrrrrrrrrrrrrrrrrr")
        co()

print("👋🔥 Now I Have To Say GOOOODBye. I Will Miss You 😭😭😭")