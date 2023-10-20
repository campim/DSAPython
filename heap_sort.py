# heap sort - complete binary tree - python version
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


def heapify(n, i):
    global iterations
    # Find largest among root and children
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and my_list[i] < my_list[left]:
        largest = left

    if right < n and my_list[largest] < my_list[right]:
        largest = right

    # If root is not largest, swap with largest and continue
    if largest != i:
        iterations += 1
        my_list[i], my_list[largest] = my_list[largest], my_list[i]
        heapify(n, largest)


def heap_sort():
    global iterations
    n = len(my_list)

    # Build max heap
    for i in range(n // 2, -1, -1):
        heapify(n, i)

    for i in range(n - 1, 0, -1):
        # Swap
        iterations += 1
        my_list[i], my_list[0] = my_list[0], my_list[i]

        # Heapify root element
        heapify(i, 0)


if __name__ == "__main__":
    print("*** heap sort - binary tree algorithm - written in Python *** ")

    top_limit = 0
    while top_limit == 0 or top_limit > 50:
        try:
            top_limit = int(input("Please enter an integer up to 50 (for this demo) for the integer limit :"))
        except ValueError:
            print("Please enter only integers")

    create_list(top_limit, top_limit)

    print("before the heap sort : ", my_list)
    print("  ")
    heap_sort()
    print("after the heap sort  : ", my_list)
    print("  ")
    print("iterations of the algorithm : ", iterations)
    print("  ")
