def main():
    hours = input("What time is it? ")
    hours = convert(hours)
    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = map(int, time.split(':'))

    fractional_hours = minutes / 60

    total_hours = hours + fractional_hours

    return total_hours

if __name__ == "__main__":
    main()
