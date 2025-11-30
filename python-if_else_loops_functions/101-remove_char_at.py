#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    new = ""
    for i in range(len(str)):
        if i != n:
            new += str[i]
    return new
