from tkinter import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg.pack()

        self.clique = Button(self.widget1)
        self.clique["text"] = "Clique aqui"
        self.clique["font"] = ("Calibri", "9")
        self.clique["width"] = 10
        self.clique["command"] = self.mudarTexto
        self.clique.pack ()

    def mudarTexto(self):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"

print("####Início do programa - listagem.py####")
root = Tk()
Application(root)
root.mainloop()