def main():
    plate = input("Plate: ")
    if is_valid(plate) and number_char(plate) and last_char(plate) and is_zero(plate) and diff_digit(plate):
        print("Valid")
    else:
        print("Invalid")

# “All vanity plates must start with at least two letters.”
def is_valid(s):
    if s[0:2].isnumeric():
        return False
    else:
        return True

# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def number_char(s):
    if len(s) > 6 or len(s) < 2:
        return False
    else:
        return True

# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.”
def last_char(s):
    return s.rstrip('0123456789').isalpha()

# "The first number used cannot be a ‘0’."
def is_zero(s):
    for character in s:
        if character.isnumeric():
            return character != "0"
    return True

# “No periods, spaces, or punctuation marks are allowed.”
def diff_digit(s):
    if s.isalnum():
        return True
    else:
        return False
main()
