# Importing the the game file where the actual game_result() function is located
import problem1_game

# For the main() function in the PlayAgain class below
class PlayAgain:
    def play_again_input_validator(self):
        """Keeps asking the user whether to play again, until the user type y or n"""
        # Create a while loop to keep checking the user input for question: Would you like to play again?
        while True:
            # Allowing the user to input either capital, lowercase or mixed of capital and lowercase letters 
            # by lowering all of the letters
            play_again = input("Would you like to play again? (type y or n): ").lower()
            # If the user type in the correct input (y or n), then and the function and return the user's choice
            if play_again == "n" or play_again == "y":
                return play_again
            # Else, print the warning message below and keep asking the question
            else:
                print("Please make sure to type only y or n!")

# This is the main function in the Main class for the rock, paper, scissors game:
class Main:
    def main(self):
        """The main function is calling the game function from problem1_game module and the play_again_input_validator() function"""
        # Creating a while loop to keep checking if the user input is valid or not
        while True:
            # Allowing the user to input either capital, lowercase or mixed of capital and lowercase letters by lowering all of the 
            # letters
            user_object = input("Please, chooose between rock, paper, and scissors: ").lower()
            # Passing the user input variable above to the imported function of game_result from the file problem1_game.py to see the 
            # result
            instance_of_GamePlay = problem1_game.GamePlay()
            result = instance_of_GamePlay.game_result(user_object)
            # Print out the result, so that the user can see it
            print(result)
            # If the word settle and must are not in the splitted list of word of the resulting sentence from the result variable, 
            # meaning the result is not a tie or the user did not enter invalid choice, the program asks the player whether to play 
            # again. If it's a tie or the user enters invalid choice, then don't ask the question, immediately go back and ask the new 
            # user's choice instead.
            if "settle" not in result.split(" ") and "must" not in result.split(" "):
                # Calling the play_again function to ask and check whether user want to play again
                instance_of_PlayAgain = PlayAgain()
                play_again = instance_of_PlayAgain.play_again_input_validator()
                # If the user choose no (n) for not playing again, then break out and end the function/program
                if play_again == "n":
                    break

# For running the module as a standalone program, we need to add the following code below:
if __name__ == "__main__":
    instance_of_Main = Main()
    instance_of_Main.main()