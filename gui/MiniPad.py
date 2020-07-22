# Mini Notepad by tkinter

from tkinter import *
from tkinter import scrolledtext, messagebox
from tkinter.filedialog import askopenfile, asksaveasfile


class Pad(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("MiniPad")
        self.geometry("600x400")
        self.area = scrolledtext.ScrolledText(self)
        self.area.pack(expand=True, fill=BOTH)
        self.mbar = Menu(self)
        self.menu1 = Menu(self.mbar, tearoff=0)
        self.menu1.add_command(label="open", command=self.tryOpen)
        self.menu1.add_command(label="save", command=self.trySave)
        self.menu1.add_command(label="exit", command=self.tryClose)
        self.mbar.add_cascade(label="File", menu=self.menu1)
        self.config(menu=self.mbar)

    def tryOpen(self):
        messagebox.showinfo("Action", "Request to open a file")
        yet = askopenfile(mode="r", filetypes=[('All Files', '*.*')])
        if yet is not None:
            lines = yet.read()
            self.area.insert(1.0, lines)
            messagebox.showinfo("Open Status", "Content shown from" + yet.name)

    def trySave(self):
        messagebox.showinfo("Action", "Request to save a file")
        types = [('Python file', '*.py'), ('Java Files', '*.java'), ('C File', '*.c'),
                 ('Text File', '*.txt')]
        set = asksaveasfile(filetypes=types, defaultextension=types)
        set.write(self.area.get(1.0, END))
        messagebox.showinfo("Save Status", "Content saved in: " + set.name)

    def tryClose(self):
        messagebox.showinfo("Action", "Request to close a file")
        self.destroy()


p = Pad()
p.mainloop()
