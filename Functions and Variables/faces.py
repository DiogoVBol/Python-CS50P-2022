# Input and using function convert()
def main():
    x = input("Say something: ")

    result = convert(obj = x)

    print(result)

# Create a function who replace ":(" and ":)" to emoticon
def convert(obj):
    emoji = obj.replace(":(", "🙁").replace(":)","🙂")
    return emoji

main()
