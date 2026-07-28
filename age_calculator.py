print("\n\t----Age in Days and Month and Hours Calculator---- 🎂📅⏰🔥")
print()
def again(x):
    return x == "yes"
while True:
    years = input("\t\t   ~~~Enter your age in years~~~ 🎂: ").strip()
    if years.isdigit():
        years = int(years)
        print(f"\n\t\t   !!!You Was Born In {2026 - years}!!! 🎉🎂🔥")
        while True:
            unit = input("please choose time unit (month(m), weeks(w), days(d), hours(h), minute(mi), second(s),) or the first letter ⏳⏰📅🔥: ".title()).strip().lower()
            month = years * 12
            weeks = years*52
            days = years * 365
            hours = years * 8760
            minutes = years * 525600
            second = years * 31622400 
            if unit == "month" or unit == "m":
                print("#"*80)
                print(f"(You Lived For {month:,} month) 🎂📅🔥".center(80,"#"))
                print("#"*80)
                if again(input("Enter (\"Yes\") If you want to enter another number or (Enter) 🔄: ").lower().strip()):
                    continue
                else:
                    break
            elif unit == "weeks" or unit == "w":
                print("#"*80)
                print(f"(You Lived For {weeks:,} week) 📅🔥⏳".center(80,"#"))
                print("#"*80)
                if again(input("Enter (\"Yes\") If you want to enter another number or (Enter) 🔄: ").lower().strip()):
                    continue
                else:
                    break
            elif unit == "days" or unit == "d":
                print("#"*80)
                print(f"(You Lived For {days:,} days) 📆🔥😎".center(80,"#"))
                print("#"*80)
                if again(input("Enter (\"Yes\") If you want to enter another number or (Enter) 🔄: ").lower().strip()):
                    continue
                else:
                    break
            elif unit == "hours" or unit == 'h':
                print("#"*80)
                print(f"(You Lived For {hours:,} hours) ⏰🔥⚡".center(80,"#"))
                print("#"*80)
                if again(input("Enter (\"Yes\") If you want to enter another number or (Enter) 🔄: ").lower().strip()):
                    continue
                else:
                    break
            elif unit == "minute" or unit == "mi":
                print("#"*80)
                print(f"(You Lived For {minutes:,} minute) ⏱️🔥💯".center(80,"#"))
                print("#"*80)
                if again(input("Enter (\"Yes\") If you want to enter another number or (Enter) 🔄: ").lower().strip()):
                    continue
                else:
                    break
            elif unit == "second" or unit == "s":
                print("#"*80)
                print(f"(You Lived For {second:,} second) ⏱️🔥⚡💯".center(80,"#"))
                print("#"*80)
                if again(input("Enter (\"Yes\") If you want to enter another number or (Enter) 🔄: ").lower().strip()):
                    continue
                else:
                    break
            else:
                print(f"{unit} Please Check For The Input... 🤔❌🔍")
        play_again = input("do you want to play again ? if yes (press any thing) or (press Enter) to skip 🔄🎮🔥: ".title()).strip()
        if play_again:
            continue
        else:
            print("Goodbye 👋😎🔥🎉")
            break
    else:
        print(f"{years} is not a number please Try again..... ❌🔢🤔🔥")