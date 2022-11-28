#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Nov 2022
# This program converts the temperature from celsius to fahrenheit


def fahrenheit():
    try:
        temp_celsius = int(input("Enter the degrees in celsius: "))
        temp_fahrenheit = (9 / 5) * temp_celsius + 32
        print("\nThe temperature is {0} fahrenheit.".format(temp_fahrenheit))
    except Exception:
        print("\n This is an invalid input. Please try again")
    finally:
        print("\nDone.")


def main():
    # this function just calls other functions

    # call functions
    fahrenheit()


if __name__ == "__main__":
    main()
