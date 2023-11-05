# Sticky Notes

Sticky Notes is a simple to-do program developed in Python using the Tkinter framework.

## Functions

- **Adding tasks**: New tasks can be added by clicking on the "+" button.
- **Marking tasks as completed**: Each task has a checkbox that can be clicked to mark the task as completed.
- **Saving tasks**: By clicking on the "Save" button, all tasks are saved in a `.pkl` file.
- **Load tasks**: Clicking on the "Load" button loads all tasks from the `.pkl` file.

## Starting the program

To start the program, simply execute the Python script:

```sh
python main.py
```

Make sure that you have installed Python and Tkinter on your system.

## Notes

This program uses the `pickle` module to save and load the tasks. 
Please note that `pickle` is not secure against erroneous or maliciously constructed data. 
Only use it to load data that you have saved yourself and that you trust.