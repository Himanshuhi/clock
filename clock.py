from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("clock")

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

lbl = Label(root, font = ('calibri', 40, 'roman'), background = 'black' , foreground = 'cyan')
lbl.pack(anchor='center')
time()

mainloop()


import fontstyle
text = fontstyle.apply('himanshu', 'bold/Italic/red/GREEN_BG')
print(text)
