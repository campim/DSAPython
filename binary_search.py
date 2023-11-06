# binary search  - simple - python version
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


def binary_search(value, low, high, i_or_r):
    global iterations
    if i_or_r == "i":
        while low <= high:
            iterations += 1
            mid = low + (high - low) // 2
            if my_list[mid] == value:
                return mid
            elif my_list[mid] < value:
                low = mid + 1
            else:
                high = mid - 1
    elif i_or_r == "r":
        if high >= low:
            iterations += 1
            mid = low + (high - low) // 2
            # If found at mid, then return it
            if my_list[mid] == value:
                return mid
            # Search the left half
            elif my_list[mid] > value:
                return binary_search(value, low, mid - 1, "r")
            # Search the right half
            else:
                return binary_search(value, mid + 1, high, "r")
    return -1


if __name__ == "__main__":
    print("*** binary search algorithm - written in Python -     *** ")
    print("*** using quick sort as ordering algorithm            *** ")
    print("*** Binary search can be implemented only on a sorted *** ")
    print("*** list of items.If the elements are not sorted      *** ")
    print("*** already, we need to sort them first. Also, we can *** ")
    print("*** choose to use iterative or recursive method.      *** ")

    search_value = 0
    while search_value == 0 or search_value > 50:
        try:
            search_value = int(input("Please enter an integer to search for up to 50 (for this demo) :"))
        except ValueError:
            print("Please enter only integers")

    create_list(50, 50)  # we create up to 50 items to search for the entered value

    inter_or_recursive = "i"  # by default, we use interactive method
    while True:
        inter_or_recursive = input("Please enter which method to use (i=iterative (default) r=recursive):").lower()
        if inter_or_recursive == "i":
            print("using iterative method for binary search.")
            break
        elif inter_or_recursive == "r":
            print("using recursive method for binary search.")
            break
        else:
            print("Please enter only two possible values")

    print("random list created before the quick sort : ", my_list)
    print("  ")
    quicksort(0, len(my_list)-1)
    print("random list ordered with quick sort       : ", my_list)
    print("  ")
    print("iterations of the quick sort algorithm    : ", iterations)
    print("  ")

    iterations = 0

    result = binary_search(search_value, 0, (len(my_list)-1), inter_or_recursive)

    if result != -1:
        print("Element is present at index " + str(result))
    else:
        print("Element Not found at present list")

    print("iterations of the binary search algorithm : ", iterations)
    print("  ")
