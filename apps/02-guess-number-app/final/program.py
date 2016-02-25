import random


def run_game():
    print("Guess my number game.")
    number = random.randint(0, 100)
    guess = -1

    while not guess == number:
        guess_text = input("Guess a number between 0 and 100: ")
        guess = int(guess_text)
        if guess < number:
            print("Sorry but {0} is LOWER than the number".format(guess))
        elif guess > number:
            print("Sorry but {0} is HIGHER than the number".format(guess))
        else:
            print("YES! You've got it. The number was {}".format(guess))


def print_header():
    print("---------------------------------------------------------------")
    print("         GUESS A NUMBER APP - demonstrates: ")
    print("         * Shape of app (whitespace) ")
    print("         * Basic methods ")
    print("         * Booleans ")
    print("         * Type conversion ")
    print("         * Import module ")
    print("         * If ")
    print("         * While ")
    print("         * Empty blocks / suites ")
    print("         * String format ")
    print("---------------------------------------------------------------")
    print()


def main():
    print_header()
    run_game()


main()
