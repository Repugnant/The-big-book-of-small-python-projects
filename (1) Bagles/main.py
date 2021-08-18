"""
Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
View this code at https://nostarch.com/big-book-small-python-projects
A version of this game is featured in the book "Invent Your Own
Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle
"""

"""
File: `vim_snippets#Filename('$1.py', 'foo.py')`
Author: `g:snips_author`
Email: `g:snips_email`
Github: `g:snips_github`
Description: 
"""


from random import choice
from sys import exit as sys_exit


def get_secret_num(length):
    """ Returns a non-repeated-digits number"""
    secret_num = ""
    nums = list(range(10))

    while len(secret_num) < length:
        num = str(choice(nums))

        if num not in secret_num:
            secret_num += num

    return secret_num


def get_clues(guess, secret_num):
    """Returns a string with the pico, fermi, bagels clues for a guess"""

    if guess == secret_num:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("Fermi")

        elif guess[i] in secret_num:
            clues.append("Pico")

    if len(clues) == 0:
        return "Bagles"

    return " ".join(sorted(clues))


def main():
    """Main function"""
    NUM_DIGITS = 3
    MAX_GUESSES = 10

    secret_num = get_secret_num(NUM_DIGITS)
    num_guesses = 0

    # Play
    print(f"I have thought up a {NUM_DIGITS} digits number.")
    print(f"You have {MAX_GUESSES} guesses to get it")

    while num_guesses <= MAX_GUESSES:
        guess = ""

        while len(guess) != NUM_DIGITS or not guess.isdecimal():
            print(f"\nGuess #{num_guesses}")
            guess = input("> ")

        clues = get_clues(guess, secret_num)
        print(clues)

        num_guesses += 1

        if guess == secret_num:
            break

    else:
        print('You ran out of guesses.')
        print('The answer was {}.'.format(secret_num))

    # Play again
    play_again = input("\nDo you wanna play again? (y, n): ").lower()

    if play_again == "y":
        main()

    elif play_again == "n":
        sys_exit(0)

    else:
        print("Wrong answer. Exiting...")
        sys_exit(-1)


if __name__ == "__main__":
    main()
