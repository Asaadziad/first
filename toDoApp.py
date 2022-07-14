import tkinter as tk
from tkinter import Button, Canvas, Entry, Frame, Label, StringVar, Toplevel,ttk
from typing import Text

root = tk.Tk()
root.title("Daddy's toDo App")
root.geometry("400x400")
root.resizable(False,False)
root.columnconfigure(0, weight=4)
root.columnconfigure(1,weight=1)
frame = Frame(root)
frame.grid(column=0,row=0,padx=10,pady=10)
frame2 = Frame(root)
frame2.grid(column=0,row=1,padx=10,pady=10)
frame3 = Frame(root)
frame3.grid(column=1,row=0,padx=10,pady=10)

#Arguments:
#Frame f
#Functionality: clears frame
def clear_widget(f):
    for widget in f.winfo_children():
        widget.destroy()

def update():
    clear_widget(frame2)
    label2 = Label(frame2, text="Tasks to do:",justify="center").pack()
    file = open("test.txt", "r")
    text_file = Label(frame2, text=file.read(),justify="center").pack()
    file.close()

def addText():
    file_text = open("test.txt", "a")
    file_text.write(entry1.get()+'\n')
    file_text.close()
    entry1.delete(0, 'end')
    update()

def clearText():
    file_text = open("test.txt", "r+")
    file_text.truncate(0)
    file_text.close()
    update()


label = Label(frame, text="add your next task:",justify="center",pady=10).pack()

update()

entry1 = Entry(frame,justify="center")
entry1.pack()

button1 = Button(frame,text="add me daddy",justify="center",command=addText)
button1.pack()
button2 = Button(frame3,text="clear me daddy",justify="center",fg="red",command=clearText)
button2.pack()

root.mainloop()
