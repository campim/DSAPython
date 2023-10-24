# linear search  - simple - python version
# Author Daniel G. Campos (2023)

# LICENSING
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation; either version 2 of the License, or (at your option)
# any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
import random

# global variables
my_list = []
iterations = 0


def create_list(top, quantity):
    global my_list
    my_list = [random.randrange(1, top, 1) for _ in range(quantity)]


def linear_search(value):
    global iterations
    # search every item
    for i in range(0, len(my_list)):
        iterations += 1
        if my_list[i] == value:
            return i

    return -1


if __name__ == "__main__":
    print("*** linear search - simple - written in Python *** ")

    search_value = 0
    while search_value == 0 or search_value > 50:
        try:
            search_value = int(input("Please enter an integer to search for up to 50 (for this demo) :"))
        except ValueError:
            print("Please enter only integers")

    create_list(50, 50)  # we create up to 50 items to search for the entered value

    print("random generated numbers are : ", my_list)

    result = linear_search(search_value)

    if result > 0:
        print("search value is found! at index.", iterations)
    else:
        print("search value not found.")

    print("iterations of the algorithm : ", iterations)
    print("  ")

