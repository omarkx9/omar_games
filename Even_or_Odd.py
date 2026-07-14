# print Welcome to user
print("\n\t-------Welcome to Even or Odd-------")
# ask user to enter a number and save the number in a varibale
number = int(input('Enter a number: '))
# check if the number is Even
if number % 2 == 0:
    # print to the user his number and the number is Even
    print(f"{number} is Even")
# check is the number is Odd
else:
    #print to the user his nubmer and the number is Odd
    print(f"{number} is Odd")