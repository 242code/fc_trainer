# This contains all funktions for adding flash cards (fc)

import general_funktions
import datetime

def get_q_a_s_input():
    # Instructs the user to input a question, an answer and a set.
    general_funktions.print_overline("Please enter a question")
    question = input()
    general_funktions.print_overline("Please enter the answer")
    answer = input()
    general_funktions.print_overline("Please enter the set")
    set = input()
    return question, answer, set

def add_date_to_fc(list):
    # Takes a new fc list ([question, answer, set]) and adds the
    # date of creation as "dd.mm.yyyy".
    today = datetime.datetime.now()
    date_to_add = today.strftime("%d.%m.%Y")
    list.append(date_to_add)
    return list   

def get_fc_to_add():
    # This stores multible new fc list to append them to a csv file.
    list_of_new_fc = []
    while True:
        new_fc = get_q_a_s_input()
        list_of_new_fc.append(new_fc)
        general_funktions.print_overline("Do you want to add another fc?")