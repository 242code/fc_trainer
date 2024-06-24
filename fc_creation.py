# This contains all funktions for adding flash cards (fc)

import general_funktions
import datetime
import csv

def get_q_a_s_input():
    # Instructs the user to input a question, an answer and a set.
    general_funktions.print_overline("Please enter a question")
    question = general_funktions.multiline_input()
    general_funktions.print_overline("Please enter the answer")
    answer = general_funktions.multiline_input()
    general_funktions.print_overline("Please enter the set")
    set = general_funktions.multiline_input()
    new_fc = [question, answer, set]
    return new_fc

def add_stage_to_fc(list):
    # Add the stage 0 to a new fc list ([question, answer, set])
    list.append(0)
    return list

def add_date_to_fc(list):
    # Takes a new fc list ([question, answer, set, stage]) and adds the
    # date of creation as "dd.mm.yyyy" as that is the date of the next quiz.
    today_datetime = datetime.datetime.now()
    today_str = today_datetime.strftime("%d.%m.%Y")
    list.append(today_str)
    return list   

def get_fc_to_add():
    # This stores multible new fc list to append them to a csv file.
    list_of_new_fc = []
    while True:
        new_fc = get_q_a_s_input()
        new_fc = add_stage_to_fc(new_fc)
        new_fc = add_date_to_fc(new_fc)
        list_of_new_fc.append(new_fc)
        general_funktions.print_overline(
            "Do you want to add another fc? ('n' to stop)")
        answer = input()
        if answer.lower() == "n":
            break
        else:
            continue
    return list_of_new_fc

def save_new_fcs(list, set):
    set = set+".csv"
    fc_set_file = open(f"./fc_sets/{set}", "a")
    fc_writer = csv.writer(fc_set_file)
    for new_fc in list:
        fc_writer.writerow(new_fc)
    fc_set_file.close()
    return None

def create_fcs():
    # Guides the user through set selection and creation, then saves all fc.
    existing_sets = general_funktions.get_existing_sets()
    print("Which set do you want to append/create?")
    print("The following sets allready exist:")
    print(", ".join(existing_sets))
    print()
    set_name = input()
    fc_to_add_list = get_fc_to_add()
    save_new_fcs(fc_to_add_list, set_name)
    fc_added = []
    for fcs in fc_to_add_list:
        fc_added.append(fcs[0])
    print(f"The following fc have been added to {set_name}")
    print(", ".join(fc_added))