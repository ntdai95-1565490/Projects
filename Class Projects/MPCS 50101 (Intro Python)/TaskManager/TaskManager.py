# Importing the necessary modules for formatting the tasks below
import sys
import pickle
import re
import datetime
from tabulate import tabulate

# Creating a custom error class
class InputError(Exception):
    """Exception raised for type errors in the argument"""
    # Initializing the message attribute
    def __init__(self, message):
        self.message = message
    # Returning the appropriate message, depending on the message
    def __str__(self):
        return "InputError, {}".format(self.message)

# Creating a PickleCreator class to create the pickle file based on the word objects
class PickleCreator:
    """Pickling the data of list_of_task to the file"""
    # Initializing the list_of_task attribute
    def __init__(self, list_of_task):
        self.list_of_task = list_of_task
    # Defining the creating_pickle() method to write the data to a pickle file    
    def creating_pickle(self):
        with open(".todo.pickle", "wb") as p:
            pickle.dump(self.list_of_task, p)

class Task:
    """Representation of a task
    Attributes:
            - created - date
            - completed - date
            - name - string
            - unique id - number
            - priority - string of value of 1, 2, or 3; 1 should be the default level
            - due date - date, optional
            - list of task - list, consisting all of the information above for each task
    """

    # Creating class variables
    created = []
    completed = []
    name = []
    unique_id = []
    priority = []
    due_date = []
    list_of_task = []
    
    # Creating the add_command() method for adding task
    def add_command(self, user_input, list_of_task):
        """Creating the name, due_date, priority, and unique_id attributes based on the user input."""
        # Checking and retrieving the task's name
        if re.search(r"\"(.+?)\"", user_input) == None and re.search(r"\'(.+?)\'", user_input) == None:
            raise InputError("please put the name of the task in a quotation mark.")
        elif re.search(r"\"(.+?)\"", user_input) != None:
            name = re.search(r"\"(.+?)\"", user_input)[1]
        else:
            name = re.search(r"\'(.+?)\'", user_input)[1]
        # Checking and retrieving the due date either in the format of mm/dd/yyyy or as a weekday
        if re.search(r"due:(\d{1,2}/\d{1,2}/\d{4})", user_input) != None:
            due_date = re.search(r"due:(\d{1,2}/\d{1,2}/\d{4})", user_input)[1]
        # If the due date is in a weekday format, then we need to calculate the exact due date in mm/dd/yyyy format
        elif re.search(r"due:(\w+)", user_input) != None:
            if re.search(r"due:(\w+)", user_input).group(1).lower() in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
                list_of_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
                # Converting the due date's weekday to numbers as Monday for 0 until sunday to 6
                weekday = []
                for index, day in enumerate(list_of_days):
                    if re.search(r"due:(\w+)", user_input).group(1).lower() == day:
                        weekday.append(index)
                # Finding out today's date weekday
                today = datetime.datetime.now()
                today_weekday = today.weekday()
                # Finding the difference of days between the input due date's weekday and today's weekday
                day_difference = weekday[0] - today_weekday
                # If the two days are the same, then it means the due date is a week from now
                if day_difference == 0:
                    day_difference = 7
                # If the difference is negative, meaning today's weekday is in this week while the input due date's weekday is in next week, we
                # need to add 7 days to get the difference in days
                elif day_difference < 0:
                    day_difference = 7 + day_difference
                # Adding the days difference to today's date to find out the due date and formatting it to mm/dd/yyyy format
                due_date_raw = today + datetime.timedelta(days = day_difference)
                due_date = due_date_raw.strftime("%m/%d/%Y")
            # If the user mistyped such as Monaday or type wrong due dates, then return the following warning message
            else:
                raise InputError("please put the due date of the task in the format of mm/dd/yyyy or type in the name of the weekday such as monday, tuesday, etc.")
        # If there is no due date present, then put - for the due date
        else:
            due_date = "-"
        # Finding the priority in the user input
        priority = re.search(r"priority:(\d)", user_input)
        if priority != None:
            # Check if the priority is either 1,2, or 3, then change it to integer to later be able to sort it out
            if priority[1] == "1" or priority[1] == "2" or priority[1] == "3":
                priority = int(priority[1])
            else:
                raise InputError("please put only 1, 2, or 3 for the level of the task's priority.")
        # If there was no priority, set the default priority to 1
        else:
            priority = 1
        # Finding out the unique_id's that have been used before
        unique_id = []
        for task in list_of_task:
            unique_id.append(task[6])
        # If there wasn't any task inputed before, then set the first task id to 1
        if unique_id == []:
            unique_id = 1
        # Else, find out the maximum id and add 1 to it to get a new unique id
        else:
            unique_id = max(unique_id) + 1
        # Returning the name, due_date, priority, unique_id based on the user input and the stored data in the list_of_task attribute
        # in the class
        return name, due_date, priority, unique_id

    def list_command(self, user_input, list_of_task):
        """Listing out the task sorted by due dates if that exists, else sorted by priority"""
        # Listing out the components of the list command
        list_of_terms_in_user_input = user_input.split(" ")
        # Selecting only the uncompleted task
        uncompleted_list_of_tasks = []
        for task in list_of_task:
            if task[5] == "-":
                uncompleted_list_of_tasks.append(task)
        # Separating the tasks with due date and the tasks without due date
        uncompleted_list_of_tasks_with_due_date = []
        uncompleted_list_of_tasks_without_due_date = []
        for task in uncompleted_list_of_tasks:
            if task[1] != "-":
                uncompleted_list_of_tasks_with_due_date.append(task)
            else:
                uncompleted_list_of_tasks_without_due_date.append(task)
        # Sorting the list of task with due date and the list of task without due date    
        sorted_uncompleted_list_of_tasks_with_due_date = sorted(sorted(uncompleted_list_of_tasks_with_due_date, key = lambda x: x[2]), key = lambda x: datetime.datetime.strptime(x[1], "%m/%d/%Y"))
        uncompleted_list_of_tasks_without_due_date.sort(key = lambda x: x[2])
        # Combining the two list back together
        sorted_uncompleted_list_of_tasks = sorted_uncompleted_list_of_tasks_with_due_date + uncompleted_list_of_tasks_without_due_date
        # Finding out today's date time to find out the age of each task below
        today = datetime.date.today()
        months = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
        # Creating the lists of columns and their values to print out to the terminal
        list_of_unique_id = []
        list_of_ages = []
        list_of_due_date = []
        list_of_priority = []
        list_of_name = []
        for task in sorted_uncompleted_list_of_tasks:
            list_of_unique_id.append(task[0])
            list_of_due_date.append(task[1])
            list_of_priority.append(task[2])
            list_of_name.append(task[3])
            list_of_attributes_of_creation_date_of_task = task[4].split(" ")
            year, month, day = int(list_of_attributes_of_creation_date_of_task[5]), list_of_attributes_of_creation_date_of_task[1], int(list_of_attributes_of_creation_date_of_task[2])
            month_as_numerical = months[month]
            creation_date = datetime.date(year, month_as_numerical, day)
            age = today - creation_date
            age_string = f"{age.days}d"
            list_of_ages.append(age_string)
        # If there was only the "list" command without search term, then just print out the above created columns and values
        if len(list_of_terms_in_user_input) == 1:
            table = []
            for i in range(len(list_of_unique_id)):
                task = [list_of_unique_id[i], list_of_ages[i], list_of_due_date[i], list_of_priority[i], list_of_name[i]]
                table.append(task)

            print(tabulate(table, headers = ["ID", "Age", "Due Date", "Priority", "Task"]))
        # If there were search terms, then go through each search term and match in the names of the tasks (upper or lower cases 
        # does not matter), selecting only those tasks
        else:
            list_of_terms_in_user_input_without_list_command = list_of_terms_in_user_input[1:]
            list_of_indexes_with_term_in_task = []
            for term in list_of_terms_in_user_input_without_list_command:
                if term[0] != "+":
                    raise InputError("please put a + mark in front of every search terms.")
                else:
                    term_without_plus = term[1:]
                    for index, value in enumerate(list_of_name):
                        if term_without_plus.lower() in value.lower():
                            list_of_indexes_with_term_in_task.append(index)
            # Creating the table with the filtered list of task based on the search terms
            table = []
            for index in list_of_indexes_with_term_in_task:
                task = [list_of_unique_id[index], list_of_ages[index], list_of_due_date[index], list_of_priority[index], list_of_name[index]]
                table.append(task)

            print(tabulate(table, headers = ["ID", "Age", "Due Date", "Priority", "Task"]))

    def done_command(self, user_input, list_of_task):
        """Creating the completed time for the tasks that was designated as done by the user"""
        # Retrieving the task's id
        done_unique_id = user_input.split(" ")[1]
        # Going through the list to find the exact task with the ID and create a date with the current date time for the task's 
        # completion date
        for task in list_of_task:
            if task[0] == int(done_unique_id):
                now = datetime.datetime.now()
                task[5] = now.strftime("%a %b %d %H:%M:%S CST %Y").replace(" 0", " ")
        
        return list_of_task

    def delete_command(self, user_input, list_of_task):
        """Deleting the task with the user input ID"""
        # Retrieving the task's id
        delete_unique_id = user_input.split(" ")[1]
        # Going through the list to find the exact task with the ID and delete that task
        for task in list_of_task:
            if task[0] == int(delete_unique_id):
                list_of_task.remove(task)
        
        return list_of_task

    def report_command(self, list_of_task):
        """Reporting the whole data for each task in the list_of_task attribute of the class"""
        # Finding out today's date time to find out the age of each task below
        today = datetime.date.today()
        months = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
        # Creating the lists of columns and their values to print out to the terminal
        list_of_unique_id = []
        list_of_ages = []
        list_of_due_date = []
        list_of_priority = []
        list_of_name = []
        list_of_created = []
        list_of_completed = []
        for task in list_of_task:
            list_of_unique_id.append(task[0])
            list_of_due_date.append(task[1])
            list_of_priority.append(task[2])
            list_of_name.append(task[3])
            list_of_attributes_of_creation_date_of_task = task[4].split(" ")
            year, month, day = int(list_of_attributes_of_creation_date_of_task[5]), list_of_attributes_of_creation_date_of_task[1], int(list_of_attributes_of_creation_date_of_task[2])
            month_as_numerical = months[month]
            creation_date = datetime.date(year, month_as_numerical, day)
            age = today - creation_date
            age_string = f"{age.days}d"
            list_of_ages.append(age_string)
            list_of_created.append(task[4])
            list_of_completed.append(task[5])
        # Creating a table to print out the above created columns and values
        table = []
        for i in range(len(list_of_unique_id)):
            task = [list_of_unique_id[i], list_of_ages[i], list_of_due_date[i], list_of_priority[i], list_of_name[i], list_of_created[i], list_of_completed[i]]
            table.append(task)

        print(tabulate(table, headers = ["ID", "Age", "Due Date", "Priority", "Task", "Created", "Completed"]))

class Tasks:
    """List of Task objects."""
    list_of_tasks = []

    @classmethod
    def ordering_of_tasks(cls, list_of_task):
        """The method takes the list_of_task attribute from the class of Task and sorted by the creation date."""
        list_of_task.sort(key = lambda x: x[4])
        cls.list_of_tasks = list_of_task

class Main:
    def main(self):
        try:
            # Displaying welcome message to the user
            print("Welcome to the Task Manager!")
            # Loading the pickle objects in
            with open(".todo.pickle", "rb") as p:
                pickle_objects = pickle.load(p)
            # Loading all of the data into their corresponding attributes in the class of Task
            Task.list_of_task = pickle_objects
            for task in Task.list_of_task:
                Task.name.append(task[3])
                Task.due_date.append(task[1])
                Task.priority.append(task[2])
                Task.unique_id.append(task[0])
                Task.completed.append(task[5])
                Task.created.append(task[4])
            # Passing the list_of_task attribute from the class of Task to the class of Tasks to be sorted by creation dates
            Tasks.ordering_of_tasks(Task.list_of_task)
        # If the pickle file was empty because of first time openning it or there wasn't any task in the file   
        except EOFError:
            Task.list_of_task = []

        while True:
            try:
                user_input = input("\nPlease, type in below one of the commands of add, list, done, delete, or report, following at least one space before your the task (eg. add 'homework' due:Monday, priority:2 or list +eggs). Press q if you want to save your data and quit.\n")
                # If user want to quit, then make sure to save the input data to a pickle file using the creating_pickle() method from
                # the PickleCreator class
                if user_input.lower() == "q":
                    list_of_task = Task.list_of_task
                    # Creating a pickle file with the list_of_task object created above
                    instance_of_PickleCreator = PickleCreator(list_of_task)
                    instance_of_PickleCreator.creating_pickle()
                    sys.exit()
                # For add commands, loading in the list_of_task attribute from the class of Task and then create new attributes for the
                # task that the user input
                elif user_input.split()[0].lower() == "add":
                    list_of_task = Task.list_of_task
                    name, due_date, priority, unique_id = Task().add_command(user_input, list_of_task)
                    Task.name.append(name)
                    Task.due_date.append(due_date)
                    Task.priority.append(priority)
                    Task.unique_id.append(unique_id)
                    completed = "-"
                    now = datetime.datetime.now()
                    created = now.strftime("%a %b %d %H:%M:%S CST %Y").replace(" 0", " ")
                    Task.completed.append(completed)
                    Task.created.append(created)
                    # After creating the attributes for the user input task above, adding it to the list_of_task attribute in the class
                    # of Task and class of Tasks for ordering by creation date
                    task = [unique_id, due_date, priority, name, created, completed, unique_id]
                    Task.list_of_task.append(task)
                    Tasks.ordering_of_tasks(Task.list_of_task)
                    # Print out the ID for that task to the user
                    print(f"Created task {unique_id}")
                # For list commands, load in the list_of_task attribute stored in the class of Task and use the list_command() method
                # to list out the tasks
                elif user_input.split()[0].lower() == "list":
                    list_of_task = Task.list_of_task
                    Task().list_command(user_input, list_of_task)
                # For done commands, load in the list_of_task attribute stored in the class of Task and use the done_command() method
                # to create a completed date time for each task
                elif user_input.split()[0].lower() == "done":
                    list_of_task = Task.list_of_task
                    Task.list_of_task = Task().done_command(user_input, list_of_task)
                    Tasks.ordering_of_tasks(Task.list_of_task)
                # For delete commands, load in the list_of_task attribute stored in the class of Task and use the delete_command() method
                # to delete the task based on the user input ID
                elif user_input.split()[0].lower() == "delete":
                    list_of_task = Task.list_of_task
                    Task.list_of_task = Task().delete_command(user_input, list_of_task)
                    Tasks.ordering_of_tasks(Task.list_of_task)
                # For report commands, load in the list_of_task attribute stored in the class of Task and use the report_command() method
                # to report all of the tasks with all of their attributes, including creation and completion dates
                elif user_input.split()[0].lower() == "report":
                    list_of_task = Task.list_of_task
                    Task().report_command(list_of_task)
                # If there wasn't any add, list, done, report, or delete commands, then ask the user to choose one of them.
                else:
                    print("Please, choose one of the commands of add, list, done, delete, or report with your task and make sure that there is at least one space after the command.")
            # If there was any input error based on the user input, then print out the message with the specific error message based on
            # the issue.
            except InputError as error:
                print(error)

# For the module to run as a standalone program, we need to call the class in the below format
if __name__ == "__main__":
    instance_of_Main = Main()
    instance_of_Main.main()