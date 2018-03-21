from Tkinter import *
import tkMessageBox

def reply():
    tkMessageBox.showinfo(title='popup',message='Button pressed!"')

window = Tk()
button = Button(window,text='press',command=reply)

button.pack()
window.mainloop()
