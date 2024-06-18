import inflect

p = inflect.engine()

list = []

try:
    while True:
        user_input = input("Name: ").title()
        list.append(user_input)
except EOFError:
    print("Adieu, adieu, to " + p.join(list))
