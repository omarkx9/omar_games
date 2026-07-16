no1 = float(input("Please Enter the first number: "))
no2 = float(input("Please Enter the second number: "))
no3 = float(input("Please Enter the third number: "))
if no1 == no2 and no1 == no3:
    print(f"All numbers is {no1}")
elif no1 >= no2 and no1 >= no3:
    print(f"The largest number is {no1}")
elif no2 >= no1 and no2 >= no3:
    print(f"The largest number is {no2}")
else:
    print(f"The largest number is {no3}")
# fathi