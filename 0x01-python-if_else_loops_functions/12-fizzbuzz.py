#!/usr/bin/python3
def fizzbuzz():
    for i in range(0, 100):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            if i == 100:
                print("Buzz")
            else:
                print("Buzz", end=" ")
        else:
            print("{}".format(i), end=" ")
