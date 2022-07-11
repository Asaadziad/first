import tkinter as tk
from tkinter import Frame,ttk

from Player import Player

    
class loadPlayer(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.createPlayer()

    def createPlayer(self):
        p = Player("Asaad")
        ttk.Label(self, text=p.getName()).grid(column=0,row=2)

class mainFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        
        self.widgets()
    
    def widgets(self):
        ttk.Button(self, text='Replace').grid(column=0, row=0)


class engine(tk.Tk):
    def __init__(self):
        super().__init__()
        self.widgets()
        self.title("App")
        self.geometry("900x600")
        self.resizable(False,False)
    
    def widgets(self):
        loggedIn = False
        while loggedIn:
            main_frame = mainFrame(self) 
            main_frame.grid(column=0,row=0)
            load_players = loadPlayer(self)
            load_players.grid(column=0,row=1)
        ttk.Label(self, text="Please Login or Register").grid(column=0,row=0)
        ttk.Button(self, text="Login").grid(column=0,row=1)
        ttk.Button(self, text="Register").grid(column=1,row=1)

if __name__ == "__main__":

    app = engine()
    app.mainloop()