print("\n\t----Age in Days and Month and Hours Calculator----")
print()
while True:
    years = input("\t\t   ~~~Enter your age in years~~~: ").strip()
    if years.isdigit():
        years = int(years)
        print(f"\t\t   !!!You Was Born In {2026 - years}!!!")
        month = years * 12
        days = years * 365
        hours = years * 8760
        mintutes = years * 525600
        seconde = years * 31622400 
        print("\t\t+++++++++++++++++++++++++++++++")
        print(f"\t\t|& You Lived For {days:,} Days  &|\n\t\t|& And {hours:,} Hours          &|\n\t\t|& And {mintutes:,} Mintutes    &|\n\t\t|& And {seconde:,} Seconde    &|")
        print("\t\t+++++++++++++++++++++++++++++++")
        again = input("Enter (\"Yes\") If you want to enter a nother number or (Enter): ").lower().strip()
        if not again:
            print("Good bye")
            break
        else:
            continue
    else:
        print(f"{years} is not a number please Try again.....")