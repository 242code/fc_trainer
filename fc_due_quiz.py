# Contains all funktions ot modify the set quiz to only ask due fcs.

import fc_quiz
import manage_quiz_date
import general_funktions
import datetime
import random

def date_str_to_datetime_obj(date_str):
    # This takes a date string (%d.%m.%Y) and returns a datetime objekt.
    date_obj = datetime.strptime(date_str, "%d.%m.%Y")
    return date_obj

def check_wether_fc_is_due(today, next_quiz_date):
    # This checks wether the next quiz date is in the furutre, then returns False,
    # else returns True.
    if today < next_quiz_date:
        return False
    else:
        return True

def quiz_due_fc_in_a_set(set_list):
    # Takes the set list of lists and iterates over the due dates of every
    # fc list and quizzes the user. Returns the updated list.
    today_dto = datetime.datetime.today()
    random.shuffle(set_list)
    for index, fc_list in enumerate(set_list):
        if check_wether_fc_is_due(today_dto, fc_list[4]):
            right_wrong = fc_quiz.quiz_single_fc(fc_list)
            set_list[index] = manage_quiz_date.update_fc_card(
                fc_list, right_wrong
            )
    return set_list

def check_if_set_has_due_fc(set_list):
    # Returns True if there is a single due fc in the given set list.
    # Else returns False.
    for index, fc_list in enumerate(set_list):
        if check_wether_fc_is_due(set_list[index]):
            return True
    return False 

def quiz_due():
    # Manages the whole due quiz.
    for set_name in general_funktions.get_existing_sets():
        set_list = fc_quiz.get_set_list(set_name)
        print(f"Now quizzing all due flash cads in the set {set_name}.")
        while check_if_set_has_due_fc(set_list):
            quizzed_set_list = quiz_due_fc_in_a_set(set_list)
            fc_quiz.save_quizzed_data(quizzed_set_list, set_name)
    print("You worked through all due flash cards, good work!")

    