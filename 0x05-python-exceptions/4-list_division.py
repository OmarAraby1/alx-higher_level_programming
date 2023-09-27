#!/usr/bin/python3
res = []
def list_division(my_list_1, my_list_2, list_length):
    for i range(0, list_length):
        try:
            res[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            res[i] = 0.0
        except TypeError:
            print("wrong type")
            res[i] = 0.0
        except IndexError:
            print("out of range")
            res[i] = 0.0
    return (res)
