print("Amount Due: 50")

n = 50
while n > 0:
    p = int(input("Insert Coin: "))
    n = n - p
    if p == 25 or p == 10 or p == 5:
        if n > 0:
            print("Amount Due: {}".format(n))
        else:
            break
    else:
        print("Amount Due: 50")
print("Change Owed: {}".format(abs(n)))
