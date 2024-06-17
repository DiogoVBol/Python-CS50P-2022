while True:
    try:
        value = input("Fraction: ").strip()
        x, y = value.split('/')
        if int(x) <= int(y):
            percent = (int(x)/int(y))*100
            if percent <= 1:
                print("E")
            elif percent >= 99:
                print("F")
            else:
                print("{:.0f}%".format(percent))
            break
        else:
            ValueError
    except (ValueError, ZeroDivisionError):
        pass
