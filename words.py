import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 2000, 1000
BACKGROUND_IMAGE = "menu_background.jpg" 
BUTTON_COLOR = (0, 108, 0)  # Green
BUTTON_HOVER_COLOR = (0, 200, 0)  # Lighter green
TEXT_COLOR = (255, 255, 255)  # White
FONT_SIZE = 100
INPUT_BOX_COLOR = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pendu de l'au-de là")

# Load the background image
background_image = pygame.image.load(BACKGROUND_IMAGE)
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  

# Load font
font = pygame.font.Font('optinational_gothic.otf', FONT_SIZE)

def draw_button(text, x, y, width, height, hover=False):
    color = BUTTON_HOVER_COLOR if hover else BUTTON_COLOR
    pygame.draw.rect(screen, color, (x, y, width, height), 10)
    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(x + width * 0.5, y + height * 0.5))
    screen.blit(text_surface, text_rect)

def save_word(word):
    word_list_file = 'word_list.txt'
    with open(word_list_file, 'a') as f:
        f.write(f"{word.lower()}\n")

def add_words_page():
    running = True
    text = ''
    input_box = pygame.Rect(WIDTH * 0.5 - 500, HEIGHT * 0.5 - 100, 1000, 200)
    
    # Draw the return to menu button
    button_width, button_height = 800, 120
    button_x = (WIDTH - button_width) * 0.5
    button_y = HEIGHT - 150
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = event.pos
                    # Check if the mouse is over the button
                    if button_rect.collidepoint(mouse_pos):
                        print("Retour au menu...")
                        # Add code here ***
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    save_word(text)
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        # Fill the background
        screen.blit(background_image, (0, 0))
        
        # Draw welcome message
        welcome_text = font.render("Ajouter un mot...", True, TEXT_COLOR)
        welcome_rect = welcome_text.get_rect(center=(WIDTH * 0.5, 150))
        screen.blit(welcome_text, welcome_rect)

        # Render the current text
        text_surface = font.render(text, True, INPUT_BOX_COLOR)
        screen.blit(text_surface, (input_box.x + 20, input_box.y + 20))
        pygame.draw.rect(screen, INPUT_BOX_COLOR, input_box, 2)

        # Check if the mouse is hovering over the button
        mouse_pos = pygame.mouse.get_pos()
        draw_button("RETOUR AU MENU", button_x, button_y, button_width, button_height, hover=button_rect.collidepoint(mouse_pos))

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    add_words_page()
