import pygame
import numpy as np
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CELL_SIZE = 120  # Size of each grid cell
GRID_SIZE = 5
GRID_ROWS = 5
GRID_COLS = 5

# Create a numpy array and assign values
GRID = np.zeros((GRID_ROWS, GRID_COLS), dtype = int)
GRID_GAME = np.zeros((GRID_ROWS, GRID_COLS), dtype = int)
GRID_BLANK = np.full((GRID_ROWS, GRID_COLS), ' ', dtype = str)
clicked_grid = np.zeros((GRID_ROWS, GRID_COLS), dtype=int)

game_start = False
game_over = False

# Generate random positions for numbers 1 to 5
for i in range(1, 6):
    # Generate random row and column for each number
    row, col = np.random.randint(0, GRID.shape[0]), np.random.randint(0, GRID.shape[1])
    # Ensure the position is not already taken
    while GRID[row, col] != 0:
        row, col = np.random.randint(0, GRID.shape[0]), np.random.randint(0, GRID.shape[1])
    # Assign the number to the random spot
    GRID[row, col] = i




# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game values
numbers_remaining = 5
start_time = pygame.time.get_ticks()

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
    grid_col = mouse_x  // CELL_SIZE
    return grid_col
def getMouseRow():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    grid_row = mouse_y // CELL_SIZE    
    return grid_row

# Check if the box clicked is correct  
def checkMouseCoords(row, col):
    print("Checking...")
    global numbers_remaining, game_over
    if GRID[row, col] == 6-numbers_remaining:
        clicked_grid[row, col] = 6 - numbers_remaining
        numbers_remaining=numbers_remaining-1
        draw_grid(clicked_grid)
        print("clicked right")
        return True
    else:
        print("clicked wrong")
        clicked_grid[row,col]=GRID[row, col] * -1
        game_over = True
        draw_grid(clicked_grid)
        return False

# Function to draw the grid
def draw_grid(arr):
    #print('DRAWING>>>>>')
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            # Get the value from the NumPy array
            value = arr[row, col]

            # Calculate the cell's position
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            
            #set the cell colors
            if clicked_grid[row,col] == 0:
                cell_color = WHITE
            elif clicked_grid[row, col] > 0:
                cell_color = GREEN
            else:
                cell_color = RED

            # Draw the cell
            pygame.draw.rect(screen, cell_color, (x, y, CELL_SIZE, CELL_SIZE), 1)  # Cell border
        
            # Render the value as text
            
            if(arr.dtype == np.int64 and game_start == True):
                if(value == 0):
                    text_surface = font.render(' ', True, WHITE)
                    text_rect = text_surface.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                    screen.blit(text_surface, text_rect)
                elif(value > 0):
                    text_surface = font.render(str(value), True, GREEN)
                    text_rect = text_surface.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                    screen.blit(text_surface, text_rect)
                elif(value < 0):
                    text_surface = font.render(str(value * -1), True, RED)
                    text_rect = text_surface.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                    screen.blit(text_surface, text_rect)
            else:
                text_surface = font.render(str(value), True, WHITE)
                text_rect = text_surface.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                screen.blit(text_surface, text_rect)
# Main game loop
running = True
quit_timer = None

"""
while running:
    if(numbers_remaining==0):
        game_over=True
    elapsed_time = pygame.time.get_ticks() - start_time  # Calculate elapsed time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if elapsed_time > 2000 and game_start:
                checkMouseCoords(getMouseRow(), getMouseCol())
                pygame.display.flip()
                
    if game_over and quit_timer is None:  # Start the 5-second timer once game is over
        quit_timer = pygame.time.get_ticks()            

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the grid
    if elapsed_time < 2000:  # 2 seconds
        draw_grid(GRID)
        #GRID.fill(0)  # clears grid
    else:
        draw_grid(clicked_grid)
        game_start = True

    if game_over:
        if(numbers_remaining==0):
            display_message("You Win", SCREEN_WIDTH //2, SCREEN_HEIGHT//2, GREEN)
        else:
            display_message("You Lose", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, RED)
        if pygame.time.get_ticks() - quit_timer > 5000:
            running = False

            


    # Update the display
    pygame.display.flip()
"""


def highlight_target(row, col):
    x = col * CELL_SIZE
    y = row * CELL_SIZE
    pygame.draw.rect(screen, GREEN, (x, y, CELL_SIZE, CELL_SIZE))  # Highlight target

def checkAimMouseCoords(row, col):
    global count, game_over, target_row, target_col
    if (row, col) == (target_row, target_col):
        count += 1
        print("Clicked right")
    else:
        game_over = True
        print("Clicked wrong")

def aim_trainer():
    elapsed_time2 = pygame.time.get_ticks() # Calculate elapsed time
    global game_over, count, target_row, target_col

    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    running = True

    while running:
        elapsed_time2 = pygame.time.get_ticks() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                clicked_row = mouse_y // CELL_SIZE
                clicked_col = mouse_x // CELL_SIZE
                checkAimMouseCoords(clicked_row, clicked_col)

        if game_over or elapsed_time2 > 30000:  # End condition
            running = False
            break

        # Select a random target
        target_row, target_col = np.random.randint(0, GRID_SIZE), np.random.randint(0, GRID_SIZE)

        # Draw everything
        draw_grid(GRID_BLANK)
        highlight_target(target_row, target_col)
        pygame.display.flip()

        # Select a new random target square if not already chosen
        if target_row is None and target_col is None:
            target_row, target_col = np.random.randint(0, GRID_ROWS), np.random.randint(0, GRID_COLS)
        clock.tick(1)  # Highlight target for 1 second

    if count >= 10 and elapsed_time2 < 30000:
        print("You win!")
    else:
        print("Game over!")

# Run the game
count = 0
running = True
aim_trainer()




# Quit Pygame
pygame.quit()
sys.exit()