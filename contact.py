
import os
import time
import string


OPTIONS = """
╔══════════════════════════════════════════════╗
║        📱📒 CONTACT MANAGER 📒📱             ║
╠══════════════════════════════════════════════╣
║                                              ║
║   1️⃣ ➕ Add a Contact                         ║
║   2️⃣ 👀 View All Contacts                     ║
║   3️⃣ 🔍 Search for a Contact                  ║
║   4️⃣ ✏️ Edit a Contact                         ║
║   5️⃣ 🗑️ Delete a Contact                       ║
║   6️⃣ 💾 Save Contacts                         ║
║   7️⃣ 📂 Load Contacts                         ║
║   8️⃣ 🚪 Exit                                  ║
║                                              ║
╚══════════════════════════════════════════════╝
""".title()


contacts = {}


# ══════════════════════════════════════════════
# 🧹 CLEAR SCREEN
# ══════════════════════════════════════════════

def clear():
    os.system("cls" if os.name == "nt" else "clear")


# ══════════════════════════════════════════════
# ❌ ERROR MESSAGE
# ══════════════════════════════════════════════

def error(title, reason, example=None):

    clear()

    print("╔══════════════════════════════════════════════╗")
    print(f"║ ❌ {title.upper()}")
    print("╠══════════════════════════════════════════════╣")
    print("║")
    print("║ 🧐 Reason:")
    print(f"║ 👉 {reason}")

    if example:
        print("║")
        print(f"║ 💡 Example: {example}")

    print("║")
    print("╚══════════════════════════════════════════════╝")

    time.sleep(2)


# ══════════════════════════════════════════════
# ✅ SUCCESS MESSAGE
# ══════════════════════════════════════════════

def success(message):

    clear()

    print("╔══════════════════════════════════════════════╗")
    print("║                  ✅ SUCCESS 🎉               ║")
    print("╠══════════════════════════════════════════════╣")
    print("║")
    print(f"║ 🎯 {message}")
    print("║")
    print("╚══════════════════════════════════════════════╝")

    time.sleep(1.5)


# ══════════════════════════════════════════════
# 📧 CHECK EMAIL
# ══════════════════════════════════════════════

def check_email(email):

    email = email.strip().lower()

    # 🧹 Remove spaces
    email = "".join(x for x in email if x != " ")

    letter = 0
    number = 0
    special = 0

    for x in email:

        if x.isdigit():
            number += 1

        elif x.isalpha():
            letter += 1

        elif x in string.punctuation:
            special += 1

    # 🔤 Must contain letters
    if not letter:
        return False

    # 🔢 Must contain a number
    if not number:
        return False

    # 🔣 Must contain a special character
    if not special:
        return False

    # 📧 Must contain Gmail
    if "gmail" not in email:
        return False

    # 🌐 Must contain .com
    if ".com" not in email:
        return False

    return True


# ══════════════════════════════════════════════
# 📱 CHECK PHONE
# ══════════════════════════════════════════════

def check_phone(phone):

    # 🔢 Numbers only
    if not phone.isdigit():
        return False

    # 📏 Exactly 10 digits
    if len(phone) != 10:
        return False

    # 🇸🇦 Must start with 05
    if not phone.startswith("05"):
        return False

    return True


# ══════════════════════════════════════════════
# 📂 LOAD CONTACTS
# ══════════════════════════════════════════════

def load():

    # 📁 Create folder if it doesn't exist
    if not os.path.exists("contacts"):
        os.makedirs("contacts")

    contacts.clear()

    loaded = 0

    for file_name in os.listdir("contacts"):

        # 📄 Ignore files that aren't .txt
        if not file_name.endswith(".txt"):
            continue

        with open(f"contacts/{file_name}", "r") as file:

            phone = file.readline().strip()
            email = file.readline().strip()

        # 👤 Get contact name from filename
        name = file_name.removesuffix(".txt")

        contacts[name] = {
            "phone": phone,
            "email": email,
        }

        loaded += 1

    return loaded


# ══════════════════════════════════════════════
# ➕ ADD CONTACT
# ══════════════════════════════════════════════

def add():

    rules = """
╔══════════════════════════════════════════════╗
║              📋 ADD RULES 📋                 ║
╠══════════════════════════════════════════════╣
║                                              ║
║ 👤 Contact Name:                             ║
║    🔹 Cannot be empty                        ║
║    🔹 Cannot contain only numbers            ║
║    🔹 Must be unique                         ║
║                                              ║
║ 📱 Phone Number:                             ║
║    🔹 Numbers only                           ║
║    🔹 Must start with 05                     ║
║    🔹 Must contain exactly 10 digits         ║
║                                              ║
║ 📧 Email:                                    ║
║    🔹 Must contain letters                   ║
║    🔹 Must contain a number                  ║
║    🔹 Must contain a special character       ║
║    🔹 Must contain "gmail"                   ║
║    🔹 Must contain ".com"                    ║
║                                              ║
╚══════════════════════════════════════════════╝
"""

    # 📋 Ask about rules
    while True:

        see = input(
            "📋 Do you want to see the rules? (y/n): "
        ).strip().lower()

        if see in ["y", "yes"]:

            clear()
            print(rules)

            input("\n👉 PRESS ENTER TO CONTINUE... ")

        elif see in ["n", "no"]:
            break

        else:

            error(
                "Invalid Choice ⚠️",
                "You must answer with Y or N.",
                "y"
            )

    # ══════════════════════════════════════════
    # 👤 NAME
    # ══════════════════════════════════════════

    while True:

        clear()

        print("╔══════════════════════════════════════════════╗")
        print("║              👤 ADD CONTACT                 ║")
        print("╚══════════════════════════════════════════════╝")

        name_contact = input(
            "\n👤 What's the contact name?: "
        ).strip().capitalize()

        if not name_contact:

            error(
                "Invalid Contact Name ❌",
                "The contact name cannot be empty.",
                "Omar"
            )

            continue

        if name_contact.isdigit():

            error(
                "Invalid Contact Name ❌",
                "The contact name cannot contain only numbers.",
                "Omar"
            )

            continue

        if name_contact in contacts:

            error(
                "Contact Already Exists ⚠️",
                "A contact with this name already exists.",
                "Choose another name."
            )

            continue

        break

    # ══════════════════════════════════════════
    # 📱 PHONE
    # ══════════════════════════════════════════

    while True:

        clear()

        phone_number = input(
            "📱 Enter phone number: "
        ).strip()

        if not phone_number.isdigit():

            error(
                "Invalid Phone Number ❌",
                "The phone number must contain numbers only.",
                "0512345678"
            )

            continue

        if len(phone_number) != 10:

            error(
                "Invalid Phone Number ❌",
                "The phone number must contain exactly 10 digits.",
                "0512345678"
            )

            continue

        if not phone_number.startswith("05"):

            error(
                "Invalid Phone Number ❌",
                "The phone number must start with 05.",
                "0512345678"
            )

            continue

        break

    # ══════════════════════════════════════════
    # 📧 EMAIL
    # ══════════════════════════════════════════

    while True:

        clear()

        email = input(
            "📧 Enter the email: "
        ).strip().lower()

        if not email:

            error(
                "Invalid Email ❌",
                "The email cannot be empty.",
                "omar123@gmail.com"
            )

            continue

        if not any(x.isalpha() for x in email):

            error(
                "Invalid Email ❌",
                "The email must contain at least one letter.",
                "omar123@gmail.com"
            )

            continue

        if not any(x.isdigit() for x in email):

            error(
                "Invalid Email ❌",
                "The email must contain at least one number.",
                "omar123@gmail.com"
            )

            continue

        if not any(x in string.punctuation for x in email):

            error(
                "Invalid Email ❌",
                "The email must contain a special character.",
                "omar123@gmail.com"
            )

            continue

        if "gmail" not in email:

            error(
                "Invalid Email ❌",
                'The email must contain "gmail".',
                "omar123@gmail.com"
            )

            continue

        if ".com" not in email:

            error(
                "Invalid Email ❌",
                'The email must contain ".com".',
                "omar123@gmail.com"
            )

            continue

        break

    # 💾 Add to dictionary

    contacts[name_contact] = {
        "phone": phone_number,
        "email": email,
    }

    success(
        f"🎉 {name_contact} was added successfully!\n"
        f"💾 Remember to save your contacts using option 6."
    )

    # ➕ Add another?

    again = input(
        "➕ Do you want to add another contact? (y/n): "
    ).strip().lower()

    if again in ["y", "yes"]:
        add()


# ══════════════════════════════════════════════
# 👀 DISPLAY CONTACTS
# ══════════════════════════════════════════════

def display():

    clear()

    if contacts:

        print("╔══════════════════════════════════════════════╗")
        print("║             📒 ALL CONTACTS 📒              ║")
        print("╚══════════════════════════════════════════════╝\n")

        number = 0

        for name in contacts:

            number += 1

            print(
                f"🔢 {number}. 👤 {name}\n"
                f"   📞 {contacts[name]['phone']}\n"
                f"   📧 {contacts[name]['email']}\n"
            )

        input("\n👉 PRESS ENTER TO CONTINUE...")

    else:

        error(
            "No Contacts Found 📭",
            "There are currently no contacts to display.",
            "Add a contact first using option 1."
        )


# ══════════════════════════════════════════════
# 🔍 SEARCH CONTACT
# ══════════════════════════════════════════════

def search():

    clear()

    if not contacts:

        error(
            "No Contacts Found 📭",
            "There are no contacts available to search.",
            "Add a contact first using option 1."
        )

        return

    name = input(
        "🔍 What's the name you want to search for?: "
    ).strip().capitalize()

    if name not in contacts:

        error(
            "Contact Not Found 🔎❌",
            f'No contact named "{name}" exists.',
            "Enter an existing contact name."
        )

        return

    clear()

    print("╔══════════════════════════════════════════════╗")
    print("║             🔍 CONTACT FOUND 🎯             ║")
    print("╠══════════════════════════════════════════════╣")
    print(f"║ 👤 Name:  {name}")
    print(f"║ 📞 Phone: {contacts[name]['phone']}")
    print(f"║ 📧 Email: {contacts[name]['email']}")
    print("╚══════════════════════════════════════════════╝")

    input("\n👉 PRESS ENTER TO CONTINUE...")


# ══════════════════════════════════════════════
# ✏️ EDIT AGAIN
# ══════════════════════════════════════════════

def another_edit():

    again = input(
        "\n✏️ Do you want to edit again? (y/n): "
    ).strip().lower()

    return again in ["y", "yes"]


# ══════════════════════════════════════════════
# ✏️ EDIT CONTACT
# ══════════════════════════════════════════════

def edit():

    clear()

    if not contacts:

        error(
            "No Contacts Found 📭",
            "There are no contacts available to edit.",
            "Add a contact first using option 1."
        )

        return

    old_name = input(
        "✏️ Enter the name of the contact: "
    ).strip().capitalize()

    if old_name not in contacts:

        error(
            "Contact Not Found 🔎❌",
            f'No contact named "{old_name}" exists.',
            "Enter an existing contact name."
        )

        return

    while True:

        clear()

        print("""
╔══════════════════════════════════════════════╗
║              ✏️ EDIT OPTIONS ✏️              ║
╠══════════════════════════════════════════════╣
║                                              ║
║   1️⃣ 👤 Edit Name                            ║
║   2️⃣ 📞 Edit Phone Number                    ║
║   3️⃣ 📧 Edit Email                           ║
║                                              ║
╚══════════════════════════════════════════════╝
""")

        move = input(
            "👉 Choose one option (1-3): "
        ).strip()

        if move not in ["1", "2", "3"]:

            error(
                "Invalid Edit Choice ❌",
                "You must choose option 1, 2, or 3.",
                "1"
            )

            continue

        # ══════════════════════════════════════
        # 👤 EDIT NAME
        # ══════════════════════════════════════

        if move == "1":

            clear()

            new_name = input(
                "👤 Enter the new name: "
            ).strip().capitalize()

            if not new_name:

                error(
                    "Invalid Name ❌",
                    "The new name cannot be empty.",
                    "Ahmed"
                )

                continue

            if new_name.isdigit():

                error(
                    "Invalid Name ❌",
                    "The new name cannot contain only numbers.",
                    "Ahmed"
                )

                continue

            if new_name in contacts:

                error(
                    "Name Already Exists ⚠️",
                    "Another contact already uses this name.",
                    "Choose a different name."
                )

                continue

            old_path = f"contacts/{old_name}.txt"
            new_path = f"contacts/{new_name}.txt"

            if os.path.exists(old_path):

                os.rename(
                    old_path,
                    new_path
                )

            contacts[new_name] = contacts.pop(old_name)

            old_name = new_name

            success(
                "👤 The contact name was updated successfully! 🎉"
            )

        # ══════════════════════════════════════
        # 📞 EDIT PHONE
        # ══════════════════════════════════════

        elif move == "2":

            clear()

            new_phone = input(
                "📞 Enter the new phone number: "
            ).strip()

            if not new_phone.isdigit():

                error(
                    "Invalid Phone Number ❌",
                    "The phone number must contain numbers only.",
                    "0512345678"
                )

                continue

            if len(new_phone) != 10:

                error(
                    "Invalid Phone Number ❌",
                    "The phone number must contain exactly 10 digits.",
                    "0512345678"
                )

                continue

            if not new_phone.startswith("05"):

                error(
                    "Invalid Phone Number ❌",
                    "The phone number must start with 05.",
                    "0512345678"
                )

                continue

            contacts[old_name]["phone"] = new_phone

            file_path = f"contacts/{old_name}.txt"

            if os.path.exists(file_path):

                with open(file_path, "w") as file:

                    file.write(
                        f"{contacts[old_name]['phone']}\n"
                    )

                    file.write(
                        contacts[old_name]["email"]
                    )

            success(
                "📞 The phone number was updated successfully! 🎉"
            )

        # ══════════════════════════════════════
        # 📧 EDIT EMAIL
        # ══════════════════════════════════════

        else:

            clear()

            new_email = input(
                "📧 Enter the new email: "
            ).strip().lower()

            if not check_email(new_email):

                error(
                    "Invalid Email ❌",
                    "The email must contain letters, numbers, "
                    'a special character, "gmail", and ".com".',
                    "omar123@gmail.com"
                )

                continue

            contacts[old_name]["email"] = new_email

            file_path = f"contacts/{old_name}.txt"

            if os.path.exists(file_path):

                with open(file_path, "w") as file:

                    file.write(
                        f"{contacts[old_name]['phone']}\n"
                    )

                    file.write(
                        contacts[old_name]["email"]
                    )

            success(
                "📧 The email was updated successfully! 🎉"
            )

        if not another_edit():
            break


# ══════════════════════════════════════════════
# 🗑️ DELETE CONTACT
# ══════════════════════════════════════════════

def deleter():

    clear()

    if not contacts:

        error(
            "No Contacts Found 📭",
            "There are no contacts available to delete.",
            "Add a contact first using option 1."
        )

        return

    name = input(
        "🗑️ Enter the name to delete: "
    ).strip().capitalize()

    if name not in contacts:

        error(
            "Contact Not Found 🔎❌",
            f'No contact named "{name}" exists.',
            "Enter an existing contact name."
        )

        return

    file_path = f"contacts/{name}.txt"

    if os.path.exists(file_path):

        os.remove(file_path)

    del contacts[name]

    success(
        f"🗑️ {name} was deleted successfully! 👋"
    )


# ══════════════════════════════════════════════
# 💾 SAVE CONTACTS
# ══════════════════════════════════════════════

def save():

    if not contacts:

        error(
            "Nothing To Save 💾❌",
            "There are no contacts currently stored in memory.",
            "Add a contact first using option 1."
        )

        return

    os.makedirs(
        "contacts",
        exist_ok=True
    )

    for name in contacts:

        with open(
            f"contacts/{name}.txt",
            "w"
        ) as file:

            file.write(
                f"{contacts[name]['phone']}\n"
            )

            file.write(
                contacts[name]["email"]
            )

    success(
        "💾 All contacts were saved successfully! 🎉📂"
    )


# ══════════════════════════════════════════════
# 🚪 EXIT
# ══════════════════════════════════════════════

def exit_program():

    messages = [
        "⏳ Just 1 second...",
        "💾 Remember to save your contacts!",
        "📂 You can load them next time!",
        "🚀 We are near...",
        "⏳ Just 1 second...",
        "👋 See you later!",
        "BYEEEEEEEEEEE 😂🔥👋"
    ]

    for message in messages:

        clear()

        print(
            f"\n\n\n"
            f"              {message}"
            f"\n\n\n"
        )

        time.sleep(1)


# ══════════════════════════════════════════════
# 📱 MAIN MENU
# ══════════════════════════════════════════════

def main_menu():

    if not os.path.exists("contacts"):
        os.makedirs("contacts")

    clear()

    print("""
╔══════════════════════════════════════════════╗
║                 ⚠️ WARNING ⚠️                ║
╠══════════════════════════════════════════════╣
║                                              ║
║ 📂 You have to LOAD your contacts using     ║
║    option 7️⃣ before using them.              ║
║                                              ║
╚══════════════════════════════════════════════╝
""")

    time.sleep(2)

    while True:

        clear()

        print(OPTIONS)

        choice = input(
            "\n👉 Enter your choice (1-8): "
        ).strip()

        # 🔢 Must be a number
        if not choice.isdigit():

            error(
                "Invalid Menu Choice ❌",
                "The menu choice must be a number from 1 to 8.",
                "1"
            )

            continue

        # 🚫 Number outside 1-8
        if choice not in [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8"
        ]:

            error(
                "Invalid Menu Choice ❌",
                "The number you entered is outside the available options.",
                "Choose a number from 1 to 8."
            )

            continue

        # ➕ ADD
        if choice == "1":
            add()

        # 👀 DISPLAY
        elif choice == "2":
            display()

        # 🔍 SEARCH
        elif choice == "3":
            search()

        # ✏️ EDIT
        elif choice == "4":
            edit()

        # 🗑️ DELETE
        elif choice == "5":
            deleter()

        # 💾 SAVE
        elif choice == "6":
            save()

        # 📂 LOAD
        elif choice == "7":

            loaded = load()

            success(
                f"📂 {loaded} contact(s) loaded successfully! 🎉"
            )

        # 🚪 EXIT
        elif choice == "8":

            exit_program()

            break


# 🚀 START PROGRAM
main_menu()