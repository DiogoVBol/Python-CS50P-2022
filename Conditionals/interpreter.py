expression = input("Expression: ").strip()

x, y, z = expression.split(" ")
x = float(x)
z = float(z)

if y == "+":
    print("{:.1f}".format(x + z))
elif y == "-":
    print("{:.1f}".format(x - z))
elif y == "/":
    print("{:.1f}".format(x / z))
elif y == "*":
    print("{:.1f}".format(x * z))
else:
    print("Error")
