import time
print("⌛-------Welcome to the Pomodoro Timer!-------⌛")
mint = int(input("Enter time in minutes: "))
total = mint * 60
while total > 0:
    mintues = total // 60
    sec = total % 60
    total -= 1
    clock = f"{mintues:02d}:{sec:02d}"
    print(f"\r⏱️ Time remaining: {clock}",end="")
    time.sleep(1)
print()
time.sleep
print("⏱️ Time remaining: 00:00")
print("Times up , Take a break")