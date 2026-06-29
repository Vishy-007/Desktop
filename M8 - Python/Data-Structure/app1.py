from tkinter import *

window = Tk()

window.title("Grids")
window.geometry("400x200")

for i in range(3):
    for j in range(3):
        frame = Tk.frame(master = window, relief = Tk.RAISED, width=2)
        frame.grid(row=i, column = j, padx = 5, pady = 5)
        label = Tk.Label(master=frame, text = f'Row{i} Col{j}',width = 12, height = 4)
        label.pack() 

window.mainloop()