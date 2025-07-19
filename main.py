# main.py
from gui.app import App
from server import Server
from paper import Paper

paper = Paper()

if __name__ == "__main__":
    testServer = Server(paper, "1.21", 130, "test", 25565)
    testServer.install()

    app = App()
    app.mainloop()