import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from tkinter import PhotoImage as image

def validate_login():
    userid = username_entry.get()
    password = password_entry.get()
    # Here you can add your own validation logic or database check
    if userid == "Oguess" and password == "hello world":
        messagebox.showinfo("Login Successful", "Welcome, Oguess!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
parent = tk.Tk()
parent.title("Login Form")

# set the size of the windows and make it resizable
parent.geometry("800x600")
parent.resizable(True,True)

# set background image
bg = image(file = "bg.jpg")

bg_label = tk.Label(parent, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create and place the username label and entry
username_label = ttk.Label(parent, text="User ID:")
username_label.pack()
username_entry = tk.Entry(parent)
username_entry.pack()

# Create and place the password label and entry
password_label = tk.Label(parent, text="Password:")
password_label.pack()
password_entry = tk.Entry(parent, show="*")  # Show asterisks for password
password_entry.pack()

# Create and place the login button
login_button = tk.Button(parent, text="Login", command=validate_login)
login_button.pack()

# Start the Tkinter event loop
parent.mainloop()
