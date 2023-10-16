# quick sort - python version - divide and conquer approach using recursion and rightmost element as pivot
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


# function to find the partition position
def partition(low, high):
    global iterations
    # choose the rightmost element as pivot
    pivot = my_list[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements - compare each element with pivot -
    for j in range(low, high):
        if my_list[j] <= pivot:
            iterations += 1
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            # swapping element at i with element at j
            (my_list[i], my_list[j]) = (my_list[j], my_list[i])

    # swap the pivot element with the greater element specified by i
    (my_list[i + 1], my_list[high]) = (my_list[high], my_list[i + 1])

    # return the position from where partition is done
    return i + 1


def quicksort(low, high):
    global iterations
    if low < high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(low, high)

        # recursive call on the left of pivot
        quicksort(low, pi - 1)

        # recursive call on the right of pivot
        quicksort(pi + 1, high)


if __name__ == "__main__":
    print("*** Quick sort algorithm - using rightmost element as pivot - written in Python - *** ")
    print("*** Ascending order by default for this demo *** ")

    top_limit = 0
    while top_limit == 0 or top_limit > 50:
        try:
            top_limit = int(input("Please enter an integer up to 50 (for this demo) for the integer limit :"))
        except ValueError:
            print("Please enter only integers")

    create_list(top_limit, top_limit)

    print("before the quick sort : ", my_list)
    print("  ")
    quicksort(0, len(my_list)-1)
    print("after the quick sort  : ", my_list)
    print("  ")
    print("iterations of the algorithm : ", iterations)
    print("  ")
