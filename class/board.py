import pygame
import numpy as np
import sys

# Initialize Pygame
pygame.init()
# Create a numpy array
GRID = np.zeros((5, 5))
# Make one of the zeros a random number
row, col = np.random.randint(0, GRID.shape[0]), np.random.randint(0, GRID.shape[1])
# Set the random number from 1-100
random_number = np.random.randint(0, 100)
GRID[row, col] = random_number

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CELL_SIZE = 120  # Size of each grid cell
GRID_ROWS = 5
GRID_COLS = 5

#Define the values of the grid


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Grid Example")

# Font for displaying values
font = pygame.font.Font(None, 36)

# Function to draw the grid
def draw_grid():
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            # Get the value from the NumPy array
            value = GRID[row, col]

            # Calculate the cell's position
            x = col * CELL_SIZE
            y = row * CELL_SIZE

            # Draw the cell
            pygame.draw.rect(screen, GRAY, (x, y, CELL_SIZE, CELL_SIZE), 1)  # Cell border

            # Render the value as text
            text_surface = font.render(str(value), True, WHITE)
            text_rect = text_surface.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
            screen.blit(text_surface, text_rect)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the grid
    draw_grid()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
