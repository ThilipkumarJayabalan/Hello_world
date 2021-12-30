
# from future.moves import tkinter
from tkinter import *

# from Radiobutton import label

'''
# import tkinter
class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

root = Tk()
# L = Label(root, text="Does it work")
# L.pack()
root.title("Does it work?")
l = Label(root)
l.pack()
# app = Window(root)
# root.mainloop()


from tkinter import *
from tkinter import ttk
root = Tk()
ttk.Button(root, text="Hello World").grid()
root.mainloop()
'''
root = Tk()


class First:
    def __init__(self, select):
        self.selection = select

    def sel(self):
        self.selection = "Selected Option" + str(var.get())
        label.config(text=self.selection)


var = IntVar()
Obj = First(str(var.get()))
Label(root, text="Does it work?").pack()
Radiobutton(root, text="Software1", variable=var, value=1, command=Obj.sel).pack()
Radiobutton(root, text="Software2", variable=var, value=2, command=Obj.sel).pack()
# Radiobutton(root, text="Exit Software3", pady=2).pack()


def client_exit():
    # exit()
    root.destroy()
    pass


Button(root, text="Submit Software", padx=111, pady=20, command=client_exit).pack()
# R1.place(x=111, y=800)
# R1.pack()

# quitButton.place()
# quitButton.pack()
label = Label(root)
root.title("MyFirstApplication")
# root.iconbitmap(default='Any')

root.geometry("1200x720")
root.iconbitmap()
label.pack()
root.mainloop()
