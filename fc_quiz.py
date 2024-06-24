# Contains the functions for fc quiz.

import general_funktions
import manage_quiz_date
import csv
import random

def ask_question(question, set_name):
    # Takes the fist item of an fc list and asks the user.
    general_funktions.print_overline(f"Q:    {question} ({set_name})")
    return None

def get_answer_from_user(answer):
    # Gets answer from the user and compares to given correct answer.
    # Returns "r" if the answer was correct. Else asks the user wether the
    # answer was correct. Else returns "f".
    print("A:")
    user_answer = general_funktions.multiline_input()
    if user_answer == answer:
        print("Correct!")
        return "r"
    print("The correct answer is:")
    general_funktions.print_overline(answer)
    print("Was your answer correct? (y/n)")
    input_correct = input()
    if input_correct == "n":
        return "f"
    else:
        return "r"

def quiz_single_fc(single_fc_list, set_name):
    # Quizzes a single fc and adjusts stage and next quiz date.
    ask_question(single_fc_list[0], set_name)
    right_wrong = get_answer_from_user(single_fc_list[1])
    return right_wrong

def get_set_list(set_name):
    # Takes the set name and opens the corresponding .csv file in
    # ./fc_sets in read mode.
    set_file = open(f"./fc_sets/{set_name}.csv", "r")
    set_reader = csv.reader(set_file)
    set_list = list(set_reader)
    set_file.close()
    return set_list

def save_quizzed_data(set_list, set_name):
    # Takes the quizzed list and saves it into the set .csv file.
    set_file = open(f"./fc_sets/{set_name}.csv", "w")
    writer = csv.writer(set_file)
    for single_fc_list in set_list:
        writer.writerow(single_fc_list)
    set_file.close()
    return None

def get_set_name():
    # Asks the user to choose a set, returns the set name (without ".csv")
    existing_sets_list = general_funktions.get_existing_sets()
    print("Which set do you want to get quizzed on?")
    print("The following sets exist:")
    print(",\n".join(existing_sets_list))
    set_to_quiz = input()
    while set_to_quiz not in existing_sets_list:
        set_to_quiz = input("Please enter an existing set name.\n")
    return set_to_quiz

def quiz_set_list(set_list, set_name):
    # Takes a fc list, shuffles it and quizzes the user.
    random.shuffle(set_list)
    for index, single_fc_list in enumerate(set_list):
        quiz_single_fc(single_fc_list, set_name)
    return set_list

def quiz():
    # Executes the quiz routine.
    print("You are now in quiz mode")
    while True:
        set_name = get_set_name()
        set_list = get_set_list(set_name)
        quizzed_fc_list = quiz_set_list(set_list, set_name)
        save_quizzed_data(quizzed_fc_list, set_name)
        print("Do you want to do another set? ('n' to stop)")
        user_input = input()
        if user_input == "n":
            break
    return None