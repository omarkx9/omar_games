import os
import time

usd = 1.0
sar = 3.75
egp = 50.72
sdg = 600.5

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def calculate_converter(amount, source_rate, target_rate):
    amount = float(amount)
    source_rate = float(source_rate)
    target_rate = float(target_rate)
    return amount * target_rate / source_rate

def c():
    input("🔥 Press Enter To Continue....")

def coins(coin):
    if coin == "USD":
        return 1.0
    elif coin == "SAR":
        return 3.75
    elif coin == "EGP":
        return 50.72
    elif coin == "SDG":
        return 600.5

clear()
print("\n\t\t{------- 💰 Welcome to 'Currency Converter' 💱 -------}-")

while True:
    print()
    print("""
    |.======================[ O_M_A_R_C_O_U_N_T_R_Y ]=======================.|
    ||%&%&%&%_    _        _ _ _   _ _  _ _ _     _       _    _  %&%&%&%&||
    ||%&.-.&/||_||_ | ||\||||_| \ (_ ||\||_(_  /\|_ |\|V||_|)|/ |\ %&.-.&&||
    ||&// |\ || ||_ \_/| ||||_|_/ ,_)|||||_,_) \/|  ||| ||_|\|\_|| &// |\%||
    ||| | | |%               ,-----,-'____'-,-----,               %| | | |||
    ||| | | |&% \"\"\"\"\"\"\"\"\"\"  [    .-;\"`___ `\";-.    ]             &%| | | |||
    ||&\===//                `).'' .'`_.- `. '.'.(`  A 76355942 J  \\===/&||
    ||&%'-'%/1                // .' /`     \    \\                  \%'-'%||
    ||%&%&%/`   d8888b       // /   \  _  _;,    \\      .-\"\"\"-.  1 `&%&%%||
    ||&%&%&    8P |) Yb     ;; (     > a  a| \    ;;    //A`Y A\\    &%&%&||
    ||&%&%|    8b |) d8     || (    ,\   \ |  )   ||    ||.-'-.||    |%&%&||
    ||%&%&|     Y8888P      ||  '--'/`  -- /-'    ||    \\_/~\_//    |&%&%||
    ||%&%&|                 ||     |\`-.__/       ||     '-...-'     |&%&%||
    ||%%%%|                 ||    /` |._ .|-.     ||                 |%&%&||
    ||%&%&|  A 76355942 J  /;\ _.'   \  } \  '-.  /;\                |%&%&||
    ||&%.-;               (,  '.      \  } `\   \'  ,)   ,.,.,.,.,   ;-.%&||
    ||%( | ) 1  \"\"\"\"\"\"\"   _( \  ;...---------.;.; / )_ ```\"\"\"\"\"\"\" 1 ( | )%||
    ||&%'-'==================\`------------------`/=================='-'%&||
    ||%&JGS&%&%&%&%%&%&&&%&%%&) O N E  D O L L A R (%&%&%&%&%&%&%%&%&&&%&%%&||
    '\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"`
    """)

    print("""
        ===============
        | USD: $1.0   | 💵
        | SAR: $3.75  | 🇸🇦
        | EGP: $50.72 | 🇪🇬
        | SDG: $600.5 | 🇸🇩
        ===============
    """)

    c()
    clear()

    user_coin = input("💱 Choose a Currency to Convert from: ").strip().upper()

    if user_coin.isalpha():
        if user_coin == "USD" or user_coin == "SAR" or user_coin == "EGP" or user_coin == "SDG":
            while True:
                clear()

                amount = input("💰 Enter the amount: ").strip()

                if amount.isdigit():
                    amount = float(amount)

                    confirm = input(
                        f"📝 You entered {amount} {user_coin}. Confirm? (Y/N): "
                    ).strip().lower()

                    if confirm == "y":
                        while True:
                            clear()
                            convert_to = input(
                                "💱 Choose a Currency to Convert to: "
                            ).strip().upper()

                            if convert_to == "USD" or convert_to == "SAR" or convert_to == "EGP" or convert_to == "SDG":

                                print("🔍 Analyzing your request... Please wait.")
                                time.sleep(2)

                                print(
                                    f"💱 Checking for {convert_to}'s best rates available ..... Please wait...."
                                )
                                time.sleep(2)

                                print(
                                    f"💰 Getting a discount price for {user_coin}..... Please wait...."
                                )
                                time.sleep(2)

                                clear()

                                print(
                                    f"💼 Preparing the deal from {user_coin} to {convert_to}.... Please wait...."
                                )
                                time.sleep(2)

                                number_of_coin = coins(user_coin)
                                number_of_coin_to = coins(convert_to)

                                exchange_rate = calculate_converter(
                                    amount,
                                    number_of_coin,
                                    number_of_coin_to
                                )

                                print(
                                    f"💱 Exchange Rate: 1 {user_coin} = "
                                    f"{round(number_of_coin_to / number_of_coin,2)} {convert_to}"
                                )

                                print(
                                    f"💰 {amount} {user_coin} is equal to "
                                    f"{round(exchange_rate,2)} {convert_to}"
                                )

                                accept = input(
                                    f"✅ Do you Want to convert another currency from {user_coin}? (Y/N): "
                                ).strip().lower()

                                if accept == "y":
                                    continue

                                else:
                                    print("❌ Canceled.")
                                    print()

                                    anohter = input(
                                        "🔄 Do you want to perform another conversion? (Y/N): "
                                    ).strip().lower()

                                    break

                            else:
                                print(
                                    "❌ Invalid Choice... just (USD, SAR, EGP, SDG)"
                                )
                                c()
                        break

                    else:
                        continue

                else:
                    print("❌ Amount should be a number")
                    c()

            if anohter != "y":
                break
            else:
                continue

        else:
            print("❌ Invalid Choice... just (USD, SAR, EGP, SDG)")
            c()

    else:
        print("❌ Please Enter Letters")
        c()

