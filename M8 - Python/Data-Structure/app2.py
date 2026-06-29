from tkinter import *
from tkinter import messagebox

root = Tk()   

root.title("Denomination Calci")
root.geometry("400x400")

def calci():
    amount = entry_amt.get()
    if amount == "":
        messagebox.showerror(
            "Error",
            "Please enter a proper value"
        )
        return 
    
    amt = int(amount)

    notes_2000 = amt // 2000
    remaining = amt % 2000

    notes_500 = amt // 500
    remaining = amt % 500

    notes_100 = amt // 100

    result_2000.config(
        text = "2000 Note: " + str(notes_2000)    
    )

    result_500.config(
        text = "500 Note: " + str(notes_500)
    )

    result_100.config(
        text = "100 Note: " + str(notes_100)
    )

heading = Label(
    root,
    text = "Denomination Calculator",
    font = ("Arial",16, "bold" )
)
heading.pack(pady = 20) 
label_amt = Label(root, text = "enter amt")

label_amt.pack()

entry_amt = Entry(root, width = "20")

entry_amt.pack(pady = 20)

button_calci = Button(
    root, text = "Calculate" , command = calci
)

button_calci.pack(pady = 10)

result_2000 = Label(root, text = "2000 Notes: ")
result_2000.pack()
result_500 = Label(root, text = "500 Notes: ")
result_500.pack()
result_100 = Label(root, text = "100 Notes: ")
result_100.pack()

root.mainloop()