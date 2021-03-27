# Importing the Fraction class from the Fraction module and the colored function for user-friendly display
from Fraction import Fraction
from termcolor import colored

# Creating the AnswerChecker class to determined if the user input is the same as the correct answer
class AnswerChecker:
    """Attributes:
    - correct_answers: integer
    - total_answers: integer
    - type_of_answer: string
    - user_answer: string"""

    # Initializing the variables that are needed to check the answer
    def __init__(self, correct_answers, total_answers, type_of_answer, user_answer):
        self.correct_answers = correct_answers
        self.total_answers = total_answers
        self.type_of_answer = type_of_answer
        self.user_answer = user_answer

    # Creating the answer checker function for operations of >, <, and =
    def answer_checker_for_comparison_operation(self, result):
        if self.user_answer.capitalize() == str(result):
            print(colored("\nCorrect!", "green"))
            self.correct_answers += 1
            self.total_answers += 1
        else:
            print(colored("\nIncorrect!", "red"))
            print(colored(f"The correct answer is {str(result)}", "cyan"))
            self.total_answers += 1
        # Returning the updated correct answers and total answers
        return self.correct_answers, self.total_answers

    # Creating the answer checker function for operations of +, -, *, and /
    def answer_checker_for_arithmetic_operation(self, result):
        # Depending on the asked answer fraction format, check the user answer with the correct answer, if it's incorrect print out the
        # correct answer for the user
        if self.type_of_answer == "mixed number" and self.user_answer == result.__str__():
            print(colored("\nCorrect!", "green"))
            self.correct_answers += 1
            self.total_answers += 1
        elif self.type_of_answer == "mixed number" and self.user_answer != result.__str__():
            print(colored("\nIncorrect!", "red"))
            print(colored(f"The correct answer is {result.__str__()}", "cyan"))
            self.total_answers += 1
        elif self.type_of_answer == "decimal" and self.user_answer == result.as_decimal():
            print(colored("\nCorrect!", "green"))
            self.correct_answers += 1
            self.total_answers += 1
        else:
            print(colored("\nIncorrect!", "red"))
            print(colored(f"The correct answer is {result.as_decimal()}", "cyan"))
            self.total_answers += 1
        # Returning the updated correct answers and total answers
        return self.correct_answers, self.total_answers

# Creating a Gameplay class, which check the user answer with the correct answer, based on the asked operation, type of answer, etc. 
# in the question
class GamePlay:
    """Attributes:
    - correct_answers: integer
    - total_answers: integer
    - fraction_1: string
    - fraction_2: string
    - user_answer: string
    - operation: string
    - type_of_answer: string"""

    # Initializing the variables that are needed to check the answer
    def __init__(self, correct_answers, total_answers, fraction_1, fraction_2, user_answer, operation, type_of_answer):
        self.correct_answers = correct_answers
        self.total_answers = total_answers
        self.fraction_1 = fraction_1
        self.fraction_2 = fraction_2
        self.user_answer = user_answer
        self.operation = operation
        self.type_of_answer = type_of_answer

    # Creating a gameplay method to check if the user answer is correct
    def gameplay(self):
        """Decides if the user calculated correctly or not and return the updated numbers of correct and total answers"""
        # Creating the instance of the AnswerChecker class above
        instance_of_AnswerChecker = AnswerChecker(self.correct_answers, self.total_answers, self.type_of_answer, self.user_answer)
        # Depending on the asked operation in the question, pass the calculated result with the operation of the two fractions into
        # the answer checker method from the AnswerChecker class above to check if the user answer is correct
        if self.operation == "+":
            result = self.fraction_1 + self.fraction_2
            self.correct_answers, self.total_answers = instance_of_AnswerChecker.answer_checker_for_arithmetic_operation(result)
        elif self.operation == "-":
            result = self.fraction_1 - self.fraction_2
            self.correct_answers, self.total_answers = instance_of_AnswerChecker.answer_checker_for_arithmetic_operation(result)
        elif self.operation == "*":
            result = self.fraction_1 * self.fraction_2
            self.correct_answers, self.total_answers = instance_of_AnswerChecker.answer_checker_for_arithmetic_operation(result)
        elif self.operation == "/":
            result = self.fraction_1 / self.fraction_2
            self.correct_answers, self.total_answers = instance_of_AnswerChecker.answer_checker_for_arithmetic_operation(result)
        elif self.operation == "<": 
            result = self.fraction_1 < self.fraction_2
            self.correct_answers, self.total_answers = instance_of_AnswerChecker.answer_checker_for_comparison_operation(result)
        elif self.operation == "=": 
            result = self.fraction_1 == self.fraction_2
            self.correct_answers, self.total_answers = instance_of_AnswerChecker.answer_checker_for_comparison_operation(result)
        else:
            result = self.fraction_1 > self.fraction_2
            self.correct_answers, self.total_answers = instance_of_AnswerChecker.answer_checker_for_comparison_operation(result)
        # Returning the updated correct answers and total answers
        return self.correct_answers, self.total_answers