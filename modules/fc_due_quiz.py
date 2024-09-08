"""Contains all funktions ot modify the set quiz to only ask due fcs."""

import datetime
import random
from modules import fc_quiz
from modules import manage_quiz_date
from modules import general_functions


def date_str_to_datetime_obj(date_str):
    # Takes a date string (%d.%m.%Y) and returns a datetime objekt.
    date_obj = datetime.datetime.strptime(date_str, "%d.%m.%Y")
    return date_obj


def check_wether_fc_is_due(next_quiz_date, today_dto):
    # Checks wether the next quiz date is in the furutre, then returns False, #TODO spelling
    # else returns True.
    if today_dto < next_quiz_date: #TODO: return today_dto < next_quiz_date
        return False
    return True


def quiz_due_fc_in_a_set(set_list, set_name, today_dto):
    # Takes the set list of lists and iterates over the due dates of every
    # fc list and quizzes the user. Returns the updated list.
    random.shuffle(set_list)
    for index, fc_list in enumerate(set_list):
        if check_wether_fc_is_due(
                date_str_to_datetime_obj(fc_list[4]), #TODO a short comment explaining the 4 would be nice
            #TODO Actually, maybe make a csv util class to access the different columns with very concise names. or switch to yaml or json and live with an already more concise way of calling attributes
                today_dto #TODO also you dont need the linebreaks here.
        ):
            right_wrong = fc_quiz.quiz_single_fc(fc_list, set_name) #TODO: no need to initalize a variable, also name it less confusing
            set_list[index] = manage_quiz_date.update_fc_card(
                fc_list, right_wrong
            )
    return set_list


def check_if_set_has_due_fc(set_list, today_dto): #TODO: reevaluate if you need to pass through the today_dto or should just create one in the check_wether_fc_is_due
    # Returns True if there is a single due fc in the given set list.
    # Else returns False.
    for fc_list in set_list:
        if check_wether_fc_is_due(
                date_str_to_datetime_obj(fc_list[4]), #TODO: Make clear why you use the 4th element in fc_list
                today_dto
        ):
            return True
    return False


def quiz_due():
    # Manages the whole due quiz.
    today_dto = datetime.datetime.today() #TODO: What is dto?
    for set_name in general_functions.get_existing_sets():
        set_list = fc_quiz.get_set_list(set_name)
        print(f"Now quizzing all due flash cads in the set {set_name}.") #TODO correct cards
        while check_if_set_has_due_fc(set_list, today_dto):
            quizzed_set_list = quiz_due_fc_in_a_set(
                set_list,
                set_name,
                today_dto
            )
            fc_quiz.save_quizzed_data(quizzed_set_list, set_name)
    print("You worked through all due flash cards, good work!")
