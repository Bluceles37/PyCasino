can_start = 0
can_quit = 0

def event_souris(event):

#### Check for mouse pos

    if event.y>200 and event.y<480:

    #### "hover" effect, checks if the mouse is hovering the surfaces

        if event.x>300 and event.x<580:
            can_start = 1
            Fond.itemconfigure(bouton1, fill='#9999aa', outline='#9999aa')
        else:
            can_start = 0
            Fond.itemconfigure(bouton1, fill='#ddddee', outline='#ddddee')

        if event.x>620 and event.x<900:
            can_quit = 1
            Fond.itemconfigure(bouton2, fill='#aa2200', outline='#aa2200')
        else:
            can_quit = 0
            Fond.itemconfigure(bouton2, fill='#cc3311', outline='#cc3311')
    else:
        can_start = 0
        can_quit = 0
        Fond.itemconfigure(bouton1, fill='#ddddee', outline='#ddddee')
        Fond.itemconfigure(bouton2, fill='#cc3311', outline='#cc3311')

#### Button-1 clic check

    if event.num == 1:
        if can_start == 1:
            start(event)
        if can_quit == 1:
            quit()

def draw_menu():

#### Création d'un cercle en fonction (http://tkinter.fdex.eu/doc/caw.html#Canvas.create_oval)

    global bouton1
    bouton1 = Fond.create_oval(290, 190, 590, 490, fill='#ddddee', outline='#ddddee')
#### Création d'un texte avec une font spécifique
    texte1 = Fond.create_text(438, 340, text="Jouer", font='Helvetica 45', state="disabled")

    global bouton2
    bouton2 = Fond.create_oval(610, 190, 910, 490, fill='#cc3311', outline='#cc3311')
    texte2 = Fond.create_text(760, 340, text="Quitter", font='Helvetica 45', state="disabled")

#### Mouvement de la souris connecté à la fonction qui check les actions de la souris

    fenetre.bind_all("<Motion>", event_souris)

#### Clic de la souris connecté à la fonction qui check les actions de la souris (dont le clic gauche)

    fenetre.bind_all("<Button>", event_souris)
