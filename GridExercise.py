from tkinter import *
import tkinter.messagebox as msgBox

window = Tk()
window.title("Grid Exercise")
window.geometry("550x250")
window.configure(bg="seagreen")

img = PhotoImage(file="GreenTreePython.gif")
imgLbl = Label(window, image=img, bg="green")

def show_info(lesson_number):
	msgBox.showinfo("Lesson Selected", "You selected Lesson " + str(lesson_number))

buttons = []
for i in range(6):
    button = Button(window, text="LESSON " + str(i + 1), bg="yellow", padx=10, pady=10,
                    command=lambda i=i: show_info(i + 1))
    buttons.append(button)

imgLbl.grid(row=0, column=0, rowspan=2, padx=20, pady=20)

for i in range(3):
	buttons[i].grid(row=0, column=i + 1, padx=10, pady=10)

for i in range(3, 6):
	buttons[i].grid(row=1, column=(i - 3) + 1, padx=10, pady=10)

window.mainloop()
