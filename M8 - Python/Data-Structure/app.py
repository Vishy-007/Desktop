from tkinter import *

window = Tk()
window.title("My First Window")
window.geometry("400x200")
f_label = Label(text="My GUI application", fg="black", bg="white")
f_button = Button(text="Click me, close your eyes and click me", fg="yellow", bg="green")
f_entry = Entry(fg = 'black', bg='blue', width="20")

f_label.pack()
f_button.pack()
f_entry.pack()
window.mainloop()