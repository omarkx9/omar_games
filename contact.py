import time

contact = {}

while True:
    print("""
          📱📱📱 ========================= 📱📱📱
            🟢 1. Add Contact 👤➕📞
            📋 2. Show All Contacts 👥👥👥
            🔴 3. Remove Contact 👤❌🗑️
            🚪 4. Exit 👋👋👋
          📱📱📱 ========================= 📱📱📱
""")

    chose = input("🎯🎯 Choose a number to do: ".title()).strip()

    if chose.isdigit() and int(chose) < 5 and int(chose) > 0:

        if chose == "1":
            name = input("👤✨ Enter the name of the person: ".title()).strip()

            if name.isalpha():
                print("\n⏳⏳⏳ Ok, wait a second... 😎🔥")
                time.sleep(2)

                phone = input("\n📞📱 Enter the number of the person: ".title()).strip()

                if phone.isdigit():
                    contact[name] = phone

                    print("\n🚀🚀🚀 Now..... 🤩🤩🤩")
                    time.sleep(1)

                    print(f"\n🎉🎉🎉 {name} is added! 👤✅📞🔥🥕🐰")

            else:
                print("\n❌❌❌ Invalid Choice.......... 🔄🔄🔄 Try again! 🤨🤨🤨💥\n")

        elif chose == "2":

            if contact:
                n = 1

                for x, y in contact.items():
                    print(f"👤 {n}.", f"✨ {x}.", "📞 No:", y, "🔥🔥")
                    n += 1

            else:
                print("\n📭📭📭 You Don't Have Any Person In Your Contacts 😭😭😭💔")

        elif chose == "3":

            if contact:
                n = 1

                for x, y in contact.items():
                    print(f"👤 {n}. {x}. 📞 No: {y} 🔥")
                    n += 1

                name_delete = input("🗑️❌ Enter name to delete: ".title()).strip()

                if name_delete in contact:
                    time.sleep(3)

                    contact.pop(name_delete)

                    print(f"🗑️💥 {name_delete} Deleted! ❌👤🔥😎")

                else:
                    print("\n❌❌❌ Invalid Choice.......... 🔄🔄🔄 Try again! 🤨🤨🤨💥\n")

            else:
                print("\n📭📭📭 You Don't Have Any Person In Your Contacts 😭😭😭💔")

        else:
            break

    else:
        print("\n🚫❌🚫 Invalid Choice.......... 🔄🔄🔄 Try again! 🤨🤯💥🔥\n")


while True:

    Evaluation = input("⭐️⭐️⭐️ Enter your Evaluation (1-5): ⭐️⭐️⭐️ ")

    if Evaluation.isdigit():

        if int(Evaluation) == 1:
            print("😢😢😢🫨💔💔💔😭😭😭")
            break

        elif int(Evaluation) == 2:
            print("🤨🤔🤨🤔😐😐💭💭")

            break

        elif int(Evaluation) == 3:
            print("😐😐😐👍👍👍🙂🙂✨")

            break

        elif int(Evaluation) == 4:
            print("🫡🫡🫡🔥🔥🔥👏👏👏🤩🤩🤩💯💯")

            break

        elif int(Evaluation) == 5:
            print("\n😮😲🤩🤩🤩🔥🔥🔥🎉🎉🎉🎊🎊🎊🚀🚀🚀💯💯💯🏆🏆🏆 Thanks..... 🎉🔥🤩👏👏👏\n")

            break

        else:
            print("\n🚫❌🚫❌ NO NO NO 😭😭😭 Please Enter (1-5).......... 🔄🔄🔄 Try again! 🔄🤨🤨🤨💥🔥🚨🚨🚨\n")

    else:
        print("🤯🤯🤯 ARE YOU CRAZY?! 😭😂😭😂 (1-5)............................................. 🤯💥🚨🔥")