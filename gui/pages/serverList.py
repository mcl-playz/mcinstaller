import tkinter as tk
from server import ServerManager
from tkinter import ttk
import os

class ServerListPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Servers", font=("Arial", 16)).pack(pady=10)

        self.serverListbox = tk.Listbox(self)
        self.serverListbox.pack(fill="both", expand=True, padx=20, pady=10)

        # Dummy server names
        self.servers = ServerManager.getServers()
        for s in self.servers:
            self.serverListbox.insert(tk.END, s)

        tk.Button(self, text="View Server", command=self.viewServer).pack(pady=5)
        tk.Button(self, text="Create Server", command=self.createServer).pack(pady=5)

    def viewServer(self):
        selection = self.serverListbox.curselection()
        if not selection:
            return
        serverName = self.serverListbox.get(selection[0])
        serverPage = self.controller.getPage("ServerViewPage")
        serverPage.loadServer(serverName)
        self.controller.showFrame("ServerViewPage")

    def createServer(self):
        # Add logic to create new server
        pass
