#
#
from tkinter import *
import sys

button_list = []


def __init__():
    global fenetre
    #Initialization of the game mechanics
    fenetre = Tk()
    master = Canvas(fenetre, width=1280, height=720)
    master.focus_set()
    master.bind("<Key>", clavier)
    master.pack()
    fenetre.mainloop()


def MenuOne():
    global PlayB, AccountsB, OptionsB, QuitB
    #Création des boutons
    PlayB = Canvas(fenetre, width=96, height=96, bg="yellow", padx=200, pady=0)
    AccountsB = Canvas(fenetre, width=96, height=96, bg="yellow", padx=200, pady=96)
    OptionsB = Canvas(fenetre, width=96, height=96, bg="yellow", padx=200, pady=96)
    QuitB = Canvas(fenetre, width=96, height=96, bg="yellow", padx=200, pady=96)

    #Apparition des boutons
    PlayB.pack()
    AccountsB.pack()
    OptionsB.pack()
    QuitB.pack()

    #Ajout des boutons dans la liste "button_list"
    button_list.append(PlayB)
    button_list.append(AccountsB)
    button_list.append(OptionsB)
    button_list.append(QuitB)

def kill(self, object):
    """supprimer tous les boutons étant dans button_list"""
    object.pack_forget()
    button_list.remove(object)


def clavier(event):
    touche = event.keysym
    if touche == "Return" or touche == "Spacebar":
        play()
    elif touche == "Escape":
        sys.exit("THE GAME IS OVER MUAHAHAHAHAHAHA")


def play():
    print("You've pressed play")
    for node in button_list:
        if node.get("name") in button_list:
            print("all the menu one buttons have been deleted")
            kill(PlayB)
            kill(AccountsB)
            kill(OptionsB)
            kill(QuitB)

__init__()
MenuOne()
