#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: May 2021
# This program guesses your number
#    with numbers inputted from the user

import constants


def main():
    # This function guesses your number

    # input
    guessed_number = int(input("Enter the number between 0 - 9: "))
    print("")

    # process/output
    if guessed_number == 5:
        print("You guessed correct!")
    if guessed_number != 5:
        print("You guessed wrong!")
    print("\nDone.")


if __name__ == "__main__":
    main()
