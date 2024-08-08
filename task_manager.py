# =====importing libraries===========
'''This is the section where you will import libraries'''

# ====Login Section====
'''Here you will write code that will allow a user to login.
  - Your code must read usernames and password from the user.txt file
  - You can use a list or dictionary to store a list of usernames
  - And passwords from the file
  - Use a while loop to validate your user name and password'''

user = {}

with open("user.txt", "r") as f:
    for line in f:
        (keys, values) = line.split()
        keys = keys.replace(",", "")
        user[keys] = values


while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in user.keys() and password == user[username]:
        print("\nLogin successful!\n")

    elif username and password != user.items():
        print("\nUsername or password is incorrect!\n")
        continue
    break


while True:
    # Present the menu to the user and
    # make sure that the user input is converted to lower case.

    if username != "admin" and password != "adm1n":

        menu = input('''\nSelect one of the following options:\n
r - register a user (admin only)
a - add task
va - view all tasks
vm - view my tasks
e - exit
: \n''').lower()
    else:
        menu = input('''\nSelect one of the following options:
r - register a user (admin only)
a - add task
va - view all tasks
vm - view my tasks
ds - display statistics
e - exit
: \n''').lower()

    if menu == 'r' and username != "admin" and password != "adm1n":
        print("\nYou are not authorised to register users. Select another option\n")

    elif menu == 'r' and username == "admin" and password == "adm1n":
        print("\nYou can register a user\n")
        new_user = []
        new_password = []

        with open("user.txt", "r") as file:
            for lines in file:
                word_strip = lines.strip()
                word_strip = word_strip.split(", ")

                new_user.append(word_strip[0])
                new_password.append(word_strip[1])

        new_user = input("\nEnter the user's username\n")
        new_password = input("\nEnter the user's password\n")
        password_confirm = input("\nRe-enter the password\n")

        if new_password != password_confirm:
            print("\nPasswords do not match. Please try again\n")

        else:
            with open("user.txt", "a") as file:
                file.write(f"\n{new_user}, {new_password}")
                print("\nNew user has been added\n")

        '''This code block will add a new user to the user.txt file
        - You can use the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same
            - If they are the same, add them to the user.txt file,
              otherwise present a relevant message'''

    elif menu == 'a':
        assigned_to = []
        task_title = []
        task_desc = []
        current_date = []
        due_date = []
        status = []

        with open("tasks.txt", "r") as file:
            for lines in file:
                temp = lines.strip()
                temp = temp.split(", ")

                assigned_to.append(temp[0])
                task_title.append(temp[1])
                task_desc.append(temp[2])
                current_date.append(temp[3])
                due_date.append(temp[4])
                status.append(temp[5])

        assigned_to_ = input("Task assigned to: ")
        task_title_ = input("Task title: ")
        task_desc_ = input("Task Description: ")
        current_date_ = input("Enter today's date (DD-MM-YYYY): ")
        due_date_ = input("Due date (DD-MM-YYYY): ")

        with open("tasks.txt", "a") as file:
            file.write(f"\n{assigned_to_}, {task_title_}, {task_desc_}, {current_date_}, {due_date_}, No")

        print("\nThe task has been added\n")

        '''This code block will allow a user to add a new task to task.txt file
            - You can use these steps:
                - Prompt a user for the following:
                    - the username of the person whom the task is assigned to,
                    - the title of the task,
                    - the description of the task, and
                    - the due date of the task.
                - Then, get the current date.
                - Add the data to the file task.txt
                - Remember to include 'No' to indicate that the task is not complete.'''

    elif menu == 'va':
        with open('tasks.txt', 'r') as file:
            for line in file:
                temp = line.strip()
                temp = temp.split(", ")
                print(f'''
Task name:          {temp[1]}
Assigned to:        {temp[0]}
Date assigened:     {temp[3]}
Due date:           {temp[4]}
Task Complete:      {temp[5]}
Task description:   {temp[2]}
''')
                # print(line.strip())

        '''This code block will read the task from task.txt file and
        print to the console in the format of Output 2 presented in the PDF
        You can do it in this way:
        - Read a line from the file.
        - Split that line where there is comma and space.
        - Then print the results in the format shown in the Output 2 in the PDF
        - It is much easier to read a file using a for loop.'''

    elif menu == 'vm':
        with open('tasks.txt', 'r') as file:
            for line in file:
                assigned_to, title, description, assigned_date, due_date, completed = line.strip().split(", ")
                if assigned_to == username:
                    temp = line.strip()
                    temp = temp.split(", ")
                    print(f'''
Task:               {temp[1]}
Assigned to:        {temp[0]}
Date assigned:      {temp[3]}
Due date:           {temp[4]}
Task complete?      {temp[5]}
Task description:   {temp[2]}
''')
        if assigned_to != username:
            print("\nThere are no tasks assigned to current user")

        '''This code block will read the task from task.txt file and
        print to the console in the format of Output 2 presented in the PDF
        You can do it in this way:
        - Read a line from the file
        - Split the line where there is comma and space.
        - Check if the username of the person logged in is the same as the
        username you have read from the file.
        - If they are the same you print the task in the format of Output 2
        shown in the PDF '''

    # elif menu == 'ds' and username == "admin" and password == "adm1n":
    #    print("Tasks and user statistics are as follows:")

    elif menu == 'ds' and username == 'admin':
        with open("user.txt", "r") as f:
            num_users = len(f.readlines())
            print(f"\nThe total number of users are:\t {num_users}")

        with open('tasks.txt', 'r') as file:
            num_tasks = len(file.readlines())
            print(f"\nThe total number of tasks are:\t {num_tasks}\n")

    elif menu == 'e':
        print('\nGoodbye!\n')
        exit()

    else:
        print("Invalid choice, please try again later")
