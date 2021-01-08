# Importing the random module to randomly select integers for the numerators and the denominators of the two fractions and the colored 
# function for user-friendly display
import random
import sys
from termcolor import colored
# Importing the related two modules below
import ActionFraction_game
from Fraction import Fraction

# Creating the Validator class for the Main class below to check the user input and the play again user input
class Validator:
    # Creating the user_input_validator method to ask and check the user input
    def user_input_validator(self, type_of_answer):
        # Create a while loop to keep checking the user input for question.
        while True:
            user_answer = input(f"\nEnter your answer here as a {type_of_answer}: ")
            # For comparison operation related questions
            if type_of_answer == "True or False":
                if user_answer.capitalize() == "True" or user_answer.capitalize() == "False":
                    return user_answer
                else:
                    print("Please, enter either True or False only.")
            # For arithmetic operation related questions
            else:
                list_user_answer = list(user_answer)
                # Check if the user input only contains valid characters
                good_character_count = 0
                for character in list_user_answer:
                    if character.isnumeric() or character == "-" or character == "+" or character == "." or character == "/":
                        good_character_count += 1
                # If the number of valid characters is not the same as the length of the user input, then the user input is invalid and
                # go back and asking the user for the new input
                if good_character_count == len(list_user_answer):
                    return user_answer
                else:
                    print("Please, make sure to enter the sum of the whole and the remaining parts of the lowest reduced fraction, e.g. -10/4 is -2-1/2 or 4/3 is 1+1/3.")

    # Creating the play_again_input_validator method to ask and check the user input whether he or she wants to play again
    def play_again_input_validator(self):
        """Keeps asking the user whether to play again, until the user type y or n"""
        # Create a while loop to keep checking the user input for question: Would you like to play again?
        while True:
            # Allowing the user to input either capital, lowercase or mixed of capital and lowercase letters 
            # by lowering all of the letters
            play_again = input("\nWould you like another problem [y/n]? ").lower()
            # If the user type in the correct input (y or n), then and the function and return the user's choice
            if play_again == "n" or play_again == "y":
                return play_again
            # Else, print the warning message below and keep asking the question
            else:
                print("Please make sure to type only y or n!")

# The main function of the game below
class Main:
    # Creating the main method, where the program of the game runs
    def main(self):
        # Print out the introduction message at the beginning to the user
        print(colored("Welcome to Action Fractions!\n\n\
If asked for a mixed number, enter the sum of the whole and the remaining parts of the lowest reduced fraction, e.g. -10/4 is -2-1/2 or 4/3 is 1+1/3.\n\
If asked for a decimal number, enter the answer with 3 decimal precision.\n\
For <, =, and > questions, type either True or False.", "yellow"))
        # Initial variables that don't need to run each time the player wants to play again
        correct_answers = 0
        total_answers = 0
        # creating while loop to keep asking the problem until the player decides to not playing anymore
        while True:
            # Integers for fractions of a_1/a_2 and b_1/b_2
            a_1 = random.randint(-100, 100)
            a_2 = random.randint(-100, 100)
            b_1 = random.randint(-100, 100)
            b_2 = random.randint(-100, 100)
            # If the denominator of either fractions is 0, then go back and create a new set of fractions
            if a_1 != 0 and a_2 != 0 and b_1 !=0 and b_2 != 0:
                # Randomly choosing the operation for the question and the type of answer expected from the user
                operation = random.choice(["+", "-", "*", "/", "<", ">", "="])
                type_of_answer = "True or False"
                if operation in ["+", "-", "*", "/"]:
                    type_of_answer = random.choice(["mixed number", "decimal"])
                fraction_1 = Fraction(a_1, a_2)
                fraction_2 = Fraction(b_1, b_2)
                # Print out the question to the user
                print(f"\nWhat is ({fraction_1}) {operation} ({fraction_2})?")
                # Asking and checking the answer from the user with the Validator class from above
                instance_of_Validator = Validator()
                user_answer = instance_of_Validator.user_input_validator(type_of_answer)
                # Update the numbers of correct and total answers based on the user's answer with Gameplay class from the ActionFraction_game
                # module
                instance_of_GamePlay = ActionFraction_game.GamePlay(correct_answers, total_answers, fraction_1, fraction_2, user_answer, operation, type_of_answer)
                correct_answers, total_answers = instance_of_GamePlay.gameplay()
                # Asking the user to play again and check his/her input
                play_again = instance_of_Validator.play_again_input_validator()
                # If the user don't want to play again, then print out the message and end the game
                if play_again == "n":
                    final_message = f"\nYou answered {correct_answers}/{total_answers} problems correctly. Keep up the good work!"
                    print(colored(final_message, "yellow"))
                    sys.exit()
            
# For the module to run as a standalone program, we need to call the function in the below format
if __name__ == "__main__":
    instance_of_Main = Main()
    instance_of_Main.main()