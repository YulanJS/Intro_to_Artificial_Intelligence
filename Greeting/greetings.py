# -----------------------------------------------------------------------------
# Name:        greeting
# Purpose:     A gentle introduction to Python
#
# Author:      Rula Khayrallah
# -----------------------------------------------------------------------------
"""
A little Python program that prints a personalized greeting

Prompt the user for their name.
Print a customized Hello message.
"""


def do_stuff():
    print('Acting busy!')


def main():
    name = input('Please enter your name: ')  # Prompt user
    print('Hello', name)  # Print a personalized greeting


if __name__ == "__main__":
    main()
