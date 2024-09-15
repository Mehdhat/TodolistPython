from tkinter import *
from tkinter import messagebox

class ToDoApp:
    def __init__(self, todolist):
        self.todolist = todolist
        todolist.title("To-Do List")
        todolist.geometry("500x450")
        todolist.resizable(0, 0)
        todolist.configure(bg="#1E1E1E")  # Dark background for the main window

        # Set the icon for the window
        todolist.iconbitmap(r'C:\Users\Admin\Downloads\pythonProject1\124.ico')  # Update this path to your .ico file

        # Create a frame for the Entry and Buttons
        self.frame = Frame(todolist, bg="#1E1E1E")
        self.frame.pack(pady=10)

        # Entry widget to input tasks (increased height)
        self.task_entry = Entry(self.frame, width=35, font=("Arial", 16), bg="#3C3F41", fg="white", insertbackground='white')
        self.task_entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Add Task Button (green background)
        self.add_task_button = Button(self.frame, text="Add Task", command=self.add_task, font=("Arial", 14), bg="#4CAF50", fg="white", relief=FLAT, width=10)
        self.add_task_button.grid(row=1, column=0, padx=5, pady=10)

        # Delete Task Button (sharp red background)
        self.delete_task_button = Button(self.frame, text="Delete Task", command=self.delete_task, font=("Arial", 14), bg="#F44336", fg="white", relief=FLAT, width=10)
        self.delete_task_button.grid(row=1, column=1, padx=5, pady=10)

        # Listbox to display tasks
        self.task_listbox = Listbox(todolist, width=45, height=10, font=("Arial", 14), selectmode=SINGLE, bg="#3C3F41", fg="white", selectbackground="#555555")
        self.task_listbox.pack(pady=20)

        # Scrollbar for the Listbox
        self.scrollbar = Scrollbar(todolist)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.task_listbox.insert(END, task)
            self.task_entry.delete(0, END)  # Clear the entry after adding
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

if __name__ == "__main__":
    root = Tk()
    todo_app = ToDoApp(root)
    root.mainloop()

