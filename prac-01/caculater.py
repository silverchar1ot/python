num = int(input("how many things do you pick:"))
money: float = 0
for i in range(0, num, 1):
    pay = int(input("what is the price"))
    money += pay
if money < 100:
    print("you should pay:{:.2f} $".format(money))
if money >= 100:
    money = money * 0.9
    print("you should pay:{:.2f} $".format(money))
