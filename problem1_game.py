# Importing random module for random.choice() function below
import random

# Creating the game_result() function in the Gameplay class to randomly choose for computer and decided who wins between user and the 
# computer
class GamePlay:
    def game_result(self, user_object):
        """Compares the called argument of user_object to see if it is rock, scissors, or paper and randomly choose one of them for the 
        computer, then it compares the user_object and the computer's choice and return the result"""
        # Setting the computer choice with the random.choice function
        computer_object = random.choice(["paper","rock","scissors"])
        # Checks if the called argument of user_object is rock
        if user_object == "rock":
            # Checks if the computer chooses paper
            if computer_object == "paper":
                # If yes, then the computer wins
                return "Computer chooses paper, the computer wins!"
            # Checks if the computer chooses scissors
            elif computer_object == "scissors":
                # If yes, then the user wins
                return "Computer chooses scissors, you win!"
            # Else, the user and computer ties with both choosing rock
            else:
                # Display the computer's choice and return the result of tie
                return "Computer chooses rock, Let's settle this!"
        # Checks if the called argument of user_object is paper
        elif user_object == "paper":
            # Checks if the computer chooses scissors
            if computer_object == "scissors":
                # If yes, then the computer wins
                return "Computer chooses scissors, the computer wins!"
            # Checks if the computer chooses rocks
            elif computer_object == "rock":
                # If yes, then the user wins
                return "Computer chooses rock, you win!"
            # Else, the user and computer ties with both choosing paper
            else:
                # Display the computer's choice and return the result of tie
                return "Computer chooses paper, Let's settle this!"
        # Checks if the called argument of user_object is scissors
        elif user_object == "scissors":
            # Checks if the computer chooses rocks
            if computer_object == "rock":
                # If yes, then the computer wins
                return "Computer chooses rock, the computer wins!"
            # Checks if the computer chooses paper
            elif computer_object == "paper":
                # If yes, then the user wins
                return "Computer chooses paper, you win!"
            # Else, the user and computer ties with both choosing scissors
            else:
                # Display the computer's choice and return the result of tie
                return "Computer chooses scissors, Let's settle this!"
        # If the called argument of user_object is not either rock, paper, or scissors, return the warning message.
        else:
            return "You must choose rock, paper or scissors. Please, make sure to type in exactly one of the 'rock', 'paper', or 'scissors' words."