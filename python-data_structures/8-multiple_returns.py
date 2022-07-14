#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    if sentence == "":
        return 0,None
    else:
        return l, sentence[0]
