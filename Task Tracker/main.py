import tkinter
import threading
from tkinter import messagebox
import sys

# Global variables
tasks = []
timer = threading
real_timer = threading
ok_thread = True

# Function to handle user input and add tasks to the list
def get_entry(event=""):
    text = todo.get()
    minutes = int(time.get())
    todo.delete(0, tkinter.END)
    time.delete(0, tkinter.END)
    todo.focus_set()
    add_list(text, minutes * 60)  # convert minutes to seconds
    if 0 < minutes < 999:
        update_list()

# Function to add a task to the list and start a timer thread for it
def add_list(text, seconds):
    tasks.append([text, seconds])
    timer = threading.Timer(seconds, time_passed, [text])
    timer.start()

# Function to update the listbox with the remaining time for each task
def update_list():
    if todolist.size() > 0:
        todolist.delete(0, "end")
    for task in tasks:
        minutes, seconds = divmod(task[1], 60)
        todolist.insert("end", "[{}] Time left: {} minutes {} seconds".format(task[0], minutes, seconds))

# Function to handle when the time for a task has passed
def time_passed(task):
    tkinter.messagebox.showinfo("Notification", "Time for: " + task)

# Function for the real-time countdown of tasks
def real_time():
    if ok_thread:
        real_timer = threading.Timer(1.0, real_time)
        real_timer.start()
    for task in tasks:
        if task[1] == 0:
            tasks.remove(task)
        task[1] -= 1
    update_list()

if __name__ == '__main__':
    # Create the main application window
    app = tkinter.Tk()
    app.geometry("480x680")
    app.title("Todolist Remainder")
    app.rowconfigure(0, weight=1)

    # Create a frame
    frame = tkinter.Frame(app)
    frame.pack()

    # Create widgets
    label = tkinter.Label(app, text="Enter work to do:",
                          wraplength=200,
                          justify=tkinter.LEFT)
    label_hour = tkinter.Label(app, text="Enter time (minutes)",
                               wraplength=200,
                               justify=tkinter.LEFT)
    todo = tkinter.Entry(app, width=30)
    time = tkinter.Entry(app, width=15)
    send = tkinter.Button(app, text='Add task', fg="#ffffff", bg='#6186AC', height=3, width=30, command=get_entry)
    quit = tkinter.Button(app, text='Exit', fg="#ffffff", bg='#EB6464', height=3, width=30, command=app.destroy)
    todolist = tkinter.Listbox(app)
    if tasks != "":
        real_time()

    # Bind the Enter key to the get_entry function
    app.bind('<Return>', get_entry)

    # Place widgets in the window
    label.place(x=0, y=10, width=200, height=25)
    label_hour.place(x=235, y=10, width=200, height=25)
    todo.place(x=62, y=30, width=200, height=25)
    time.place(x=275, y=30, width=50, height=25)
    send.place(x=62, y=60, width=50, height=25)
    quit.place(x=302, y=60, width=50, height=25)
    todolist.place(x=60, y=100, width=300, height=300)

    # Start the Tkinter main loop
    app.mainloop()

    # Stop the real-time thread and exit the program
    ok_thread = False
    sys.exit("FINISHED")
