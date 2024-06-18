import random

while True:
    level = input("Level: ")
    if level.isnumeric():
        level = int(level)
        if level > 0:
            value = random.randint(1, level)
            while True:
                guess = input("Guess: ")
                if guess.isnumeric():
                    guess = int(guess)
                    if guess > value:
                        print("Too large!")
                    elif guess < value:
                        print("Too small!")
                    else:
                        print("Just right!")
                        break
            break
        elif level == 0:
            continue
        else:
            break
