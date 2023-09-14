#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return 0, "None"
    else: 
        len = len(sentence)
        f = sentence[0]
        return len, f
