import tkinter as tk
from tkinter import Button, Canvas, Entry, Frame, Label, StringVar, Toplevel,ttk

root = tk.Tk()
root.title("Daddy's toDo App")
root.geometry("400x400")
canvas = Canvas(root)
canvas.pack()

def addText():
    file_text = open("test.txt", "a")
    file_text.write(entry1.get()+'\n')
    entry1.delete(0, 'end')

label = Label(root, text="add your next task").pack()
canvas.create_rectangle(30, 10, 350, 80,
    outline="#fb0", fill="#fb0")
canvas.create_text(190, 45, text="Welcome home daddy")

file1 = open("test.txt", "r")

canvas.create_text(190, 100, text="List of things to do:")
j = 0
for i,line in enumerate(file1):
    canvas.create_text(190, 125+j, text=str(i)+") "+line)
    j = j+20

file1.close()

label1= Label(root, text="Description:",padx=10)
label1.pack()
entry1 = Entry(root)
entry1.pack()

button1 = Button(root,text="add me daddy",command=addText)
button1.pack()

root.mainloop()
