import tkinter as tk
from tkinter import messagebox, font
import tkinter.ttk as ttk

def validate_login():
    userid = username_entry.get()
    password = password_entry.get()
    if userid == "Oguess" and password == "hello world":
        messagebox.showinfo("Login Successful", "Welcome, Oguess!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to re-center and resize the login frame upon window resize
def resize_widgets(event=None):
    window_width = parent.winfo_width()
    window_height = parent.winfo_height()
    frame_width = login_frame.winfo_reqwidth()
    frame_height = login_frame.winfo_reqheight()
    x = int((window_width - frame_width) / 2)
    y = int((window_height - frame_height) / 2)
    login_frame.place(x=x, y=y)

    # Resize the font based on the window size
    new_font_size = max(int(min(window_width, window_height) / 25), 8)  # Minimum font size of 8
    login_font.config(size=new_font_size)

# Create the main window
parent = tk.Tk()
parent.title("Login Form")

# Set the size of the windows and make it resizable
parent.geometry("800x600")
parent.resizable(True, True)

# Create a frame to contain the login widgets
login_frame = ttk.Frame(parent)
login_frame.pack()

# Create a font object for the labels
login_font = font.Font(family='Helvetica', size=12)

# Bind the event to re-center and resize the frame when the window is resized
parent.bind('<Configure>', resize_widgets)

# Create and place the username label and entry within the frame
username_label = ttk.Label(login_frame, text="User ID:", font=login_font)
username_label.pack()
username_entry = tk.Entry(login_frame)
username_entry.pack()

# Create and place the password label and entry within the frame
password_label = tk.Label(login_frame, text="Password:", font=login_font)
password_label.pack()
password_entry = tk.Entry(login_frame, show="*")  # Show asterisks for password
password_entry.pack()

# Create and place the login button within the frame
login_button = tk.Button(login_frame, text="Login", command=validate_login, font=login_font)
login_button.pack()

# Call the resize_widgets function to center the login frame initially
resize_widgets()

# Start the Tkinter event loop
parent.mainloop()
