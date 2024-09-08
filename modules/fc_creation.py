# This contains all functions for adding flash cards (fc)


import datetime
import csv
from modules import general_functions


def get_q_a_s_input(): #TODO: That method name makes no apparent sense, its always better to have a too wordy name than one that cannot be easily understood
    # Instructs the user to input a question, an answer and an origin.
    general_functions.print_overline("Please enter a question")
    question = general_functions.multiline_input()
    general_functions.print_overline("Please enter the answer")
    answer = general_functions.multiline_input()
    general_functions.print_overline("Please enter the origin")
    origin = general_functions.multiline_input()
    new_fc = [question, answer, origin] #TODO: No need to initialize variable for one time use
    return new_fc


def add_stage_to_fc(lst):
    # Add the stage 0 to a new fc list ([question, answer, set]) #TODO This comment uses set, even though before it was origin, and to be honest up to here I assumed s stood for source. If in doubt, explain too much
    # TODO Also what even is a stage in this context.
    lst.append(0) #TODO This entire method just appends an object to a list, it is not necessary to make that an extra method
    return lst #TODO: also lst is very generic and at least "list" would make it clear that its not an abbreviation to mean e.g. "latest set transformed" which could be thought by an already confused developer
# TODO: It is always a good rule to think that code should be understandable for the dumbest new trainee who just learned reading code a week ago.


def add_date_to_fc(lst):
    # Takes a new fc list ([question, answer, set, stage]) and adds the #TODO it might still not be set but origin
    # date of creation as "dd.mm.yyyy" as that is the date of the next quiz.
    today_datetime = datetime.datetime.now()
    today_str = today_datetime.strftime("%d.%m.%Y") #TODO: can be one line with the previous and even the next two
    lst.append(today_str)
    return lst   


def get_fc_to_add():
    # This stores multiple new fc list to append them to a csv file.
    list_of_new_fc = []
    while True:
        new_fc = get_q_a_s_input()
        new_fc = add_stage_to_fc(new_fc)
        new_fc = add_date_to_fc(new_fc)
        list_of_new_fc.append(new_fc) #TODO These four lines could be a oneliner by not always using the variable new_fc
        general_functions.print_overline(
            "Do you want to add another fc? ('n' to stop)")
        answer = input() #TODO: no need for initialising a variable
        if answer.lower() == "n": #TODO: Breaking Condition should be put in cycle head
            break
        else: #TODO: this and the next line are not needed, because the cycle should already continue when this part is reached.
            continue
    return list_of_new_fc


def save_new_fcs(lst, set_name): #TODO lst is not a clear name
    set_name = set_name + ".csv" #TODO think about making the extension a sort of variable, maybe in a config script to make a possible change to a different file extension easier
    fc_set_file = open(f"./fc_sets/{set_name}", "a") #TODO There is no reason to not have the previous line instead of setting it to a variable
    fc_writer = csv.writer(fc_set_file)
    for new_fc in lst:
        fc_writer.writerow(new_fc)
    fc_set_file.close()
    return None #TODO delete that line, or is there a reason behind it.


def create_fcs():
    # Guides the user through set selection and creation, then saves all fc.
    existing_sets = general_functions.get_existing_sets()
    print("Which set do you want to append/create?")
    print("The following sets already exist:") #TODO a multiline output does need to be split up onto several print commands, better perhaps "'''"
    print(", ".join(existing_sets))
    print() # TODO replace with \n in previous print
    set_name = input()
    fc_to_add_list = get_fc_to_add()
    save_new_fcs(fc_to_add_list, set_name)
    fc_added = []
    for fcs in fc_to_add_list:
        fc_added.append(fcs[0])
    print(f"The following {len(fc_added)}fc have been added to {set_name}")
    print(",\n".join(fc_added))
    print() #TODO: replace by adding a \n to the previous line
    