import pygame
import sys
import SequenceGame
import AimTrainerGame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Selector")

# Font for displaying options
font = pygame.font.Font(None, 48)

# Function to display text
def display_message(text, x, y, color):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Main title screen loop
def title_screen():
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BLACK)

        # Display title and options
        display_message("Choose a Game:", SCREEN_WIDTH // 2, 100, WHITE)
        display_message("1. Sequence Game", SCREEN_WIDTH // 2, 200, GREEN)
        display_message("2. Aim Trainer", SCREEN_WIDTH // 2, 300, GREEN)
        display_message("Press 1 or 2 to select", SCREEN_WIDTH // 2, 400, WHITE)
        display_message("Press Q to Quit", SCREEN_WIDTH // 2, 500, RED)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    SequenceGame.main()
                elif event.key == pygame.K_2:
                    AimTrainerGame.main()
                elif event.key == pygame.K_q:
                    running = False
        clock.tick(60)



# Run the title screen
title_screen()
