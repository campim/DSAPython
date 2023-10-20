# bucket sort - python version
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


def insertion_sort(b):
    global iterations
    for i in range(1, len(b)):
        iterations += 1
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b


def bucket_sort():
    global iterations
    arr = []
    slots = 10  # at the beginning we give every bucket a 10 limit, we adjust this afterwards
    for i in range(slots):
        arr.append([])  # creates the buckets

    # Put array elements in different buckets
    for j in my_list:
        iterations += 1
        index_b = abs(int(j / 10))  # we divide by 10 so to get the values into their respective buckets
        arr[index_b].append(j)

    # Sort individual buckets with insertion sort
    for i in range(slots):
        arr[i] = insertion_sort(arr[i])

    # concatenate the result
    k = 0
    for i in range(slots):
        for j in range(len(arr[i])):
            iterations += 1
            my_list[k] = arr[i][j]
            k += 1
    return my_list


if __name__ == "__main__":
    print("*** bucket sort - with insertion sort as secondary algorithm - written in Python *** ")

    top_limit = 0
    while top_limit == 0 or top_limit > 50:
        try:
            top_limit = int(input("Please enter an integer up to 50 (for this demo) for the integer limit :"))
        except ValueError:
            print("Please enter only integers")

    create_list(top_limit, top_limit)

    print("before the bucket sort : ", my_list)
    print("  ")
    bucket_sort()
    print("after the bucket sort  : ", my_list)
    print("  ")
    print("iterations of the algorithm : ", iterations)
    print("  ")
