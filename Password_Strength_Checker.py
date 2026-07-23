import string
print("\n\t-------Welcome to Password Strength Checker-------\n")
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
punctuation = string.punctuation
Rules = ["1️⃣  At least 8 characters long,","2️⃣  Has at least 1 uppercase letter,","3️⃣  Has at least 1 lowercase letter,","4️⃣  Has at least 1 number,","5️⃣  Has at least 1 spicial character"]
rules = f"""
             *-------------THE RULES--------------*
             | {Rules[0]}     |
             | {Rules[1]}| 
             | {Rules[2]}|
             | {Rules[3]}          |
             | {Rules[4]}|
             *____________________________________*         
"""
while True:
    want_rules = input("If you want the rules press (yes) If not press (no): ").lower()
    if want_rules == "yes":
        print(rules)
        break
    elif want_rules == "no":
        break
    else:
        print("Invalid Choice!!.......... Please type (Yes or NO), Try again.")
while True:
    password = input("Enter password: ")
    lower_count = 0
    upper_count = 0
    number_count= 0
    spicial_count= 0
    for x in password:
        if x in lower:
            lower_count += 1 
        elif x in upper:
            upper_count += 1
        elif x in numbers:
            number_count += 1
        elif x in punctuation:
            spicial_count += 1
        else:
            continue
    if len(password) < 8:
        print(Rules[0])
    if upper_count < 1:
        print(Rules[1])
    if lower_count < 1:
        print(Rules[2])
    if number_count < 1:
        print(Rules[3])
    if spicial_count < 1:
        print(Rules[4])
    if lower_count >= 1 and upper_count >= 1 and number_count >= 1 and spicial_count >= 1 and len(password) >= 8:
        print(f"({password}) That is strong password")
        break