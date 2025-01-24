import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 1400
BACKGROUND_COLOR = (255,192,203)
HANGMAN_IMAGE = "hanged_man.jpg"
MAX_INCORRECT_GUESSES = 7

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

# Load the hangman image
image = pygame.image.load(HANGMAN_IMAGE)
image = pygame.transform.scale(image, (WIDTH // 2, HEIGHT // 2))  # Scale image to half the screen

# Function to display increasing segments of the hangman image with each incorrect guess
def hangman_stage(incorrect_guesses):
    segment_height = (HEIGHT // 2) // MAX_INCORRECT_GUESSES  # Height of each segment

    if incorrect_guesses < MAX_INCORRECT_GUESSES:
        # Calculate the height to display
        height_to_display = segment_height * (incorrect_guesses)
        # Create a surface to display the segment
        segment_surface = pygame.Surface((WIDTH // 2, height_to_display))
        segment_surface.blit(image, (0, 0), (0, 0, WIDTH // 2, height_to_display))
        screen.blit(segment_surface, (WIDTH // 4, HEIGHT // 4)) # Display segments, (top corner x, y position)
    else:
        # Display the whole image
        screen.blit(image, (WIDTH // 4, HEIGHT // 4))
        # Display game over message
        font = pygame.font.Font('outlaw.ttf', 140) # Create a font object
        game_over_text = font.render("Game Over", True, (255, 0, 0)) # Render the text
        text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2)) 
        screen.blit(game_over_text, text_rect) # Display the text

def main():
    incorrect_guesses = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Test - replace later with the event of player's incorrect guess
                    if incorrect_guesses < MAX_INCORRECT_GUESSES:
                        incorrect_guesses += 1  # Increment incorrect guesses

        # Fill the background
        screen.fill(BACKGROUND_COLOR)

        # Display the appropriate segment of the image
        hangman_stage(incorrect_guesses)

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
