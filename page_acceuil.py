import pygame
from pygame.locals import *


def welcome_page():
    font=pygame.font.Font('carnevalee_freakshow.ttf', 40) # defini la typographie et la taile du texte
    text_welcome = "Bienvenu \ndans le jeu du pendu \n(espace pour continuer)"
    y = 200 # coordonnée dans l'écran dans le sens de la hauteur
    x = screenWidth / 2 # coordonnée dans l'ecran dans le sens de la largeur
    screen.fill(background)
    for ligne in text_welcome.splitlines(): # boucle pour lire ligne par ligne
        textSurface = font.render(ligne, 1, WHITE) # rendu d'une ligne
        textRect = textSurface.get_rect() # ligne transformé en surface grace à .get_rect()
        textRect.center = (x, y) # centrage du point d'ancrage
        screen.blit(textSurface, textRect) # imprime une ligne
        y = y + 100 # déplace la prochaine ligne  de 100 pixel vers le bas

def menu_page():
    font=pygame.font.Font('carnevalee_freakshow.ttf', 40)
    tittle = "PENDU !"
    text_menu = "Pour ajouter un mot à la liste : touche a\nPour jouer : touche b"
    x = screenWidth / 2
    screen.fill(background)
    tittleSurface = font.render(tittle, 1, WHITE)
    tittleRect = tittleSurface.get_rect()
    tittleRect.center = (x, 20)  
    screen.blit(tittleSurface, tittleRect)
    y = 200
    for ligne in text_menu.splitlines():
        textSurface = font.render(ligne, 1, WHITE)
        textRect = textSurface.get_rect()
        textRect.center = (x, y)
        screen.blit(textSurface, textRect)
        y = y + 100


def add_word_page():
    font = pygame.font.Font('carnevalee_freakshow.ttf', 50)
    color = pygame.Color(255,192,203)

    input_box = pygame.Rect(100, 150, 800, 100)
    word = ""
    
    run = True
    while run:

        text = "Vous pourvez saisir le mot à ajouter : "
        x = 360 / 2
        textSurface = font.render(text, True, (WHITE))
        textRect = textSurface.get_rect()
        textRect.center = (x, 40)


        for evt in pygame.event.get():
            if evt.type == pygame.KEYDOWN:
                if evt.unicode.isalpha():
                    word += evt.unicode
                elif evt.key == pygame.K_BACKSPACE:
                    word = word[:-1]
                elif evt.key == pygame.K_RETURN:
                    word = f"\n{word.lower()}"
                    with open("mots.txt", "a") as f:
                        f.write(word)
                    word = "Le mot est ajouté à la liste !"
                    # espace pour retrouner au menu!!!!!
                    run = False
            elif evt.type == pygame.QUIT:
                run = False


        screen.fill((BLACK))
        wordSurface = font.render(word, True, (WHITE))
        screen.blit(wordSurface, (input_box.x+25, input_box.y+10))
        screen.blit(textSurface, textRect)
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()

def play_game():




    







pygame.init()

screenWidth = 900
screenHeight = 700
 
screen = pygame.display.set_mode((screenWidth, screenHeight))
tittle = pygame.display.set_caption("PENDU !")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ROSE = (250,37,203)
BLEU = (50,100,255)


background = pygame.Surface(screen.get_size())
background.convert()
background = BLACK


welcome_page()

play = True
while play:
 
    for event in pygame.event.get():
        if event.type == QUIT:
            play = False


key = pygame.key.get_pressed()

if key[pygame.K_SPACE] == True:
    menu_page()

if key[pygame.K_a] == True:
    add_word_page()

if key[pygame.K_b] == True:
    # play_pendu()


pygame.display.flip()

 
pygame.quit()
