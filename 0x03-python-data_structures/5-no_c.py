#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)
    m = 0
    new_string = my_string[:]
    for n in range(length):
        if (my_string[n] == 'c' or my_string[n] == 'C'):
            new_string = new_string[:(n - m)] + my_string[:(n + 1):]
            m += 1
    return (new_string)
