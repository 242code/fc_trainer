# Contains functions that are used in multiple modules. TODO: do not mix German and English unless absolutely necessary

import os
from os.path import exists


def print_overline(text): #TODO: I would call it print_under_line because I thought you meant exactly the opposite while quickly reading it, perhaps print_with_line_above
    print("------------------")
    print(text)

def get_existing_sets():
    # Returns the names of existing sets saved in "./fc_sets" without ".csv".
    if not exists("./fc_sets"):
        os.mkdir("./fc_sets")  #TODO: Otherwise the program has problems when starting without the fc_sets created.
    existing_sets = os.listdir("./fc_sets")
    for num, name in enumerate(existing_sets):
        #existing_sets[num] = name[:-4] #TODO: While currently functional, it would be better to cut any file extension, otherwise it would lead to confusion if you changed to json for example.
        existing_sets[num] = os.path.splitext(name)[0]
    return existing_sets

def multiline_input():
    lines = []
    while True: #TODO: Possibly do something like while input(), but I don't know for sure wether Python allows that, perhaps there are do-whiles?
        line = input()
        if line:
            lines.append(line)
        else:
            break
    return "\n".join(lines)