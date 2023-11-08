# simple stack of integers - python version -
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
my_stack = []

# we implement a simple stack of integers using Last In First Out (LIFO) principle.
# These are the basic operations for a stack : Push, Pop, IsEmpty, IsFull, Peek


def create_list(my_top, quantity):
    global my_stack
    my_stack = [random.randrange(1, my_top, 1) for _ in range(quantity)]


# checking empty stack
def check_empty():
    return len(my_stack) == 0


# checking full stack
def check_full():
    return len(my_stack) < 30


# Adding items into the stack
def push(item):
    my_stack.insert(len(my_stack)+1, int(item))
    print("pushed item: " + str(item))


# Removing an element from the stack
def pop():
    if check_empty():
        return "stack is empty"

    return my_stack.pop()


if __name__ == "__main__":
    answer = ""
    top = 50
    print("*** Simple stack implementation with python - ***")
    print("*** I create a simple random list of integers ***")
    print("*** and then we use push and pop to interact  ***")
    print("*** with it  - for this demo only 30 items -  ***")

    create_list(top, 30)

    print("list of integers created : ", my_stack)

    while answer != "q":
        answer = input("enter 'u' for push(we push random number), 'o' for pop , 'p' for peek  (q to quit):").lower()
        if answer == "u":
            # we check if stack is full - for this demo up to 30 items -
            if check_full():
                push(int(random.randrange(1, top, 1)))
                print("pushed random item, now stack is :", my_stack)
            else:
                print("stack is full, cannot push more items right now.")

        if answer == "o":
            # we check if stack is empty - for this demo up to 30 items -
            if check_empty():
                print("stack is empty, cannot pop more items right now.")
            else:
                pop()
                print("popped last item, now stack is :", my_stack)

        if answer == "p":
            # peek, we show last item on the stack
            if len(my_stack) > 0:
                print("last item on stack :", my_stack[len(my_stack)-1])
            else:
                print("no items on stack.")

    print("stack now is :", my_stack)
