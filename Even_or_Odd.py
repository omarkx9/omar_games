# اطبع للمستخدم رساله ترحيب
print("\n\t-------Welcome to Even or Odd-------")
# اطلب من المستخدم اخال رقم وخزنه في متغير
number = int(input('Enter a number: '))
# تتحقق ما اذا كان الرقم زوجي
if number % 2 == 0:
    # اطبع للمستخدم رقمه و انه زوجي
    print(f"{number} is Even")
# تحقق ما اذا كان الرقم فردي
else:
    #اطبع للمستخدم رقمه وانه فردي
    print(f"{number} is Odd")