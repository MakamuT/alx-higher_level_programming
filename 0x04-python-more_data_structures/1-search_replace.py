#!/usr/bin/python3
def search_replace(my_list, search, replace):
    s = my_list[:]
    for n in range(len(my_list)):
        if s[n] is search:
            s[n] = replace
    return (s)
