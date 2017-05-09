from random import *
from tkinter import *
import sqlite3
import sys
import Menus

conn = sqlite3.connect('bdd.db')
cursor = conn.cursor()
#--------------------------------------------CARTES----------------------------------------------------#
couleur = ["pique", "trefle", "carreau", "coeur"]
rang = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "Dix", "Valet", "Dame", "Roi"]
deck = []
deck2 = []
#--------------------------------------------CROUPIER--------------------------------------------------#
main_c = []
main_c_value = []
#--------------------------------------------JOUEUR----------------------------------------------------#
main_j = []
main_j_value = []
main_j_total = 0
win_j2 = 0
win_j2_equal = 0
mise_j = 0
replay_j = 1
pass_ok = 0
money = 0
xp = 0
xp_need = 0
mise_possible = 0
#-------------------------------------------COMPTEURS--------------------------------------------------#
x1 = 0
x2 = 0
x3 = 0
x4 = 0
want_draw = 0
win = 0
ended = 0
nbtour = 1
nbr_jeu = 1
replay = 1
want_draw_possible = 1

def __init__():
    global pass_ok, money, xp, level
    global user1, pseudo, pseudo2, pass_test, pass_result, pass1, creation, level, response

    global bg_i, game_logo_little_i, game_logo_i, button_jouer_i, button_comptes_i, button_quit_i
    global button_bj_i, button_rr_i, button_return_i, load_compte_i, add_compte_i, c_title_i

    global w, bgBJ, bgMC, bgMP_L


    #--Création-de-la-fenêtre-graphique.-Nom-:-"w"--#
    w = Tk()
    w.title("Super TKZino2000 - BlackJack")
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
            #---Menu-C---#
    load_compte_i = PhotoImage(file="1_images/0_Menus/3_MenuC/load_compte.gif")
    add_compte_i = PhotoImage(file="1_images/0_Menus/3_MenuC/add_compte.gif")
    c_title_i = PhotoImage(file="1_images/0_Menus/3_MenuC/c_title.gif")

    bgBJ = Canvas(w, width=1280, height=720)
    bgMC = Canvas(w, width=1280, height=720)
    bgMP_L = Canvas(w, width=1280, height=720)

    bgBJ.create_image(0, 0, anchor="nw", image=bg_i)
    bgBJ.pack()

    w.mainloop()

    #--------------------------------------BDD--------------------------------------------#
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            pseudo TEXT,
            password TEXT,
            level INTEGER,
            xp INTEGER,
            xpneed INTEGER,
            money INTEGER);''')

    cursor.execute("""SELECT pseudo FROM users""")
    user1 = cursor.fetchall()

    pseudo = input("Entrez votre pseudo")
    print("Votre pseudo est : ", pseudo)
    pseudo2 = (pseudo,)

    if pseudo2 in user1:
        while pass_ok == 0:
            cursor.execute("""SELECT password FROM users WHERE pseudo=?""", (pseudo,))
            pass_test = cursor.fetchall()
            pass_result = str(pass_test[0][0])
            pass1 = input("Entrez votre mot de passe")
            if pass1 == pass_result:
                print("Bonjour",pseudo)
                pass_ok += 1
            else:
                print("Mauvais mot de passe")
    else:
        creation = int(input("Ce pseudo n'existe pas, voulez vous creer un compte ? 1 = Oui, 0 = Non"))
        if creation == 1:
            pass2 = input("Choisissez un mot de passe")
            cursor.execute('''INSERT INTO users(pseudo, password, level, xp, xpneed, money) VALUES (?, ?, ?, ?, ?, ?);''', (pseudo, pass2, 1, 0, 100, 500))
            conn.commit()
        else:
            sys.exit("Aurevoir")

    cursor.execute("""SELECT level FROM users WHERE pseudo=?""", (pseudo,))
    level = int(cursor.fetchone()[0])

    print("Vous etes niveau", level)

    cursor.execute("""SELECT money FROM users WHERE pseudo=?""", (pseudo,))
    response = cursor.fetchone()
    money += int(response[0])
    #--------------------------------------LEVELS--------------------------------------------#
    cursor.execute("""SELECT xp FROM users WHERE pseudo=?""", (pseudo,))
    xp += int(cursor.fetchone()[0])
    #------------------------------------Launch-Game-----------------------------------------#
    game()
    db.close()




def level_up():
    global level, xp, xp_need
    while xp > xp_need:
        xp_need -= xp_need
        cursor.execute("""SELECT xpneed FROM users WHERE pseudo=?""", (pseudo,))
        xp_need += int(cursor.fetchone()[0])
        if xp >= xp_need:
            level += 1
            cursor.execute("""UPDATE users SET level = ? WHERE pseudo =?""", (level, pseudo))
            conn.commit()
            xp_need = (xp_need*1.5)+100
            cursor.execute("""UPDATE users SET xpneed = ? WHERE pseudo =?""", (xp_need, pseudo))
            conn.commit()
            print("Vous êtes monté de niveau ! Vous êtes maintenant niveau", level, ". Il vous manque", (int(xp_need)-xp), "d'xp pour passer niveau", level+1, ".")
#--------------------------------------CONSTRUCTION DU DECK--------------------------------------------#
def deck_construction():
    while len(deck2) < 52:
        self_rang = choice(rang)
        self_couleur = choice(couleur)
        self_carte = self_rang + " de " + self_couleur
        deck.append(self_carte)
        [deck2.append(n) for n in deck if n not in deck2]
        deck2.sort()
#--------------------------------------DISTRIBUTION DES CARTES-----------------------------------------#
def distrib():
    global x1, x2
    while x1 < 1:
        main_c_pop = deck2.pop()
        main_c.append(main_c_pop)
        x1 += 1
    while x2 < 2:
        main_j_pop = deck2.pop()
        main_j.append(main_j_pop)
        x2 += 1

def distrib_j_2():
    global x3
    while x3 < 1:
        main_j_pop = deck2.pop()
        main_j.append(main_j_pop)
        x3 += 1
    x3 = 0

def distrib_c_2():
    global x4
    while x4 < 1:
        main_c_pop = deck2.pop()
        main_c.append(main_c_pop)
        x4 += 1
    x4 = 0

def draw_card():
    global want_draw, ended, nbtour, want_draw_possible
    while want_draw_possible == 1:
        want_draw = int(input("Voulez-vous tirer une carte supplémentaire ? (1 = Oui, 0 = Non)"))
        if want_draw == 1:
           want_draw_possible -= 1
           jump()
           show_draw()
           distrib_j_2()
           reset_value()
           nbtour += 1
        if want_draw == 0:
           want_draw_possible -= 1
           ended += 1
           reset_value()
           jump()
           draw_c()
           nbtour += 1
        else:
            print("Réponse erronée")

def draw_c():
    global main_c_total
    while main_c_total < 17:
        show_draw_c()
        distrib_c_2()
        main_c_value[:] = []
        card_value_c()
        main_c_total = sum(main_c_value)
#--------------------------------------VALEURS DES CARTES----------------------------------------------#
def card_value_c():
    for index, item in enumerate(main_c):
        if item[0].isdigit():
                main_c_value.append(int(item[0]))
        else:
            if item[0] == "V" or item[0] == "D" or item[0] == "R":
                main_c_value.append(10)
            if item[0] == "A":
                main_c_value.append(11)

def card_value_j():
    for index, item in enumerate(main_j):
        if item[0].isdigit():
            main_j_value.append(int(item[0]))
        else:
            if item[0] == "V" or item[0] == "D" or item[0] == "R":
                main_j_value.append(10)
            if item[0] == "A":
                main_j_value.append(11)

def change_as_value_j():
    global main_j_total
    if main_j_total > 21:
       for index, item in enumerate(main_j):
           if item[0] == "A":
              item.replace("s", "", 1)
              main_j_total -= 10

def reset_value():
    main_c_value[:] = []
    main_c_total = 0
    main_j_value[:] = []
    main_j_total = 0

def reset_value2():
    global main_j_total, win_j2, win_j2_equal, mise_j, x1, x2, x3, x4, want_draw, win, ended, nbtour, replay, mise_possible, want_draw_possible
    couleur = ["pique", "trefle", "carreau", "coeur"]
    rang = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "Dix", "Valet", "Dame", "Roi"]
    deck.clear()
    deck2.clear()
    main_c.clear()
    print("valeuuuuur3", main_j_value)
    print("valeuuuuur4", main_j_total)
    main_c_value.clear()
    main_j.clear()
    main_j_value.clear()
    main_j_total -= main_j_total
    print("valeuuuuur5", main_j_value)
    print("valeuuuuur6", main_j_total)
    win_j2 -= win_j2
    win_j2_equal -= win_j2_equal
    mise_j -= mise_j
    x1 -= x1
    x2 -= x2
    x3 -= x3
    x4 -= x4
    want_draw -= want_draw
    win -= win
    ended -= ended
    nbtour -= nbtour
    deck_construction()
    replay += 1
    mise_possible -= 1
    want_draw_possible += 1
#-----------------------------------------GRAPHIQUE-------------------------------------------------#
def jump():
    print(" ")

def show_game():
    global main_c, main_j, main_c_total, main_j_total, nbtour
    jump()
    if nbtour > 1:
        print("--------------------------------")
        print("             Tour ", nbtour, "                             ")
        print("--------------------------------")
    jump()
    print("--------------------------------")
    print("      CARTES DU CROUPIER        ")
    print("--------------------------------")
    print(*main_c, sep='\n')
    jump()
    print("Valeur de la main du croupier :", main_c_total)
    jump()
    print("--------------------------------")
    print("          VOS CARTES            ")
    print("--------------------------------")
    print(*main_j, sep='\n')
    jump()
    print("Valeur de votre main :", main_j_total)
    print("--------------------------------")

def show_draw():
    print("-----------------------------------------------------------")
    print("             Le croupier vous donne une carte              ")
    print("-----------------------------------------------------------")

def show_draw_c():
    print("-----------------------------------------------------------")
    print("                 Le croupier tire une carte                ")
    print("-----------------------------------------------------------")
#-----------------------------------------GAGNER OU NON-------------------------------------------------#
def win_c():
    global win, ended
    if ended == 1:
        if main_c_total > main_j_total and main_c_total < 21:
            win += 1
            print("Vous perdez..")

def win_j():
    global win, ended, win_j2
    if ended == 1:
        if main_j_total > main_c_total:
            win += 1
            win_j2 += 1
            print("Vous gagnez !")

def blackjack():
    global win, win_j2
    if main_c_total == 21:
       win += 1
       print("BLACKJACK ! Le croupier gagne..")
    if main_j_total == 21:
       win += 1
       win_j2 += 1
       print("BLACKJACK ! Vous gagnez !")

def black_equality():
    global win, win_j2_equal
    if main_c_total == 21 and main_j_total == 21:
        win += 1
        win_j2_equal += 1
        print("DOUBLE BLACKJACK ! Egalité !")

def equality():
    global win, ended, win_j2_equal
    if ended == 1:
        if main_c_total == main_j_total:
             win += 1
             win_j2_equal += 1
             print("Egalité !")

def lose_c():
    global win, win_j2
    if main_c_total > 21:
        win += 1
        win_j2 += 1
        print("Croupier brulé ! Vous gagnez !")

def lose_j():
    global win
    if main_j_total > 21:
        win += 1
        print("Vous perdez..")

def test_score():
    test_blackjack()
    win_c()
    win_j()
    equality()
    lose_c()
    lose_j()

def test_blackjack():
    blackjack()
    black_equality()
#--------------------------------------MISES--------------------------------------------#
def mise():
    global money, mise_j, xp, mise_possible
    print("Votre solde : ", money)
    while mise_possible == 0:
        mise_j = int(input("Combien voulez-vous miser ? (NOMBRE ENTIER)"))
        if mise_j > money:
            print("Fonds insufisants")
        else:
            mise_possible += 1
            money -= mise_j
            print("Votre mise : ", mise_j)
            print("Votre solde : ", money)
            xp += mise_j
            cursor.execute("""UPDATE users SET xp = ? WHERE pseudo =?""", (xp, pseudo))
            conn.commit()

def gain():
    global money, win_j2, mise_j
    if win_j2 == 1:
        money += mise_j*2
    if win_j2_equal == 1:
        money += mise_j

#--------------------------------------DEROULEMENT DU SCRIPT--------------------------------------------#
def jouer():
    global main_c_total, main_j_total, mise
    mise()
    deck_construction()
    shuffle(deck2)
    distrib()
    print("valeuuuuur11", main_j_value)
    print("valeuuuuur12", main_j_total)
    card_value_c()
    card_value_j()
    print("--------- DEBUT DE JEU ---------")
    main_c_total = sum(main_c_value)
    main_j_total = sum(main_j_value)
    change_as_value_j()
    print("valeuuuuur13", main_j_value)
    print("valeuuuuur14", main_j_total)


    show_game()
    test_blackjack()
    gain()
#--------------------------------------TOURS--------------------------------------------#
def rolllaunch():
    global nbtour, win, main_j_total, main_c_total
    while win == 0:
                #-----------------------------DEMANDE AU JOUEUR TIRER OU NON
                draw_card()
                #-----------------------------RECOMPTAGE DES POINTS
                card_value_c()
                card_value_j()
                main_j_total = sum(main_j_value)
                change_as_value_j()
                    #-----------------------------AFFICHAGE DU JEU
                show_game()
                #-----------------------------TEST DU SCORE
                test_score()
                gain()
#----------------------------------------LANCEMENT DU JEU----------------------------------------------#
def game():
    global replay_j, nbr_jeu, replay
    print("Vous avez", xp, "d'expérience")
    while replay_j == 1:
        while replay == 1:
            if nbr_jeu == 1:
                choix = int(input("Voulez-vous jouer au black jack ? 1 = Oui, 0 = Non"))
                if choix == 1:
                    replay -= 1
                if choix == 0:
                    sys.exit("A bientot")
                if choix != 1 and choix != 0:
                    print("Réponse erronée")
            else:
                choix = int(input("Voulez-vous rejouer ? 1 = Oui, 0 = Non"))
                if choix == 1:
                    replay -= 1
                if choix == 0:
                    sys.exit("A bientot")
                else:
                    print("Réponse erronée")
        jouer()
        level_up()
        rolllaunch()
        nbr_jeu += 1
        print("Votre solde :", money)
        print("Vous avez", xp, "d'expérience")
        cursor.execute("""UPDATE users SET money = ? WHERE pseudo =?""", (money, pseudo))
        conn.commit()
        win = 0
        reset_value()
        reset_value2()




