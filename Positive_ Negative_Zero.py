print("\n\t-------Welcome to Positive and Negative and Zero number-------\n")
str_number = input("Enter numbers separated by space: ").split()
numbers = []
for x in str_number:
    numbers.append(int(x))
negative = []
positive = []
zero = []
for i in numbers:
    if i < 0:
        negative.append(i)
    elif i > 0:
        positive.append(i)
    else:
        zero.append(i)
print(f"\nzero : {len(zero)} ")
print(f"negative : {len(negative)}")
print(f"positive : {len(positive)}")
while True:
    see = input("\nDo you want to see numbers? (yes or no): ").lower()
    if see == "yes":
        print(f"\n\t\tPositive number: {positive}")
        print(f"\t\tNegative number: {negative}")
        print(f"\t\tZero number: {zero}\n")
        break
    elif see == "no":
        print(f"\nGood bye 👋\n")
        break
    else:
        print(f"\nInvalid input.......... ({see}) is not yes or no Try again\n")