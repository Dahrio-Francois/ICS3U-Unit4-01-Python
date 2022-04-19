#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Sep 2020
# This program uses a while loop


def main():
    # this function uses a while loop

    # this is to keep track of hw many times you go through the loop
    loop_counter = 0
    calculation = 0

    # input
    positive_integer = input("Enter in an integer: ")
    try:
        positive_integer_int = int(positive_integer)

        # process & output
        print("\n", end="")
        while loop_counter <= positive_integer_int:
            calculation = calculation + loop_counter
            loop_counter = loop_counter + 1
    except Exception:
        print("\nThis was not an integer.")
    finally:
        print("The sum of those numbers is {}".format(calculation))
        print("\nDone")


if __name__ == "__main__":
    main()
