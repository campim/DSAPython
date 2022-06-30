# bubble sort simple - python version
# Author Daniel G. Campos (2022)

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


def insertion_sort():
    global iterations
    for step in range(1, len(my_list)):
        iterations += 1
        key = my_list[step]
        j = step - 1

        while j >= 0 and key < my_list[j]:
            iterations += 1
            my_list[j + 1] = my_list[j]
            j = j - 1

        my_list[j + 1] = key


if __name__ == "__main__":
    print("*** classic bubble sort simple version  - written in Python *** ")

    top_limit = 0
    while top_limit == 0 or top_limit > 50:
        try:
            top_limit = int(input("Please enter an integer up to 50 (for this demo) for the integer limit :"))
        except ValueError:
            print("Please enter only integers")

    quantity_items = 0
    while quantity_items == 0 or quantity_items > 20:
        try:
            quantity_items = int(
                input("Please enter an integer up to 20 (for this demo) for the amount of items :"))
        except ValueError:
            print("Please enter only integers")

    create_list(top_limit, quantity_items)

    print("before the bubble sort optimized : ", my_list)
    print("  ")
    insertion_sort()
    print("after the bubble soft optimized  : ", my_list)
    print("  ")
    print("iterations of the algorithm : ", iterations)
    print("  ")
