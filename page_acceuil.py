def message_acceuil():
    font=pygame.font.Font(None, 40) # defini la typographie et la taile du texte
    text_welcome = "Bienvenu \ndans le jeu du pendu \n(espace pour continuer)"
    y = 200 # coordonnée dans l'écran dans le sens de la hauteur
    x = fenetreWidth / 2 # coordonnée dans l'ecran dans le sens de la largeur
    fenetre.fill(background)
    for ligne in text_welcome.splitlines(): # boucle pour lire ligne par ligne
        textSurface = font.render(ligne, 1, BLEU) # rendu d'une ligne
        textRect = textSurface.get_rect() # ligne transformé en surface grace à .get_rect()
        textRect.center = (x, y) # centrage du point d'ancrage
        fenetre.blit(textSurface, textRect) # imprime une ligne
        y = y + 100 # déplace la prochaine ligne  de 100 pixel vers le bas

def menu():
    font=pygame.font.Font(None, 40)
    titre = "PENDU !"
    text_menu = "Pour ajouter un mot à la liste : touche 1\nPour jouer : touche 2"
    x = fenetreWidth / 2
    fenetre.fill(background)
    titreSurface = font.render(titre, 1, BLEU)
    titreRect = titreSurface.get_rect()
    titreRect.center = (x, 20)  
    fenetre.blit(titreSurface, titreRect)
    y = 200
    for ligne in text_menu.splitlines():
        textSurface = font.render(ligne, 1, BLEU)
        textRect = textSurface.get_rect()
        textRect.center = (x, y)
        fenetre.blit(textSurface, textRect)
        y = y + 100

def add_word():
    name = ""
    font = pygame.font.Font(None, 50)
    running = True
    while running:
        texte = "Vous pourvez saisir le mot à ajouter : "
        x = 360 / 2
        texteSurface = font.render(texte, True, (255, 255, 255))
        texteRect = texteSurface.get_rect()
        texteRect.center = (x, 40)
        for evt in pygame.event.get():
            if evt.type == pygame.KEYDOWN:
                if evt.unicode.isalpha():
                    name += evt.unicode
                elif evt.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif evt.key == pygame.K_RETURN:
                    name = f"\n{name.lower()}"
                    with open("mots.txt", "a") as f:
                        f.write(name)
                    name = "Le mot est ajouté à la liste !"
                    # espace pour retrouner au menu!!!!!
                    running = False
            elif evt.type == pygame.QUIT:
                running = False
        fenetre.fill((0, 0, 0))
        block = font.render(name, True, (255, 255, 255))
        rect = block.get_rect()
        rect.center = fenetre.get_rect().center
        fenetre.blit(texteSurface, texteRect)
        fenetre.blit(block, rect)
        pygame.display.flip()







import pygame
from pygame.locals import *
 
pygame.init()

fenetreWidth = 900
fenetreHeight = 700
 
fenetre = pygame.display.set_mode((fenetreWidth, fenetreHeight))
tittle = pygame.display.set_caption("PENDU !")

# varibles de couleur
ROSE = (250,37,203)
BLEU = (50,100,255)

# background
background = pygame.Surface(fenetre.get_size())
background.convert()
background = ROSE

# variables pour blit
afficher_acceuil = message_acceuil()
afficher_menu = 0
afficher_add_word = 0


continuer = 1
while continuer:
 
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0


    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE] == True:
        afficher_acceuil = 0
        afficher_menu = menu()

    if key[pygame.K_a] == True:
        afficher_menu = 0
        afficher_add_word = add_word()
    elif key[pygame.K_b] == True:
        afficher_menu = 0
        afficher_add_word = 0




    pygame.display.flip()

 
pygame.quit()
