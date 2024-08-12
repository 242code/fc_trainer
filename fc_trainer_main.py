"""This is the main menu for the flash card (fc) trainer, that
starts the other modules."""

import sys
from modules import fc_quiz
from modules import fc_due_quiz
from modules import fc_creation


def main_menu():
    print("Welcome user to felix' flash card trainer (ffct)")
    while True:
        print("What do you want to do?")
        print("""Type
            create    to create new flash cards,
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
