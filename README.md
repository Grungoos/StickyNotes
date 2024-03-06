# Sticky Notes

Sticky Notes is a simple to-do program developed in Python using the Tkinter framework.

## Features

- **Adding tasks**: New tasks can be added by clicking on the "+" button.
- **Deleting tasks**: Tasks can be deleted individually by clicking on the "X" button next to each task.
- **Marking tasks as completed**: Each task has a checkbox that can be clicked to mark the task as completed.
- **Saving tasks**: By clicking on the "Save" button, all tasks are saved in a `.txt` file in JSON format.
- **Loading tasks**: Clicking on the "Load" button loads all tasks from the `.txt` file.
- **Adjusting transparency**: A slider is provided to adjust the window's transparency.
- **Pinning the window**: The window can be pinned to stay on top of all other windows.

## Starting the program

To start the program, run the Python script with the following command:

```sh
python main.py

# Usage Notes

This program uses JSON serialization, which is saved in a .txt file to store the tasks.
This format is more secure and readable compared to binary serialization formats such as pickle.
The .txt file will be created in the same directory as the script if it doesn't already exist.
Ensure that this script has the necessary permissions to read from and write to the filesystem.
Always make sure that the data in the .txt file is in a proper JSON format to avoid load errors.

For transparency adjustment and pinning the window, use the provided slider and "Pin" button respectively in the application interface.


You can save this text as a `README.md` file in your project directory where the `main.py` script is located.
The Markdown format (`.md`) is commonly used for README files as it allows easy formatting and is widely supported by various platforms,
including code repositories like GitHub.
