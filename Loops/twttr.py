phrase = input("Input: ")

for letter in phrase:
    if letter.lower() not in ["a","e","i","o","u"]:
        print(letter, end="")
