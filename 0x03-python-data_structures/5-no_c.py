#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        if my_string[i] != "c" or my_string[i] != "C":
            new_string += my_string[i]
    return new_string
