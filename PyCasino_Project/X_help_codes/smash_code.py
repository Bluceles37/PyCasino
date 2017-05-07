# -*- coding:utf-8 -*-

from tkinter import *

def menu():
    global menu, bt_jouer, bt_options, bt_quitter, txt_jouer, txt_options, txt_quitter
    if menu_actif:
        menu = canvas.create_image(0, 0, anchor="nw", image=fond_menu)
        bt_jouer = canvas.create_rectangle(408, 287, 672, 363, fill='red', activefill='blue')
        txt_jouer = canvas.create_text(540, 325, text="Jouer", font='Helvetica 50', state="disabled")
        bt_options = canvas.create_rectangle(408, 386, 672, 462, fill='red', activefill='blue')
        txt_options = canvas.create_text(540, 424, text="Options", font='Helvetica 50', state="disabled")
        bt_quitter = canvas.create_rectangle(408, 485, 672, 561, fill='red', activefill='blue')
        txt_quitter = canvas.create_text(540, 523, text="Quitter", font='Helvetica 50', state="disabled")


def souris(event):
    """Gère les événements souris"""
    global menu_actif
    # Si le clic s'effectue au niveau du bouton "Jouer"
    if menu_actif:
        if ((408 <= event.x <= 672) and (287 <= event.y <= 363)):
            print("Clic sur Jouer")
            menu_actif = False
            canvas.delete(menu, bt_jouer, bt_options, bt_quitter, txt_jouer, txt_options, txt_quitter)
        elif ((408 <= event.x <= 672) and (386 <= event.y <= 462)):
            print("Clic sur Options")
        # Si le clic s'effectue au niveau du bouton "Quitter"
        elif ((408 <= event.x <= 672) and (485 <= event.y <= 561)):
            fenetre.destroy()

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("PyCasino")
fenetre.geometry("1080x720")
fenetre.resizable(width=False, height=False)

# Création du canvas
canvas = Canvas(fenetre, width="1080", height="720", bg="white")
canvas.focus_set()
canvas.bind("<Button-1>", souris)
canvas.pack()

# Variables globales
menu_actif = True


# Création de l'interface du menu
fond_menu = PhotoImage(file="../1_images/0_Menus/bg.gif")
menu()

# Boucle principale
fenetre.mainloop()
