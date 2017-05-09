# -*- coding:utf-8 -*-

from tkinter import *



#---INITIALISATION-DU-PROGRAMME---#

def __init__():
    """Initialisation du programme"""
    global bgMP, bgMJ, bgMC
    global w
    global bg_i, game_logo_i, button_jouer_i, button_comptes_i, button_quit_i
    global button_bj_i, button_rr_i, button_return_i, button_compte_empty_i, button_remove_compte_i, game_logo_little_i

    #--Création-de-la-fenêtre-graphique.-Nom-:-"w"--#
    w = Tk()
    w.title("Super TKZino2000")
    w.geometry('1280x720')
    w.resizable(width=False, height=False)


    #----------IMPORT-IMAGES----------#
        #-----Menu-Images-----#
            #---bg+Logos---#
    bg_i = PhotoImage(file="1_images/0_Menus/bg.gif")
    game_logo_little_i = PhotoImage(file="1_images/0_Menus/3_MenuC/bg_little.gif")
    game_logo_i = PhotoImage(file="1_images/0_Menus/game_logo.gif")
            #---Menu-P---#
    button_jouer_i = PhotoImage(file="1_images/0_Menus/1_MenuP/button_jouer.gif")
    button_comptes_i = PhotoImage(file="1_images/0_Menus/1_MenuP/button_comptes.gif")
    button_quit_i = PhotoImage(file="1_images/0_Menus/1_MenuP/button_quit.gif")
            #---Menu-J---#
    button_bj_i = PhotoImage(file="1_images/0_Menus/2_MenuJ/button_bj.gif")
    button_rr_i = PhotoImage(file="1_images/0_Menus/2_MenuJ/button_rr.gif")
    button_return_i = PhotoImage(file="1_images/0_Menus/2_MenuJ/button_return.gif")


    #---------Canvas-Root----------#

    bgroot = Canvas(w, width=1280, height=720)
    bgroot.create_image(0, 0, anchor="nw", image=bg_i)
    #-----ROOT-BACKGROUND-CANVAS------#
        #-----Menu-P-----#
    bgMP = Canvas(w, width=1280, height=720)
        #-----Menu-J-----#
    bgMJ = Canvas(w, width=1280, height=720)

    #----Lancement-de-l'interface-Menu-Principal----#
    MenuPrincipal()
    w.mainloop()




#--------------MENUS--------------#

def MenuPrincipal():
    """Ce menu comprend :
      - Le canvas root du Menu Principal
      - Le bouton Jouer (clic = launch MenuJouer())
      - Le bouton Comptes (clic = launch MenuAccounts())
      - Le bouton Quitter (clic = w.destroy())
      - Le logo principal du jeu
    """
    global bgMP, button_jouer, button_comptes, button_quit

    #--Background-Root--#

    bgMP.focus_set()
    bgMP.bind("<Button-1>", MouseMP)
    bgMP.pack()

    bgMP.create_image(0, 0, anchor="nw", image=bg_i) #Background
    bgMP.create_image(0, 0, anchor="nw", image=game_logo_i) #Logo du jeu

    #------Boutons-------#
    button_jouer = bgMP.create_image(537, 261, anchor=NW, image=button_jouer_i) #Bouton Jouer
    button_comptes = bgMP.create_image(537, 467, anchor=NW, image=button_comptes_i) #Bouton Comptes
    button_quit = bgMP.create_image(20, 20, anchor=NW, image=button_quit_i) #Bouton Quit



def MenuJouer():
    """Ce menu comprend :
      - Le canvas root du Menu Jouer
      - Le bouton Blackjack (clic = launch BlackJack Game)
      - Le bouton Roulette (clic = launch Roulette Game)
      - Un bouton retour au MP (clic = launch "MenuPrincipal()")
      - Le logo principal du jeu
    """
    global bgMJ, button_bj, button_rr, button_return_MJ

    #--Background-Root--#

    bgMJ.focus_set()
    bgMJ.bind("<Button-1>", MouseMJ)
    bgMJ.pack()

    bgMJ.create_image(0, 0, anchor="nw", image=bg_i) #Background
    bgMJ.create_image(0, 0, anchor="nw", image=game_logo_i) #Logo du jeu

    #------Boutons-------#
    button_bj = bgMJ.create_image(307, 337, anchor=NW, image=button_bj_i) #Bouton BlackJack
    button_rr = bgMJ.create_image(713, 337, anchor=NW, image=button_rr_i) #Bouton Roulette
    button_return_MJ = bgMJ.create_image(20, 20, anchor=NW, image=button_return_i) #Bouton Retour




#------------COMMANDES------------#

def MouseMP(event):
    """Cette commande rend fonctionnels les boutons du Menu Principal
    """

    X = event.x
    Y = event.y

    #---Hitbox-du-bouton-Jouer---#
    if 537 <= X <= 743 and 261 <= Y <= 467:
        print("## Vous avez cliqué sur le bouton Jouer ##")
        MenuJouer()
        bgMP.pack_forget()

    #---Hitbox-du-bouton-Comptes---#
    elif 537 <= X <= 743 and 467 <= Y <= 673:
        print("## Vous avez cliqué sur le bouton Comptes ##")
        import TESTS
        TESTS.MenuComptes()
        bgMP.pack_forget()

    #---Hitbox-du-bouton-Quit---#
    elif 20 <= X <= 74 and 20 <= Y <= 74:
        w.destroy()
        print("## Vous avez quitté le jeu ##")


def MouseMJ(event):
    """Cette commande rend fonctionnels les boutons du Menu Jouer
    """

    X = event.x
    Y = event.y

    #---Hitbox-du-bouton-BlackJack---#
    if 307 <= X <= 567 and 337 <= Y <= 597:
        print("## Vous avez cliqué sur le bouton BlackJack ##")
        w.destroy()
        import TESTS
        TESTS.__init__()
    #---Hitbox-du-bouton-Roulette---#
    if 713 <= X <= 973 and 337 <= Y <= 597:
        print("## Vous avez cliqué sur le bouton Roulette ##")

    #---Hitbox-du-bouton-Return---#
    elif 20 <= X <= 74 and 20 <= Y <= 74:
        MenuPrincipal()
        print("## Vous êtes retourné au Menu Principal ##")
        bgMJ.pack_forget()


__init__()


