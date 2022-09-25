#!/usr/bin/python3
def multiple_returns(sentence):
    sentence = list(str(sentence))
    counting = len(sentence)
    new = str(sentence[0])
    if sentence == "":
        first = None
    else:
        first = new[0]
    return counting, first
