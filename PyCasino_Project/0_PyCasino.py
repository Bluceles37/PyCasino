 # -*- coding:utf-8 -*-

from tkinter import *


#---INITIALISATION-DU-PROGRAMME---#

def __init__():
    """Initialisation du programme"""
    global w, bgMP, bgMJ, bgMC, bg_i, game_logo_i, button_jouer_i, button_comptes_i, button_quit_i, button_bj_i, button_rr_i, button_return_i, button_compte_empty_i, button_remove_compte_i

    #--Création-de-la-fenêtre-graphique.-Nom-:-"w"--#
    w = Tk()
    w.title("Super TKZino2000")
    w.geometry('1280x720')
    w.resizable(width=False, height=False)
    w.bind("<Motion>", mouse_pos)

    #----------IMPORT-IMAGES----------#
        #-----Menu-Images-----#
            #---bg+Logos---#
    bg_i = PhotoImage(file="1_images/0_Menus/bg.gif")
    game_logo_i = PhotoImage(file="1_images/0_Menus/game_logo.gif")
            #---Menu-P---#
    button_jouer_i = PhotoImage(file="1_images/0_Menus/1_MenuP/button_jouer.gif")
    button_comptes_i = PhotoImage(file="1_images/0_Menus/1_MenuP/button_comptes.gif")
    button_quit_i = PhotoImage(file="1_images/0_Menus/1_MenuP/button_quit.gif")
            #---Menu-J---#
    button_bj_i = PhotoImage(file="1_images/0_Menus/2_MenuJ/button_bj.gif")
    button_rr_i = PhotoImage(file="1_images/0_Menus/2_MenuJ/button_rr.gif")
    button_return_i = PhotoImage(file="1_images/0_Menus/2_MenuJ/button_return.gif")
            #---Menu-C---#
    button_compte_empty_i = PhotoImage(file="1_images/0_Menus/3_MenuC/button_compte_empty.gif")
    button_remove_compte_i = PhotoImage(file="1_images/0_Menus/3_MenuC/button_remove_compte.gif")

    #-----ROOT-BACKGROUND-CANVAS------#
        #-----Menu-P-----#
    bgMP = Canvas(w, width=1280, height=720)
        #-----Menu-J-----#
    bgMJ = Canvas(w, width=1280, height=720)
        #-----Menu-C-----#
    bgMC = Canvas(w, width=1280, height=720)

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
    bgMJ.pack_forget()
    bgMC.pack_forget()

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
    bgMP.pack_forget()

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


def MenuComptes():
    """Ce menu comprend :
      - Le canvas root du Menu Comptes
      - 3 emplacements de comptes :
        - clic sur compte existant --> charge le compte
        - double-clic sur compte existant --> charge le compte et retour au menu principal
        - clic sur compte vide --> lance sous-menu "Créer Compte()"
      - Un bouton |-| pour supprimer un compte existant (clic = launch sous-menu "Supprimer Compte()")
      - Un bouton retour au MP (clic = launch "MenuPrincipal()")
      - Le logo principal du jeu
    """
    global button_compte1, button_compte2, button_compte3, button_return_MC, button_remove_compte
    bgMP.pack_forget()

    #--Background-Root--#

    bgMC.focus_set()
    bgMC.bind("<Button-1>", MouseMC)
    bgMC.pack()

    bgMC.create_image(0, 0, anchor="nw", image=bg_i) #Background
    bgMC.create_image(0, 0, anchor="nw", image=game_logo_i) #Logo du jeu

    #------Boutons-------#
    button_compte1 = bgMC.create_image(84, 192, anchor=NW, image=button_compte_empty_i) #Bouton Compte1
    button_compte2 = bgMC.create_image(487, 192, anchor=NW, image=button_compte_empty_i) #Bouton Compte2
    button_compte3 = bgMC.create_image(893, 192, anchor=NW, image=button_compte_empty_i) #Bouton Compte3
    button_remove_compte = bgMC.create_image(592, 583, anchor=NW, image=button_remove_compte_i) #Bouton remove compte
    button_return_MC = bgMC.create_image(20, 20, anchor=NW, image=button_return_i) #Bouton Retour


#------------COMMANDES------------#

def mouse_pos(event):
   global X, Y
   X = event.x
   Y = event.y

def MouseMP(event):
    """Cette commande rend fonctionnels les boutons du Menu Principal
    """
    #---Hitbox-du-bouton-Jouer---#
    if 537 <= X <= 743 and 261 <= Y <= 467:
        print("## Vous avez cliqué sur le bouton Jouer ##")
        MenuJouer()

    #---Hitbox-du-bouton-Comptes---#
    elif 537 <= X <= 743 and 467 <= Y <= 673:
        print("## Vous avez cliqué sur le bouton Comptes ##")
        MenuComptes()

    #---Hitbox-du-bouton-Quit---#
    elif 20 <= X <= 74 and 20 <= Y <= 74:
        w.destroy()
        print("## Vous avez quitté le jeu ##")


def MouseMJ(event):
    """Cette commande rend fonctionnels les boutons du Menu Jouer
    """
    #---Hitbox-du-bouton-BlackJack---#
    if 307 <= X <= 567 and 337 <= Y <= 597:
        print("## Vous avez cliqué sur le bouton BlackJack ##")

    #---Hitbox-du-bouton-Roulette---#
    if 713 <= X <= 973 and 337 <= Y <= 597:
        print("## Vous avez cliqué sur le bouton Roulette ##")

    #---Hitbox-du-bouton-Return---#
    elif 20 <= X <= 74 and 20 <= Y <= 74:
        MenuPrincipal()
        print("## Vous êtes retourné au Menu Principal ##")


def MouseMC(event):
    """Cette commande rend fonctionnels les boutons du Menu Jouer
    """
    #---Hitbox-du-bouton-Compte1---#
    if 84 <= X <= 393 and 192 <= Y <= 545:
        print("## Vous avez cliqué sur le bouton Compte1 ##")

    #---Hitbox-du-bouton-Compte2---#
    elif 487 <= X <= 796 and 192 <= Y <= 545:
        print("## Vous avez cliqué sur le bouton Compte2 ##")

    #---Hitbox-du-bouton-Compte3---#
    elif 893 <= X <= 1202 and 192 <= Y <= 545:
        print("## Vous avez cliqué sur le bouton Compte3 ##")

    #---Hitbox-du-bouton-Remove-Compte---#
    elif 592 <= X <= 583 and 690 <= Y <= 682:
        print("## Vous avez cliqué sur le bouton remove compte ##")

    #---Hitbox-du-bouton-Return---#
    elif 20 <= X <= 74 and 20 <= Y <= 74:
        MenuPrincipal()
        print("## Vous êtes retourné au Menu Principal ##")



##=========================================##
##------PARTIE-EXÉCUTION-DU-PROGRAMME------##
##=========================================##

__init__()
