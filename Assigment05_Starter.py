# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# AJehle,8.6.2020, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, "r")
for row in objFile:
    strData = row.split(", ")
    dicRow = {"task": strData[0], "priority": strData[1]}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        index = 0
        while index < len(lstTable):
            TaskRow = lstTable[index]
            print(TaskRow['task'] + ', ' + TaskRow['priority'])
            index += 1
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        task = input("Input task: ")
        priority = input("What is the priority of " + task + "? ")
        dicRow = {"task": task, "priority": priority}
        lstTable.append(dicRow)
    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        InputRemove = input("Which task would you like to remove?")
        index = 0
        while index < len(lstTable):
            TaskRemove = lstTable[index]
            if InputRemove == TaskRemove["task"]:
                lstTable.remove(TaskRemove)
                print("Task removed from To-Do List")
            index += 1
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open(strFile, "w")
        printer = ""
        index = 0
        # Write each row to a string
        while index < len(lstTable):
            TaskRow = lstTable[index]
            printer += (TaskRow['task'] + ', ' + TaskRow['priority'] + '\n')
            index += 1
        # Copy string to file and display a message to the user
        objFile.write(printer)
        print('List saved!' + '\n')
        objFile.close()
    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        break  # and Exit the program
