# bubble sort optimized - python version
# Author Daniel G. Campos (2022)
# in bubble sort optimized we use a variable to check if the swap has been made, in that case we follow the loop,
# and so we save in iterations. We create random numbers and the list is shorted up to the user criteria

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


def bubble_sort():
    # loop through each element of my_list
    global iterations
    for i in range(len(my_list)):
        iterations += 1
        # keep track of swapping
        swapped = False

        # loop to compare my_list elements
        for j in range(len(my_list) - i - 1):
            iterations += 1
            # compare two adjacent elements
            # change > to < to sort in descending order
            if my_list[j] > my_list[j + 1]:
                # swapping occurs if elements
                # are not in the intended order
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp

                swapped = True

        # no swapping means the my_list is already sorted
        # so no need for further comparison
        if not swapped:
            break


if __name__ == "__main__":
    print("*** classic bubble sort optimized version  - written in Python *** ")

    top_limit = 0
    while top_limit == 0 or top_limit > 50:
        try:
            top_limit = int(input("Please enter an integer up to 50 (for this demo) for the integer limit :"))
        except ValueError:
            print("Please enter only integers")

    quantity_items = 0
    while quantity_items == 0 or quantity_items > 20:
        try:
            quantity_items = int(input("Please enter an integer up to 20 (for this demo) for the amount of items :"))
        except ValueError:
            print("Please enter only integers")

    create_list(top_limit, quantity_items)

    print("before the bubble sort optimized : ", my_list)
    bubble_sort()
    print("after the bubble soft optimized  : ", my_list)
    print("iterations of the algorithm : ", iterations)

