import tkinter as tk
from tkinter import Label, ttk
from turtle import width

class engine(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To Do App")
        self.geometry("300x400")

        self.input_label = Label(self, text="To Do Next:")
        self.input_label.grid(column=0,row=0)


if __name__ == "__main__":
    app = engine()
    app.mainloop()