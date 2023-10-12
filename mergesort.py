# merge sort - python version
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


def mergesort(my_array):
    global iterations
    if len(my_array) > 1:

        #  r is the point where the array is divided into two subarrays - merge sort algorithm
        r = len(my_array) // 2
        L = my_array[:r]
        M = my_array[r:]

        # Sort the two halves - recursive -
        mergesort(L)
        mergesort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among elements L and M and
        # place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                iterations += 1
                my_array[k] = L[i]
                i += 1
            else:
                iterations += 1
                my_array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            iterations += 1
            my_array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            iterations += 1
            my_array[k] = M[j]
            j += 1
            k += 1


if __name__ == "__main__":
    print("*** Merge sort ordering algorithm version  - written in Python *** ")

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

    print("before the merge sort : ", my_list)
    print("  ")
    mergesort(my_list)
    print("after the merge sort  : ", my_list)
    print("  ")
    print("iterations of the algorithm : ", iterations)
    print("  ")
