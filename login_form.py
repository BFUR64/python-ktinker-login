import tkinter as tk
from tkinter import messagebox


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "12345":
        messagebox.showinfo(
            "LOGIN SUCCESSFULLY!",
            "Welcome Admin!"
        )
    else:
        messagebox.showerror(
            "LOGIN FAILED!",
            "Invalid Username and Password!"
        )


root = tk.Tk()
root.title("Login Form")
root.geometry("400x350")
root.resizable(False, False)
root.configure(bg="#24150d")

title_label = tk.Label(
    root,
    text="USER LOGIN",
    font=("Arial", 20, "bold"),
    bg="#3b2415",
    fg="#f2c879",
    relief="raised",
    bd=4
)
title_label.pack(pady=5)

username_label = tk.Label(
    root,
    text="Username",
    font=("Arial", 11),
    bg="#24150d",
    fg="#f2c879"
)
username_label.pack(pady=5)

username_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=25,
    bg="#d1b18a",
    fg="#24150d",
    insertbackground="#24150d",
    relief="sunken",
    bd=4
)
username_entry.pack(pady=5)

password_label = tk.Label(
    root,
    text="Password",
    font=("Arial", 12),
    bg="#24150d",
    fg="#f2c879"
)
password_label.pack(pady=5)

password_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=25,
    show="*",
    bg="#d1b18a",
    fg="#24150d",
    insertbackground="#24150d",
    relief="sunken",
    bd=4
)
password_entry.pack(pady=5)

login_button = tk.Button(
    root,
    text="CLAIM YOUR ACCESS NOW!!!",
    font=("Arial", 12, "bold"),
    bg="#8b3f16",
    fg="#fff0c2",
    activebackground="#b85a1b",
    activeforeground="white",
    width=25,
    relief="raised",
    bd=5,
    command=login
)
login_button.pack(pady=20)

root.mainloop()