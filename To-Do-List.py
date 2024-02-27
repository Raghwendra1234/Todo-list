import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Task cannot be empty!")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showerror("Error", "Select a task to delete!")

root = tk.Tk()
root.title("To-Do List")
root.config(background="black")
root.geometry("350x450")
entry = tk.Entry(root)
add_button = tk.Button(root, text="Add Task", command=add_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
tasks_listbox = tk.Listbox(root)
entry.grid(row=0, column=0, padx=10, pady=10)
add_button.grid(row=0, column=1, padx=10, pady=10)
delete_button.grid(row=1, column=1, padx=10, pady=10)
tasks_listbox.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()
