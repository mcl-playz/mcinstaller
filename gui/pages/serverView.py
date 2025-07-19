import tkinter as tk

class ServerViewPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.serverNameLabel = tk.Label(self, text="", font=("Arial", 14))
        self.serverNameLabel.pack(pady=10)

        self.infoLabel = tk.Label(self, text="Server info goes here", font=("Arial", 10))
        self.infoLabel.pack()

        tk.Button(self, text="Back", command=lambda: controller.showFrame("ServerListPage")).pack(pady=10)

    def loadServer(self, server):
        self.serverNameLabel.config(text=f"Server: {server}")
        self.infoLabel.config(text=f"{server} settings and controls coming soon.")
