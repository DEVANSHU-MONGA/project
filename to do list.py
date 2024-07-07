from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("To-Do List")
root.geometry("570x700")
root.resizable(False,False)
root.config(bg="orange")

def add_task(event=None):
    global messagebox
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(END, task)
        task_entry.delete(0,END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    global messagebox
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def clear_tasks():
    tasks_listbox.delete(0, END)

task_entry = Entry(root, width=30,bg="powder blue",font=("arial 25 bold"),bd=9,fg="black",)
task_entry.pack(pady=20)
task_entry.bind("<Return>", add_task)

add =Button(root, text="Add Task", font=("arial 15 bold"),bd=9,fg="#fff",bg="#2a2d36",command=add_task)
add.pack(pady=5)

tasks_listbox = Listbox(root, width=35,font=("arial 15 bold"),bd=9,bg="yellow", height=15)
tasks_listbox.pack(pady=10)

delete = Button(root, text="Delete Task",font=("arial 15 bold"),bd=9,fg="#fff",bg="#2a2d36", command=delete_task)
delete.pack(pady=5)

clear =Button(root, text="Clear All Tasks",font=("arial 10 bold"),bd=9,fg="#fff",bg="#3697f5",command=clear_tasks)
clear.pack(pady=5)

root.mainloop()
