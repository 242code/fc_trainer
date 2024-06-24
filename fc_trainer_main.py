# This is the main menu for the flash card (fc) trainer, that
# starts the other modules.

import fc_creation
import fc_quiz
import fc_due_quiz
import sys
import os

def main_menu():
    print(os.getcwd())
    print("Welcome user to felix' flash card trainer (ffct)")
    while True:
        print("What do you want to do?")
        print("""Type
            creation  to create new flash cards,
            due       to get quizzed on all due flash cards from all sets,
            set       to get quizzed on existing flash card sets or
            exit      to exit the flash card trainer.
            """)
        command = input()
        match command:
            case "create":
                fc_creation.create_fcs()
            case "due":
                fc_due_quiz.quiz_due()
            case "set":
                fc_quiz.quiz()
            case "exit":
                sys.exit()

main_menu()