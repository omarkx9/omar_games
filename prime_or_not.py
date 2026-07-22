print("\t-------Welcome to Prime or not-------")
while True:
    number = int(input("Enter the number: "))
    if number <= 1 :
        print(f"\n({number}) is a prime number\n")
        again = input("If you want to enter another number press (Enter) or type any letter: ")
        if again:
            print("\nGood bye👋\n")
            break
        else:
            continue
    elif number % 2 != 0:
        print(f"\n({number}) is a prime number\n")
        again = input("If you want to enter another number press (Enter) or type any letter: ")
        if again:
            print("\nGood bye👋\n")
            break
        else:
            continue
    else:
        print(f"\n({number}) is not a prime number\n")
        again = input("If you want to enter another number press (Enter) or type any letter: ")
        if again:
            print("\nGood bye👋\n")
            break
        else:
            continue