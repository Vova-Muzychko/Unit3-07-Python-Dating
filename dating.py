#!/usr/bin/env python3

# Created by: Vova
# Created on: 27 October 2026
# This program checks if a user is eligible to date a grandchild
# based on their age using compound boolean operators.

# Constants for age boundaries
MIN_AGE = 25
MAX_AGE = 40


def main():
    # Get user input for age as a string
    age_string = input("Enter your age: ")

    # Error handling for non-integer inputs
    try:
        age_integer = int(age_string)

        # Check compound condition using logical AND
        if age_integer > MIN_AGE and age_integer < MAX_AGE:
            print("You can date their grandchild")
        else:
            print("You cannot date their grandchild")

    except ValueError:
        print("Invalid input! Please enter a valid integer age.")


if __name__ == "__main__":
    main()
