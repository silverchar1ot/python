sales = float(input("Enter sales: $"))
gift = 0
while sales > 0:
    if sales < 1000:
        gift = sales * 0.1
        print("you will get 10% gift.the gift you get :{:.2f}".format(gift))
    if sales >= 1000:
        gift = sales * 0.15
        print("you will get 15% gift.the gift you get :{:.2f}".format(gift))
    sales = float(input("Enter sales: $"))
print("this number is not valid")
