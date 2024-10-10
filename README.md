# My To-Do App

This is a simple To-Do application built using Python and PySimpleGUI. It allows users to add, edit, complete, and manage tasks in a to-do list. The application also displays the current time and date, which updates in real-time.
Features

    Add new to-do items
    Edit existing to-do items
    Mark items as complete and remove them from the list
    Display the current time and date
    Simple and intuitive graphical user interface (GUI)

Requirements

To run this application, you need to install the following Python libraries:

    PySimpleGUI
    A custom functions.py file (explained below)

You can install PySimpleGUI using pip:

bash

pip install PySimpleGUI

functions.py

The functions.py file should contain two functions that handle reading and writing tasks from a text file:

    get_todos(): Reads the current list of to-do items from a file and returns them as a list.
    write_todos(todos): Writes the updated list of to-do items back to the file.

Example of functions.py:

python

def get_todos():
    """Reads a text file and returns a list of to-do items."""
    with open("todos.txt", "r") as file:
        todos = file.readlines()
    return todos

def write_todos(todos):
    """Writes the list of to-do items to a text file."""
    with open("todos.txt", "w") as file:
        file.writelines(todos)

How to Run

    Ensure you have Python installed on your system.
    Install the required libraries using pip:

    bash

pip install PySimpleGUI

Ensure you have the functions.py file in the same directory as the main application code.
Run the application:

bash

    python your_todo_app.py

Application Interface

    Add: Type in a task and click "Add" to add a new to-do item to the list.
    Edit: Select an existing task from the list, edit the text in the input box, and click "Edit" to update the task.
    Complete: Select a task and click "Complete" to remove it from the list.
    Exit: Click "Exit" or close the window to quit the application.
