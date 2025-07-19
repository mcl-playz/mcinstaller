# gui/app.py
import tkinter as tk
from gui.pages.serverList import ServerListPage
from gui.pages.serverView import ServerViewPage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Server Manager")
        self.geometry("600x400")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        for Page in (ServerListPage, ServerViewPage):
            pageName = Page.__name__
            frame = Page(parent=self.container, controller=self)
            self.frames[pageName] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame("ServerListPage")

    def showFrame(self, pageName):
        frame = self.frames[pageName]
        frame.tkraise()

    def getPage(self, pageName):
        return self.frames[pageName]
