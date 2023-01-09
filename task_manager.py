# Lets you create and manage tasks for different users.

import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%d %b %Y"

class Task:
    def __init__(self, taskID = None, username = None, title = None, description = None, due_date = None, assigned_date = None, completed = None):
        '''
        Inputs:
        username: String
        title: String
        description: String
        due_date: DateTime
        assigned_date: DateTime
        completed: Boolean
        '''
        self.taskID = taskID
        self.username = username
        self.title = title
        self.description = description
        self.due_date = due_date
        self.assigned_date = assigned_date
        self.completed = completed


    def from_string(self, task_str):
        '''
        Convert from string in tasks.txt to object
        '''
        tasks = task_str.split("...;;;...")
        taskID = int(tasks[0])
        username = tasks[1]
        title = tasks[2]
        description = tasks[3]
        due_date = datetime.strptime(tasks[4], DATETIME_STRING_FORMAT)
        assigned_date = datetime.strptime(tasks[5], DATETIME_STRING_FORMAT)
        completed = True if tasks[6] == "Yes" else False
        self.__init__(taskID, username, title, description, due_date, assigned_date, completed)


    def to_string(self):
        
        '''
        Convert to string for storage in tasks.txt
        '''
        
        str_attrs = [
            str(self.taskID),
            self.username,
            self.title,
            self.description,
            self.due_date.strftime(DATETIME_STRING_FORMAT),
            self.assigned_date.strftime(DATETIME_STRING_FORMAT),
            "Yes" if self.completed else "No"
        ]
        return "...;;;...".join(str_attrs)

    def display(self):
        '''
        Display object in readable format
        '''
        
        disp_str = f"Task: \t\t {self.title}\n"
        disp_str += f"Task ID: \t {self.taskID} \n"
        disp_str += f"Assigned to: \t {self.username}\n"
        disp_str += f"Date Assigned: \t {self.assigned_date.strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {self.due_date.strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {self.description}\n"
        return disp_str
        

# Read and parse tasks.txt
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    # List comprehension
    # Goes through each item in task_data and keeps it if it's not blank
    task_data = [t for t in task_data if t != ""]

task_list = []
for t_str in task_data:
    curr_t = Task()
    curr_t.from_string(t_str)
    task_list.append(curr_t)
    
# Read and parse user.txt
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin...;;;...password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split('...;;;...')
    username_password[username] = password

# Keep trying until a successful login
logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

def validate_string(input_str):
    '''
    Function for ensuring that string is safe to store
    '''
    if "...;;;..." in input_str:
        print("Your input cannot contain a '...;;;...' character")
        return False
    return True

def check_username_and_password(username, password):
    '''
    Ensures that usernames and passwords can't break the system
    '...;;;...' character cannot be in the username or password
    '''
    if "...;;;..." in username or "...;;;..." in password:
        print("Username or password cannot contain '...;;;...'.")
        return False
    return True

def write_usernames_to_file(username_dict):
    '''
    Function to write username to file
    Input: dictionary of username-password key-value pairs
    '''
    with open("user.txt", "w") as out_file:
        user_data = []
        for k in username_dict:
            user_data.append(f"{k}...;;;...{username_dict[k]}")
        out_file.write("\n".join(user_data))

def reg_user():
    '''
    Function that is called when the user selects ‘r’ to register a user
    '''
    while True:
        # Request input of a new username
        if curr_user != 'admin':
            print("Registering new users requires admin privileges")
            break
        new_username = input("New Username: ")
        temp_usernames_list = []

        # loop that will apply different actions depending on the position of the word in the list
        for user_pass in user_data:
            temp_usernames_list.append(user_pass.split("...;;;...")[0])  # split the first element of each line of user data and append it to usernames list
        if new_username in temp_usernames_list:
            print("Username already exists.")
            continue

        # Request input of a new password
        new_password = input("New Password: ")

        if not check_username_and_password(new_username, new_password):
            # Username or password is not safe for storage - continue
            continue

        # Request input of password confirmation.
        confirm_password = input("Confirm Password: ")

        # Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # If they are the same, add them to the user.txt file,
            print("New user added")

            # Add to dictionary and write to file
            username_password[new_username] = new_password
            write_usernames_to_file(username_password)

        # Otherwise you present a relevant message.
        else:
            print("Passwords do no match")
        break


def add_task():
    '''
    Called when a user selects ‘a’ to add a new task.
    '''

    while True:
        # Prompt a user for the following: 
        #     A username of the person whom the task is assigned to,
        #     A title of a task,
        #     A description of the task and 
        #     the due date of the task.

        taskID = len(task_list)

        # Ask for username
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            continue

        # Get title of task and ensure safe for storage
        while True:
            task_title = input("Title of Task: ")
            if validate_string(task_title):
                break

        # Get description of task and ensure safe for storage
        while True:
            task_description = input("Description of Task: ")
            if validate_string(task_description):
                break

        # Obtain and parse due date
        valid_parse = False
        while not valid_parse:
            try:
                task_due_date = input("Due date of task (e.g. 29 Feb 2024): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                valid_parse = True
            except ValueError:
                print("Invalid datetime format. Please use the format specified")

        # Obtain and parse current date
        curr_date = date.today()
        
        # Create a new Task object and append to list of tasks
        new_task = Task(taskID, task_username, task_title, task_description, due_date_time,curr_date, False)
        task_list.append(new_task)

        # Write to tasks.txt
        with open("tasks.txt", "w") as task_file:
            task_file.write("\n".join([t.to_string() for t in task_list]))
        print("Task successfully added.")
        break

def view_all():
    '''
    view_all is called when users type ‘va’ to view all the taskslisted in ‘tasks.txt’.
    Return to this later, and give admin option to delete tasks.
    '''
    print("-----------------------------------")

    if len(task_list) == 0:
        print("There are no tasks.")
        print("-----------------------------------")

    for t in task_list:
        print(t.display())
        print("-----------------------------------")

def view_mine():
    '''
    view_mine is called when users type ‘vm’ to view all the tasks that have been assigned to them.
    '''
    vm_menu_temp = ""

    while vm_menu_temp != 'e':
        # view_mine is called when users type ‘vm’ to view all the tasks that have been assigned to them.
        current_task = None
        print("-----------------------------------")
        has_task = False
        for t in task_list:
            if t.username == curr_user:
                has_task = True
                print(t.display())
                print("-----------------------------------")

        if not has_task:
            print("You have no tasks.")
            print("-----------------------------------")
            vm_menu_temp = 'e'

        # Choose to edit task
        vm_menu_temp = input('''Select one of the following options below:
            x - Choose a task to edit or mark complete
            e - Exit task view
            : ''').lower()

        # Select task to edit
        if vm_menu_temp == 'x':
            target_task_id = None
            vm_menu_temp = input("Type the ID number of the task you wish to edit:")
        
            while target_task_id == None:
                try:
                    target_task_id = int(vm_menu_temp)
                except ValueError:
                    print("Please enter a valid ID.")

            for task in task_list:
                if task.taskID == target_task_id:
                    current_task: Task = task # The ": Task" bit is type hinting. Hopefully it works.
            
            if current_task is None:
                print(f"Task not found with given ID: {target_task_id}")
                continue
                
            if curr_user != current_task.username:
                print("You are attempting to edit another user's task.")
                continue

            # Menu for editing tasks. 
            # Need to be able to edit tasks if they are incomplete, mark tasks as complete, and exit the menu.
            if current_task.completed == 'Yes':
                print("This task cannot be edited.")
                vm_menu_temp = 'e'
            else:
                vm_menu_temp = input('''Select one of the following options below:
            x - Edit task
            c - Mark task as complete
            e - Exit task view
            : ''').lower()

            # Edit task
            if vm_menu_temp == 'x':
                vm_menu_temp = input('''Select one of the following options below:
                q - Edit person assigned to task
                w - Edit due date
                e - Exit task view
                : ''').lower()
                if vm_menu_temp == 'q':
                    task_username = input("Name of person assigned to task: ")
                    if task_username not in username_password.keys():
                        print("User does not exist. Please enter a valid username")
                        continue
                    
                    current_task.username = task_username  # Modifying username attribute of current_task by reference

                # Edit due date
                elif vm_menu_temp == 'w':
                    valid_parse = False
                    while not valid_parse:
                        try:
                            task_due_date = input("Due date of task (e.g. 29 Feb 2024): ")
                            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                            valid_parse = True
                        except ValueError:
                            print("Invalid datetime format. Please use the format specified")
                    
                    current_task.assigned_date = due_date_time

                vm_menu_temp = 'e'
           
           # Mark task as complete
            elif vm_menu_temp == 'c':
                current_task.completed = "Yes"
                vm_menu_temp = 'e'
            else:
                vm_menu_temp = 'e'
            
            # Iterate over every task in task_list, call the to_string() function on each one
            # and store that as an element in the list task_data_to_save.
            task_data_to_save = [f"{x.to_string()}\n" for x in task_list] 
            with open("tasks.txt", "w") as f:  # Opens the file in write only mode
                f.writelines(task_data_to_save)  # writelines takes a list, and writes each element as a new line to the file

def generate_reports():
    '''
    Add several fields to the report including number of:
    tasks, complete tasks, incomplete tasks, and overdue tasks. 
    Also show percentage of each type of task.
    '''
    num_tasks = len(task_list)
    num_tasks_complete = 0.0
    num_tasks_incomplete = 0.0
    num_tasks_overdue = 0.0

    for i in task_list:
        # if task is complete add one to num_tasks_complete
        if i.completed == True:
            num_tasks_complete += 1
        # else add one to num_tasks_incomplete
        elif i.completed == False:
            num_tasks_incomplete += 1
            # if incomplete task is overdue add one to num_tasks_overdue
            if  i.due_date <= datetime.now():
                num_tasks_overdue += 1
    
    perc_tasks_complete = int(round((num_tasks_complete/num_tasks)*100, 1))
    perc_tasks_incomplete = int(round((num_tasks_incomplete/num_tasks)*100, 1))
    perc_tasks_overdue = int(round((num_tasks_overdue/num_tasks)*100, 1))

    temp_contents = f"TASK OVERVIEW\n\nTotal number of tasks: {num_tasks}\nCompleted: {num_tasks_complete} ({perc_tasks_complete}%)\nIncomplete: {num_tasks_incomplete} ({perc_tasks_incomplete}%)\nOverdue: {num_tasks_overdue} ({perc_tasks_overdue}%)"

    # write to task_overview.txt
    with open("task_overview.txt", "w") as task_file:
        task_file.write(temp_contents)
    print("Task overview report generated.")

    # Total number of users registered
    num_users = len(username_password.keys())

    temp_contents = f"USER OVERVIEW\n\nTotal number of tasks: {num_tasks}\nTotal registered users: {num_users}\n"

    # For each user print their assigned tasks
    for u in username_password:
        user1 = u
        temp_contents += "-----------------------------------\n"

        tasks_for_user = [task for task in task_list if task.username == user1]

        num_tasks = len(tasks_for_user)
        num_tasks_complete = 0.0
        num_tasks_incomplete = 0.0
        num_tasks_overdue = 0.0

        for task in tasks_for_user:
            # if task is complete add one to num_tasks_complete
            if task.completed == True:
                num_tasks_complete += 1
            # else add one to num_tasks_incomplete
            elif task.completed == False:
                num_tasks_incomplete += 1
                # if incomplete task is overdue add one to num_tasks_overdue
                if  task.due_date <= datetime.now():
                    num_tasks_overdue += 1

        if num_tasks == 0:
            perc_tasks_complete = 0.0
            perc_tasks_incomplete = 0.0
            perc_tasks_overdue = 0.0
        else:
            perc_tasks_complete = int(round((num_tasks_complete/num_tasks)*100, 1))
            perc_tasks_incomplete = int(round((num_tasks_incomplete/num_tasks)*100, 1))
            perc_tasks_overdue = int(round((num_tasks_overdue/num_tasks)*100, 1))

        temp_contents += f"Task Overview for {user1}\n\nTotal number of tasks: {num_tasks}\nCompleted: {num_tasks_complete} ({perc_tasks_complete}%)\nIncomplete: {num_tasks_incomplete} ({perc_tasks_incomplete}%)\nOverdue: {num_tasks_overdue} ({perc_tasks_overdue}%)\n"

    temp_contents += "-----------------------------------\n"

    # write to user_overview.txt
    with open("user_overview.txt", "w") as task_file:
        task_file.write(temp_contents)
    print("User overview report generated.")

def display_statistics():
    '''
    New reports will be generated every time.
    Only generating reports if the relevant txt files do not exist means if a user adds a task and then runs displays statistics the reports will be out of date.
    '''
    generate_reports()
    
    # Read contents of generated reports and print them
    print("-----------------------------------\n")
    with open('task_overview.txt', 'r+') as f:
        for line in f:
                print(line)
    print("-----------------------------------\n")
    with open('user_overview.txt', 'r+') as f:
        for line in f:
                print(line)

#########################
# Main Program
######################### 

while True:
    # Get input from user
    print()
    if curr_user == 'admin':
        menu = input('''Select one of the following options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    gr - Generate reports
    ds - Display statistics
    e - Exit
    : ''').lower()
    else:
        menu = input('''Select one of the following options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    e - Exit
    : ''').lower()

    if menu == 'r': # Register new user (if admin)
        reg_user()

    elif menu == 'a': # Add a new task
        add_task()

    elif menu == 'va': # View all tasks
        view_all()

    elif menu == 'vm': # View my tasks
        view_mine()

    elif menu == 'gr': 
        generate_reports()

    # Return to this a lot is missing
    elif menu == 'ds' and curr_user == 'admin': # If admin, display statistics
        display_statistics()

    elif menu == 'e': # Exit program
        print('Goodbye!!!')
        exit()

    else: # Default case
        print("This is not a valid menu choice, please try again.")