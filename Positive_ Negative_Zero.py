print("\n\t-------Welcome to Positive and Negative and Zero number-------\n")
positive_number = []
negative_number = []
zero_number = []
str_number = input("Enter  numbers to sveral: ").split()
number = []
for x in str_number:
    number.append(int(x))
for y in number:
    if y < 0:
        negative_number.append(y)
    elif y == 0:
        zero_number.append(y)
    else:
        positive_number.append(y)
print(f"\n\t\tPpsitive number: {len(positive_number)}\n\t\tNegative number: {len(negative_number)}\n\t\tZero number: {len(zero_number)}\n")