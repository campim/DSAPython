# selection sort - python version
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


def selection_sort(order):
    global iterations

    for step in range(len(my_list)):
        iterations += 1
        min_idx = step

        for i in range(step + 1, len(my_list)):
            iterations += 1
            # algorithm can change in descending or ascending order
            if order == 1 and my_list[i] < my_list[min_idx] or order != 1 and my_list[i] > my_list[min_idx]:
                min_idx = i
        # put min at the correct position
        (my_list[step], my_list[min_idx]) = (my_list[min_idx], my_list[step])


if __name__ == "__main__":
    print("*** classic selection sort - written in Python - *** ")
    which_order = 0  # ascending or descending order
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

    answer = 0
    while answer == 0:
        try:
            which_order = int(input("Please select which order to sort : 1=ascending  2=descending (default is 1) :"))
            if which_order > 2 or which_order < 1:
                raise ValueError
            else:
                answer = 1
        except ValueError:
            print("Please enter valid values ( 1 or 2 )")

    create_list(top_limit, quantity_items)

    print("before the selection sort : ", my_list)
    print("  ")
    selection_sort(which_order)
    print("after the selection soft  : ", my_list)
    print("  ")
    print("iterations of the algorithm : ", iterations)
    print("  ")
