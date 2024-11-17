import pygame
import numpy as np
import sys
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CELL_SIZE = 120  # Size of each grid cell
GRID_ROWS = 5
GRID_COLS = 5

# Create a numpy array and assign values
GRID = np.zeros((GRID_ROWS, GRID_COLS), dtype=int)
GRID_BLANK = np.full((GRID_ROWS, GRID_COLS), ' ', dtype=str)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game values
game_over = False
count = 0
target_row, target_col = None, None  # Start with no target initially
total_time = 15

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Grid Example")

# Font for displaying values
font = pygame.font.Font(None, 36)

# Function to display text
def display_message(text, x, y, color):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)
    
# Check grid boxes for mouse when pressed
def getMouseCol():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    grid_col = mouse_x // CELL_SIZE
    return grid_col

def getMouseRow():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    grid_row = mouse_y // CELL_SIZE    
    return grid_row

# Function to check if the clicked square is correct  
def checkMouseCoords(row, col):
    global count , game_over
    if (row, col) == (target_row, target_col):  # Correct square clicked
        count += 1
        print("Count: ", count)
        select_new_target()  # Select a new random target
    else:  # Incorrect square clicked
        print("Clicked wrong")
        game_over = True


# Function to draw the grid
def draw_grid(arr):
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            # Get the value from the NumPy array
            value = arr[row, col]

            # Calculate the cell's position
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            
            # Set the cell color
            if (row, col) == (target_row, target_col):  # Highlight target
                cell_color = GREEN
            elif value == 0:  # Empty cells
                cell_color = WHITE
            else:
                cell_color = GRAY

            # Draw the cell
            pygame.draw.rect(screen, cell_color, (x, y, CELL_SIZE, CELL_SIZE), 1)  # Cell border
        
            # Render the value as text
            text_surface = font.render(str(value), True, WHITE)
            text_rect = text_surface.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
            screen.blit(text_surface, text_rect)

# Function to highlight the target square
def highlight_target(row, col):
    x = col * CELL_SIZE
    y = row * CELL_SIZE
    pygame.draw.rect(screen, GREEN, (x, y, CELL_SIZE, CELL_SIZE))  # Highlight target

# Function to select a new random target
def select_new_target():
    global target_row, target_col
    target_row, target_col = np.random.randint(0, GRID_ROWS), np.random.randint(0, GRID_COLS)

# Main game loop
def aim_trainer():
    global game_over, count, target_row, target_col
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    elapsed_time = pygame.time.get_ticks() - start_time
    time_left = 15000
    running = True

    # Select the initial random target
    select_new_target()

    while running:
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Convert to seconds
        time_left = max(0, total_time - elapsed_time)        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                clicked_row = mouse_y // CELL_SIZE
                clicked_col = mouse_x // CELL_SIZE
                checkMouseCoords(clicked_row, clicked_col)

        

        # Draw everything
        screen.fill(BLACK)  # Fill the screen with black
        draw_grid(GRID_BLANK)  # Draw the grid
        highlight_target(target_row, target_col)  # Highlight the current target square
        display_message(f"Time Left: {int(time_left)}s", SCREEN_WIDTH // 2, 24, WHITE)


        pygame.display.flip()


        # If game over, stop the loop
        if game_over or time_left <= 0:
            if time_left <= 0:
                display_message("Time's Up! Your score was "+str(count), SCREEN_WIDTH //2, SCREEN_HEIGHT //2, RED)
                break
            else: 
                display_message("You Missed! Your score was "+str(count), SCREEN_WIDTH//2, SCREEN_HEIGHT//2, RED)
                break
        clock.tick(60) #limit to 60fps
    pygame.display.flip()
    time.sleep(5)
    
# Run the game
def main():
    aim_trainer()

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()