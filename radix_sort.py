# radix sort - python version -
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


# counting sort, cumulative array algorithm for sorting
def counting_sort(arr1):
    global iterations
    output = [0] * len(arr1)

    # Initialize count array, this is for the cumulative array
    count = [0] * len(arr1)

    # Store the count of each element in count array
    for i in range(0, len(arr1)):
        iterations += 1
        index = arr1[i]
        count[index % len(arr1)] += 1

    # Store the cumulative count
    for i in range(1, len(arr1)):
        iterations += 1
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = len(arr1) - 1
    while i >= 0:
        iterations += 1
        index = arr1[i]
        output[count[index % len(arr1)] - 1] = arr1[i]
        count[index % len(arr1)] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, len(arr1)):
        arr1[i] = output[i]


# radix sort
def radix_sort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        counting_sort(array)
        place *= 10


if __name__ == "__main__":
    print("*** radix sort ordering algorithm version  - written in Python - *** ")

    top_limit = 0
    while top_limit == 0 or top_limit > 50:
        try:
            top_limit = int(input("Please enter an integer up to 50 for the max item and value for the list :"))
        except ValueError:
            print("Please enter only integers")

    create_list(top_limit, top_limit)

    print("before the radix sort : ", my_list)
    print("  ")
    radix_sort(my_list)
    print("after the radix sort  : ", my_list)
    print("  ")
    print("iterations of the algorithm : ", iterations)
    print("  ")
