print("\n\t----Age in Days and Month and Hours Calculator----")
print()
years = int(input("\t\t   ~~~Enter your age in years~~~: "))
print(f"\t\t   !!!You Was Born In {2026 - years}!!!")
month = years * 12
days = years * 365
hours = years * 8760
mintutes = years * 525600
seconde = years * 31622400 
print("\t\t+++++++++++++++++++++++++++++++")
print(f"\t\t|& You Lived For {days:,} Days  &|\n\t\t|& And {hours:,} Hours          &|\n\t\t|& And {mintutes:,} Mintutes    &|\n\t\t|& And {seconde:,} Seconde    &|")
print("\t\t+++++++++++++++++++++++++++++++")
