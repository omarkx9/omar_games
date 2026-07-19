import time
print("⌛-------Welcome to the Pomodoro Timer!-------⌛")
number_of_seconde = int(input("\t🕰️ Enter time in minutes: "))
total = number_of_seconde * 60
if number_of_seconde != 0:
    while total > -1:
        mintues = total // 60
        sec = total % 60
        total -= 1
        clock = f"{mintues:02d}:{sec:02d}"
        print(f"\r\t⏱️ Time remaining: {clock}",end="")
        time.sleep(1)
    print()
    print("\t🛑Times up , Take a break")
else:
    print("😧 What!!!!!!! these number is zero 😧")