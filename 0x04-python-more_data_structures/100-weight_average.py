#!/usr/bin/python3
def weight_average(my_list=[]):
    if not len(my_list):
        return 0
    sum = 0
    den = 0
    for tup in my_list:
        sum += tup[0] * tup[1]
        den += tup[1]
    return float(sum / den)
