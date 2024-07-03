import tkinter as tk
from tkinter import messagebox

def show_password():
    password = entry.get()
    messagebox.showinfo("Password", "The password entered is: {}".format(password))

window = tk.Tk()
window.title("Password Checker")
window.configure(bg="light blue")
window.geometry("400x200")

entry = tk.Entry(window, show="*")
entry.pack(pady=10)

check_button = tk.Button(window, text="CHECK", bg="dark green", fg="white", command=show_password)
check_button.pack(pady=10, padx=10)

window.mainloop()