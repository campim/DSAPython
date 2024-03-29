# shell_sort algorithm - python version
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


# create random list
def create_list(top, quantity):
    global my_list
    my_list = [random.randrange(1, top, 1) for _ in range(quantity)]


def shell_sort():
    global iterations
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = len(my_list) // 2
    while interval > 0:
        for i in range(interval, len(my_list)):
            temp = my_list[i]
            j = i
            while j >= interval and my_list[j - interval] > temp:
                iterations += 1
                my_list[j] = my_list[j - interval]
                j -= interval

            my_list[j] = temp
        interval //= 2


if __name__ == "__main__":
    print("*** classic shell sort ordering algorithm version  - written in Python *** ")

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

    print("before the shell sort  : ", my_list)
    print("  ")
    shell_sort()
    print("after the shell sort   : ", my_list)
    print("  ")
    print("iterations of the algorithm : ", iterations)
    print("  ")


