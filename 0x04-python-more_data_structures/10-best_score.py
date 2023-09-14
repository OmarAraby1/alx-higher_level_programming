#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    k = list(a_dictionary.keys())[0]
    mx = a_dictionary[k]
    for key, val in a_dictionary.itmes():
        if val > mx:
            mx = val
            k = key
    return k
