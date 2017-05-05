#
#
from tkinter import *
import sys

button_list = []




class button:
    def create(self, chosen_name, h, w, image, action):
        self.name = {"name", chosen_name}
        button = Canvas(fenetre, width=w, height=h, bg=image)
        button.focus_set()
        button.bind("<Button-1>", action)
        button.pack()
        button_list.append(chosen_name)

    def killall(self):
        """supprimer tous les boutons étant dans button_list"""
        

def __init__():
    #Initialization of the game mechanics
    fenetre = Tk()
    master = Canvas(fenetre, width=1280, height=720, bg='grey')
    master.focus_set()
    master.bind("<Key>", clavier)
    master.pack()
    fenetre.mainloop()

def clavier(event):
    touche = event.keysym
    if touche == "Return" or touche == "Spacebar":
        play()
    elif touche == "Escape":
        sys.exit("THE GAME IS OVER MUAHAHAHAHAHAHA")


def play():
    for node in button_list:
        if node.get("name") in button_list:
            button.killall()




