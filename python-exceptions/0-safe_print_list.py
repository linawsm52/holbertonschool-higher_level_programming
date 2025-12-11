#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    addition = 0
    for element in my_list:
        addition += 1
    i = 0
    try:
        while i < x:
            print(my_list[i], end='')
            i += 1
        print('\n', end='')
        return x
    except IndexError:
        if i < addition:
            while my_list[i]:
                print(my_list[i], end='')
                i += 1
        else:
            pass
        print('\n', end='')
        return addition
