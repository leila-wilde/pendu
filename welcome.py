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

def draw_button(text, x, y, width, height, hover=False):
    color = BUTTON_HOVER_COLOR if hover else BUTTON_COLOR
    pygame.draw.rect(screen, color, (x, y, width, height), 10)
    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(x + width * 0.5, y + height * 0.5))
    screen.blit(text_surface, text_rect)

def welcome_page():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = event.pos
                    # Check if the mouse is over the button
                    if button_rect.collidepoint(mouse_pos):
                        print("En entrant dans le jeu...")
                        # Add code here ***

        # Fill the background
        screen.blit(background_image, (0, 0))

        # Draw welcome message
        welcome_text = font.render("Bienvenue dans le jeu de pendu de l'au-de là . . . ", True, TEXT_COLOR)
        welcome_rect = welcome_text.get_rect(center=(WIDTH // 2, 300))
        screen.blit(welcome_text, welcome_rect)

        # Draw the Enter button
        button_width, button_height = 500, 120
        button_x = (WIDTH - button_width) // 2
        button_y = HEIGHT - 400
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

        # Check if the mouse is hovering over the button
        mouse_pos = pygame.mouse.get_pos()
        draw_button("MENU", button_x, button_y, button_width, button_height, hover=button_rect.collidepoint(mouse_pos))

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    welcome_page()
