# This contains functions to get the date of the next quiz depending on stage
# of the flash card (fc).

import datetime

STAGES = {
    # Contains the stage: days till next quiz.
    0: 0,
    1: 3,
    2: 7,
    3: 15,
    4: 31,
    5: 64
    }

def get_days_till_next_quiz(stage):
    # Takes the int stage and returns the int days till next quiz.
    return STAGES[stage]

def get_next_quiz_date(stage):
    # Takes the stage of a fc and returns the next quiz date as a str dd.mm.yy
    today_datetime = datetime.datetime.now()
    delta = datetime.timedelta(days = get_days_till_next_quiz(stage))
    next_quiz_date_datetime = today_datetime + delta
    next_quiz_date_str = next_quiz_date_datetime.strftime("%d.%m.%Y")
    return next_quiz_date_str

def get_new_stage(stage, right_or_wrong):
    # Takes the current stage and the information wether the answer was
    # right ("r") or wrong and returns the new stage as int.
    if right_or_wrong == "r":
        return int(stage) + 1
    else:
        return 0

def update_fc_card(single_fc_list, right_or_wrong):
    # Takes a single fc list and the information wether the answer was
    # was right ("r") or wrong and updates stage and next quiz date.
    # then returns the updated fc list
    single_fc_list[3] = get_new_stage(single_fc_list[3], right_or_wrong)
    single_fc_list[4] = get_next_quiz_date(single_fc_list[3])
    return single_fc_list
