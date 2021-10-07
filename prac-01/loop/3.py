num = int(input("stars:"))
while num > 0:
    for num in range(0, num, 1):
        print("*",end=' ')
    num = int(input("stars:"))