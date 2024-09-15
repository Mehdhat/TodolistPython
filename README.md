# To-Do List Application

## Overview

This is a simple To-Do list application built using Python's Tkinter library. The application allows users to add and delete tasks. The user interface features a dark theme with a modern design.

## Features

- **Add Task**: Input a task and add it to the list.
- **Delete Task**: Select a task from the list and delete it.
- **Scrollable Listbox**: View tasks in a scrollable listbox.

## Installation

1. Ensure you have Python installed on your system.
2. Install the Tkinter library if it is not already included with your Python installation.

## Usage

1. Save the provided code into a file named `todo_app.py`.
2. Run the script using Python:

    ```bash
    python todo_app.py
    ```

3. A window will open with a dark-themed To-Do list application.

## Code Details

- **Window Title**: "To-Do List"
- **Window Size**: 500x450 pixels
- **Background Color**: Dark grey (#1E1E1E)
- **Task Entry Field**: 
  - Font: Arial, 16
  - Background: Dark grey (#3C3F41)
  - Foreground: White
- **Add Task Button**:
  - Color: Green (#4CAF50)
  - Font: Arial, 14
- **Delete Task Button**:
  - Color: Red (#F44336)
  - Font: Arial, 14
- **Listbox**:
  - Font: Arial, 14
  - Background: Dark grey (#3C3F41)
  - Foreground: White

## Dependencies

- Python 3.x
- Tkinter (comes with Python standard library)

## Icon

The application uses an icon file. Update the path in the script to the location of your `.ico` file.

```python
todolist.iconbitmap(r'C:\Users\Admin\Downloads\pythonProject1\124.ico')
