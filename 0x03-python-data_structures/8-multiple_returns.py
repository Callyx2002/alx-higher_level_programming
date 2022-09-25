#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        first = None
        counting = 0
    else:
        sentence = list(sentence)
        counting = len(sentence)
        new = str(sentence[0])
        first = new[0]
    return counting, first
