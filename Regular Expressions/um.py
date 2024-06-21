import re


def main():
    print(count(input("Text: ")))

def count(s):
    regex = "(^|\W)um($|\W)"
    value = re.findall(regex, s, re.IGNORECASE)
    if value:
        return(len(value))


if __name__ == "__main__":
    main()
