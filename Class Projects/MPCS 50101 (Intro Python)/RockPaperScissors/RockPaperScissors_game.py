# Importing random module for random.choice() function below and the colored function for user-friendly display
import random
from termcolor import colored

# Creating the game_result() function in the Gameplay class to randomly choose for computer and decided who wins between user and the 
# computer
class GamePlay:
    def game_result(self, user_object, win, total_game):
        """Compares the called argument of user_object to see if it is rock, scissors, or paper and randomly choose one of them for the 
        computer, then it compares the user_object and the computer's choice and return the result"""
        # Setting the computer choice with the random.choice function
        computer_object = random.choice(["paper","rock","scissors"])
        # Checks if the called argument of user_object is rock
        if user_object == "rock":
            # Checks if the computer chooses paper
            if computer_object == "paper":
                # If yes, then the computer wins
                total_game += 1
                return colored("Computer chooses paper, the computer wins!", "red"), win, total_game
            # Checks if the computer chooses scissors
            elif computer_object == "scissors":
                # If yes, then the user wins
                win += 1
                total_game += 1
                return colored("Computer chooses scissors, you win!", "green"), win, total_game
            # Else, the user and computer ties with both choosing rock
            else:
                # Display the computer's choice and return the result of tie
                return colored("Computer chooses rock, Let's settle this!", "cyan"), win, total_game
        # Checks if the called argument of user_object is paper
        elif user_object == "paper":
            # Checks if the computer chooses scissors
            if computer_object == "scissors":
                # If yes, then the computer wins
                total_game += 1
                return colored("Computer chooses scissors, the computer wins!", "red"), win, total_game
            # Checks if the computer chooses rocks
            elif computer_object == "rock":
                # If yes, then the user wins
                win += 1
                total_game += 1
                return colored("Computer chooses rock, you win!", "green"), win, total_game
            # Else, the user and computer ties with both choosing paper
            else:
                # Display the computer's choice and return the result of tie
                return colored("Computer chooses paper, Let's settle this!", "cyan"), win, total_game
        # Checks if the called argument of user_object is scissors
        elif user_object == "scissors":
            # Checks if the computer chooses rocks
            if computer_object == "rock":
                # If yes, then the computer wins
                total_game += 1
                return colored("Computer chooses rock, the computer wins!", "red"), win, total_game
            # Checks if the computer chooses paper
            elif computer_object == "paper":
                # If yes, then the user wins
                win += 1
                total_game += 1
                return colored("Computer chooses paper, you win!", "green"), win, total_game
            # Else, the user and computer ties with both choosing scissors
            else:
                # Display the computer's choice and return the result of tie
                return colored("Computer chooses scissors, Let's settle this!", "cyan"), win, total_game
        # If the called argument of user_object is not either rock, paper, or scissors, return the warning message.
        else:
            return colored("You must choose rock, paper or scissors. Please, make sure to type in exactly one of the 'rock', 'paper', or 'scissors' words.", "yellow"), win, total_game