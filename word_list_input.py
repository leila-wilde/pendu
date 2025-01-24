import pygame
import sys

# Initialize Pygame
pygame.init()

# constants
width, height = 1000, 400
color = pygame.Color(255,192,203)

# Set up display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Word List Input")

# Set up fonts
font = pygame.font.Font('carnevalee_freakshow.ttf', 75)

# Input box
input_box = pygame.Rect(100, 150, 800, 100)
text = ''

# Word list file
word_list_file = 'word_list.txt'

def save_word(word):
    with open(word_list_file, 'a') as f:
        f.write(word + '\n')

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                save_word(text)
                text = ''
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode

    # Fill the background
    screen.fill((30, 30, 30))

    # Render the current text
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (input_box.x+25, input_box.y+10))
    pygame.draw.rect(screen, color, input_box, 2)

    # Update the display
    pygame.display.flip()
