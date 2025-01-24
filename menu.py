import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 2000, 1000
BACKGROUND_IMAGE_PATH = "menu_background.jpg"
BUTTON_COLOR = (0, 108, 0)  # Green
BUTTON_HOVER_COLOR = (0, 200, 0)  # Lighter green
TEXT_COLOR = (255, 255, 255)  # White
FONT_SIZE = 100

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pendu de l'au-de là")

# Load the background image
background_image = pygame.image.load(BACKGROUND_IMAGE_PATH)
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Load font
font = pygame.font.Font('optinational_gothic.otf', FONT_SIZE)

# Function to draw the buttons
def draw_button(text, x, y, width, height, hover=False):
    color = BUTTON_HOVER_COLOR if hover else BUTTON_COLOR
    pygame.draw.rect(screen, color, (x, y, width, height), 10)
    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(x + width * 0.5, y + height * 0.5))
    screen.blit(text_surface, text_rect)

def menu_page():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    mouse_pos = event.pos
                    # Check if the mouse is over the buttons
                    if button1_rect.collidepoint(mouse_pos):
                        print("En entrant dans le jeu...")  
                        # Add code here ***
                    elif button2_rect.collidepoint(mouse_pos):
                        print("Ajoute un mot...") 
                        # Add code here ***
                    elif button3_rect.collidepoint(mouse_pos):
                        print("Affichage des scores...")  
                        # Add code here ***

        # Fill the background
        screen.blit(background_image, (0, 0))

        # Draw welcome message
        welcome_text = font.render("Menu du pendu de l'au-de là... ", True, TEXT_COLOR)
        welcome_rect = welcome_text.get_rect(center=(WIDTH * 0.5, HEIGHT * 0.5 - 350))
        screen.blit(welcome_text, welcome_rect)

        # Draw the buttons
        button_width, button_height = 800, 120
        button_x = (WIDTH - button_width) * 0.5
        button_y = HEIGHT * 0.5
        
        # Define button rectangles
        button1_rect = pygame.Rect(button_x, button_y - 150, button_width, button_height)
        button2_rect = pygame.Rect(button_x, button_y + 50, button_width, button_height)
        button3_rect = pygame.Rect(button_x, button_y + 250, button_width, button_height)

        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()
        
        # Draw buttons with hover effect
        draw_button("JOUER", button_x, button_y - 150, button_width, button_height, 
                    hover=button1_rect.collidepoint(mouse_pos))
        draw_button("AJOUTE  UN  MOT", button_x, button_y + 50, button_width, button_height, 
                    hover=button2_rect.collidepoint(mouse_pos))
        draw_button("SCORES", button_x, button_y + 250, button_width, button_height, 
                    hover=button3_rect.collidepoint(mouse_pos))

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    menu_page()