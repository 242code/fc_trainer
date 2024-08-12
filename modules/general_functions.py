# Contains funktions that are used in multiple modules.

import os

def print_overline(text):
    print("------------------")
    print(text)

def get_existing_sets():
    # Returns the names of existing sets saved in "./fc_sets" without ".csv".
    existing_sets = os.listdir("./fc_sets")
    for num, name in enumerate(existing_sets):
        existing_sets[num] = name[:-4]
    return existing_sets

def multiline_input():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    return "\n".join(lines)