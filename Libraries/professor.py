import random


def main():
    n = get_level()
    score = 0
    for _ in range(10):
        fails = 0
        x, y = generate_integer(n), generate_integer(n)
        while True:
            if fails == 3:
                print(f"{x} + {y} = {x+y}")
                break
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                fails += 1
                print("EEE")
            else:
                if answer == x + y:
                    score += 1
                    break
                else:
                    fails += 1
                    print("EEE")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n not in [1, 2, 3]:
                continue
        except ValueError:
            pass
        else:
            return n


def generate_integer(level):
    if level == 1:
        start = 0
        stop = 10
    else:
        start = 10 ** (level-1)
        stop = 10 ** level
    rand_int = random.randrange(start,stop,1)
    return rand_int


if __name__ == "__main__":
    main()
