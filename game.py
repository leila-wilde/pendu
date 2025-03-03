import pygame
import sys
import math
from random import choice

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 2000, 1200
BACKGROUND_COLOR = ('Pink')
LETTERS_COLOUR = (0,0,0)
LETTERS_SIZE = 120
FONT = "capth.ttf"
MESSAGE_SIZE = 120  # Font size for the message
RADIUS_TOP = 1400  # Radius for the top arc
RADIUS_BOTTOM = 1500  # Radius for the bottom arc
CENTER_TOP = (WIDTH // 2, 2000)  # Center for the top arc
CENTER_BOTTOM = (WIDTH // 2, 2300)  # Center for the bottom arc
HANGMAN_IMAGE = "hanged_man.jpg"
MAX_INCORRECT_GUESSES = 7

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Load fonts
letters_font = pygame.font.Font(FONT, LETTERS_SIZE)
message_font = pygame.font.Font(FONT, MESSAGE_SIZE)  # Load message font

# Create lists of letters
letters_top = [chr(i) for i in range(65, 78)]  # A-M
letters_bottom = [chr(i) for i in range(78, 91)]  # N-Z
all_letters = letters_top + letters_bottom  # Combine both lists to simplify

# Calculate positions for letters in a curved arc
def get_curved_letter_positions(letters, center, radius):
    positions = []
    angle_step = 70 / len(letters)  # Angle step between letters / steepness of arc
    for i, letter in enumerate(letters):
        angle = math.radians(122.5 - (i * angle_step))  # Adjust angle calculation for upward arch
        x = center[0] + radius * math.cos(angle)  # X position
        y = center[1] - radius * math.sin(angle)  # Y position
        positions.append((letter, (x, y)))
    return positions

# Get positions for both arcs with different radii
letter_positions_top = get_curved_letter_positions(letters_top, CENTER_TOP, RADIUS_TOP)
letter_positions_bottom = get_curved_letter_positions(letters_bottom, CENTER_BOTTOM, RADIUS_BOTTOM)

# Message to display
message = ""

# Load the hangman image
image = pygame.image.load(HANGMAN_IMAGE)
image = pygame.transform.scale(image, (400, 700))  # Scale image


# fonction to generate a random secret word to play from txt file
def random_word(): 
    with open("mots.txt", "r") as f:
        list_words = f.readlines()
    secret_word = choice(list_words)
    secret_word.replace("\n", "")

    return secret_word

# fonction to buidl a liste with "_" for each guessing letters
def first_display():
    word_in_progress = []
    secret_word = random_word()
    for i, char in enumerate(secret_word):
        word_in_progress.append("_")
    return secret_word, word_in_progress



# Function to display increasing segments of the hangman image with each incorrect guess
def hangman_stage(incorrect_guesses):
    segment_height = 700 // MAX_INCORRECT_GUESSES  # Height of each segment

    if incorrect_guesses < MAX_INCORRECT_GUESSES:
        # Calculate the height to display
        height_to_display = segment_height * (incorrect_guesses)
        # Create a surface to display the segment
        segment_surface = pygame.Surface((400, height_to_display))
        segment_surface.blit(image, (0, 0), (0, 0, 400, height_to_display))
        screen.blit(segment_surface, (1600, 0))
    else:
        # Display the whole image
        screen.blit(image, (1600, 0))
        # Display game over message
        font = pygame.font.Font('outlaw.ttf', 100) # Create a font object
        game_over_text = font.render("Game Over", True, (255, 0, 0)) # Render the text
        text_rect = game_over_text.get_rect(center=(1800, 350)) # Position text
        screen.blit(game_over_text, text_rect) # Display the text

# Main loop
incorrect_guesses = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 1:  # Left mouse button
        #         mouse_pos = event.pos
        #         for letter, pos in letter_positions_top + letter_positions_bottom:
        #             text_surface = letters_font.render(letter, True, LETTERS_COLOUR)
        #             rect = text_surface.get_rect(center=pos)
        #             if rect.collidepoint(mouse_pos):
        #                 message = play_pendu()
        elif event.type == pygame.KEYDOWN:  # Check for key presses
            if event.unicode.upper() in all_letters:  # Check if the pressed key is a letter
                letter = event.unicode.upper()
                incorrect_guesses, word_in_progress = play_pendu()

            # if event.key == pygame.K_SPACE:  # Simulate the player's incorrect guesses
            #     if incorrect_guesses < MAX_INCORRECT_GUESSES:
            #         incorrect_guesses += 1  # Increment incorrect guesses
                

    # Fill the background
    screen.fill(BACKGROUND_COLOR)
    
    # Draw letters for both arcs
    for letter, pos in letter_positions_top + letter_positions_bottom:
        text_surface = letters_font.render(letter, True, LETTERS_COLOUR)
        rect = text_surface.get_rect(center=pos)
        screen.blit(text_surface, rect.topleft)
        
    # Draw the top message
    if message:
        message_surface = message_font.render(message, True, LETTERS_COLOUR)
        message_rect = message_surface.get_rect(center=(WIDTH // 2, 100))  # Position message at the top
        screen.blit(message_surface, message_rect)
    
    # Display the appropriate segment of the image
    hangman_stage(incorrect_guesses)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()