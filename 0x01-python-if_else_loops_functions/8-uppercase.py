#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            letter = ord(letter) - 32
            print("{}".format(chr(letter)), end="")
        else:
            print("{}".format(letter), end="")
