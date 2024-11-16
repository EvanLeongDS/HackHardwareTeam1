import pygame
import numpy as np
import sys

# Initialize Pygame
pygame.init()


# Create a numpy array and assign values
GRID = np.zeros((5, 5), dtype = int)
# Generate random positions for numbers 1 to 5
for i in range(1, 6):
    # Generate random row and column for each number
    row, col = np.random.randint(0, GRID.shape[0]), np.random.randint(0, GRID.shape[1])
    # Ensure the position is not already taken
    while GRID[row, col] != 0:
        row, col = np.random.randint(0, GRID.shape[0]), np.random.randint(0, GRID.shape[1])
    # Assign the number to the random spot
    GRID[row, col] = i


# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CELL_SIZE = 120  # Size of each grid cell
GRID_ROWS = 5
GRID_COLS = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Game values
numbers_remaining = 5
start_time = pygame.time.get_ticks()

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Grid Example")

# Font for displaying values
font = pygame.font.Font(None, 36)

# Function to display text
def display_message(text, x, y):
    #pygame.draw.rect(screen, (255,0,0), (360, 120, CELL_SIZE, CELL_SIZE), 1)  # Cell border
    print("Displaying...")
    text_surface = font.render(text, True, (255,0,0))  
    text_rect = text_surface.get_rect(center=(x, y))  
    screen.blit(text_surface, text_rect) 
    #pygame.display.flip()
    
# Check grid boxes for mouse when pressed
def getMouseCol():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    grid_col = mouse_x  // CELL_SIZE
    return grid_col
def getMouseRow():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    grid_row = mouse_y // CELL_SIZE    
    return grid_row

# Check if the box clicked is correct  
def checkMouseCoords(row, col):
    print("Checking...")
    global numbers_remaining
    if GRID[row, col] == 6-numbers_remaining:
        numbers_remaining=numbers_remaining-1
        display_message("You win", 300, 300)
        print("clicked right")
        return True
    else:
        display_message("You lose", 300, 300)
        print("clicked wrong")
        return False

# Function to draw the grid
def draw_grid():
    print('DRAWING>>>>>')
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
    elapsed_time = pygame.time.get_ticks() - start_time  # Calculate elapsed time
    if elapsed_time > 2000:  # 2 seconds
        GRID.fill(0)  # clears grid
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            checkMouseCoords(getMouseRow(), getMouseCol())
            while(True):
                pygame.display.flip()
                
            

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the grid
    draw_grid()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()