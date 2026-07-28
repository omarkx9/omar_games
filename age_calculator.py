print("\n\t----Age in Days and Month and Hours Calculator----")
print()
def again(x):
    return x == "yes"
while True:
    years = input("\t\t   ~~~Enter your age in years~~~: ").strip()
    if years.isdigit():
        years = int(years)
        print(f"\n\t\t   !!!You Was Born In {2026 - years}!!!")
        while True:
            unit = input("please choose time unit (month, weeks, days, hours, mint, seconde,): ".title()).strip().lower()
            month = years * 12
            weeks = years*52
            days = years * 365
            hours = years * 8760
            mintutes = years * 525600
            seconde = years * 31622400 
            if unit == "month":
                print("\t\t________________________________")
                print(f"\t\t (You Lived For {month:,} month)")
                if again(input("Enter (\"Yes\") If you want to enter a nother number or (Enter): ").lower().strip()):
                    continue
                else:
                    break
            elif unit == "weeks":
                print("\t\t________________________________")
                print(f"\t\t (You Lived For {weeks:,} week)")
                if again(input("Enter (\"Yes\") If you want to enter a nother number or (Enter): ").lower().strip()):
                    continue
                else:
                    break
            elif unit == "days":
                print("\t\t________________________________")
                print(f"\t\t (You Lived For {days:,} days)")
                if again(input("Enter (\"Yes\") If you want to enter a nother number or (Enter): ").lower().strip()):
                    continue
                else:
                    break
            elif unit == "hours":
                print("\t\t________________________________")
                print(f"\t\t (You Lived For {hours:,} hours)")
                if again(input("Enter (\"Yes\") If you want to enter a nother number or (Enter): ").lower().strip()):
                    continue
                else:
                    break
            elif unit == "mint":
                print("\t\t________________________________")
                print(f"\t\t (You Lived For {mintutes:,} mintute)")
                if again(input("Enter (\"Yes\") If you want to enter a nother number or (Enter): ").lower().strip()):
                    continue
                else:
                    break
            elif unit == "seconde":
                print("\t\t________________________________")
                print(f"\t\t (You Lived For {seconde:,} seconde)")
                if again(input("Enter (\"Yes\") If you want to enter a nother number or (Enter): ").lower().strip()):
                    continue
                else:
                    break
            else:
                print(f"{unit} Please Check For The Input...")
        play_again = input("do you want to play again ? if yes (press any thing) or (press Enter) to skip: ".title()).strip()
        if play_again:
            continue
        else:
            print("Goodbye")
            break
    else:
        print(f"{years} is not a number please Try again.....")