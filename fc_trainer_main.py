# This is the main menu for the flash card (fc) trainer, that
# starts the other modules.

import fc_creation
import fc_quiz
import fc_due_quiz
import sys

def main_menu():
    print("Welcome user to felix' flash card trainer (ffct)")
    while True:
        print("What do you want to do?")
        print("""Type
            creation  to create new flash cards,
            qdates    to get quizzed on all due flash cards from all sets,
            qsets     to get quizzed on existing flash card sets or
            exit      to exit the flash card trainer.
            """)
        command = input()
        match command:
            case "creation":
                fc_creation.create_fcs()
            case "gdates":
                fc_due_quiz.quiz_due()
            case "qsets":
                fc_quiz.quiz()
            case "exit":
                sys.exit()

main_menu()