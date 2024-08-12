"""This contains the gui for the fc trainer and will replace the fc_trainer_main.py
evntually
"""

from tkinter import *
from tkinter import ttk
from mudules import general_funktions

SUB_MENUS = ["create", "quiz", "set quiz"]

def create_set_buttons(frame, mode):
    """This creates a Button for every existing set. The mode parameter is used
    to determine, whether the a button for a new set needs to be generated."""
    if mode == SUB_MENUS[0]:
        ttk.Button(frame, text="New set", width=15).grid(column=0, row=1, sticky=W)
    existing_sets = general_funktions.get_existing_sets()
    for index, set in enumerate(existing_sets):
        ttk.Button(frame, text=set, width=15).grid(column=0, row=index+2, sticky=W)

def create_sub_menu_frames(frame):
    """Creates the three Frames for "create", "quiz" and "set quiz" with the
    corresponding label and Buttons and places them into the given frame"""
    for index, sm in enumerate(SUB_MENUS):
        current_frame = ttk.Frame(frame, padding="3")
        current_frame.grid(column=index, row=0)
        ttk.Label(current_frame, text=sm, width=20).grid(row=0, sticky=(W, N))
        if not sm == "quiz":
            create_set_buttons(current_frame, sm)

root = Tk()
root.title("ffct")

# Create the frame for all other widgets to be placed on.
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create the frame for the static text to be placed on.
static_frame = ttk.Frame(mainframe)
static_frame.grid(column=0, row=0)
greeting_label = ttk.Label(
    static_frame,
    text = "Welcome user to felix' flash card trainer (ffct)"
)
question_label = ttk.Label(
    static_frame,
    text = "What do you want to do?",
    width = 15
)
greeting_label.grid(column=0, row=0, sticky=W)
question_label.grid(column=0, row=1, sticky=W)

# Create the menu
menu_frame = ttk.Frame(mainframe)
menu_frame.grid(column=0, row=1, sticky=W)

create_sub_menu_frames(menu_frame)
"""create_option = ttk.Label(
    menu_frame,
    text = "create"
)
create_option.bind(
    "<ButtonPress-1>",
    lambda e: create_option.configure(
        text="WOW"
    ))

create_option.grid(column=0, row=0, sticky=W)
create_set_buttons(menu_frame, mode="create")"""

root.mainloop()
