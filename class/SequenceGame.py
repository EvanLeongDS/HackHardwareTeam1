import pygame
import numpy as np
import sys
import time

# Initialize Pygame
pygame.init()

# Game values
level = 0
numbers_remaining = 3
numbers_remaining_partner = 4
start_time = pygame.time.get_ticks()
score=0
game_start = False
end_game = False
game_over = False
quit_timer = None

# Screen setup
CELL_SIZE = 120  # Size of each grid cell

# Font for displaying values
font = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Function to generate the grid for the current level
def generate_grid():
    global GRID, clicked_grid, GRID_ROWS, GRID_COLS
    if level<3:
        grid_size=3
    elif level<6:
        grid_size=4
    else:
        grid_size=5

    GRID = np.zeros((grid_size, grid_size), dtype=int)  # Grid of zeros initially (empty cells)
    GRID_ROWS = GRID.shape[0]
    GRID_COLS = GRID.shape[1]
    clicked_grid = np.zeros((GRID_ROWS, GRID_COLS), dtype=int)

    # Update the number of remaining items for this level
    global numbers_remaining_partner
    numbers_remaining_partner = level + 4  # The number of numbers to be placed increases with level

# Function to assign random positions to numbers on the grid
def assign_positions():
    global GRID
    GRID.fill(0)
    for i in range(1, numbers_remaining_partner):
        row, col = np.random.randint(0, GRID.shape[0]), np.random.randint(0, GRID.shape[1])
        while GRID[row, col] != 0:  # Ensure the cell is empty
            row, col = np.random.randint(0, GRID.shape[0]), np.random.randint(0, GRID.shape[1])
        GRID[row, col] = i

# Function to update screen dimensions based on grid size
def update_screen_dimensions():
    global SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE, GRID_ROWS, GRID_COLS
    GRID_ROWS = GRID.shape[0]
    GRID_COLS = GRID.shape[1]
    SCREEN_WIDTH = GRID_COLS * CELL_SIZE
    SCREEN_HEIGHT = GRID_ROWS * CELL_SIZE

# Display some text
def display_message(text, x, y, color):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Figure out which box got clicked
def getMouseCol():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    return mouse_x // CELL_SIZE

def getMouseRow():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    return mouse_y // CELL_SIZE

# Check if the box that got clicked is correct  
def checkMouseCoords(row, col):
    global numbers_remaining, game_over, score, end_game
    if GRID[row, col] == numbers_remaining_partner - numbers_remaining:  
        clicked_grid[row, col] = GRID[row, col]
        numbers_remaining=numbers_remaining-1
        draw_grid(clicked_grid)
        print("Clicked right")
        score += 1
        if numbers_remaining == 0:
            game_over = True
    else:  # Incorrect number
        end_game = True
        clicked_grid[row,col]=GRID[row, col] * -1
        draw_grid(clicked_grid)
        print("Clicked wrong! You lose!")

# Function to draw the grid
def draw_grid(arr):
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            value = arr[row, col]

            # Calculate the cell's position
            x = col * CELL_SIZE
            y = row * CELL_SIZE

            # Set the cell colors
            if clicked_grid[row,col] == 0:
                cell_color = WHITE
            elif clicked_grid[row, col] > 0:
                cell_color = GREEN
            else:
                cell_color = RED

            # Draw the cell
            pygame.draw.rect(screen, cell_color, (x, y, CELL_SIZE, CELL_SIZE), 1)

            # Render the value as text only if it's within the first 2 seconds
            #if value != 0 and pygame.time.get_ticks() - start_time < 2000:
            if(game_start):
                if(value > 0):
                    text_surface = font.render(str(value), True, GREEN)
                    text_rect = text_surface.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                    screen.blit(text_surface, text_rect)
                elif(value < 0):
                    text_surface = font.render(str(value * -1), True, RED)
                    text_rect = text_surface.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                    screen.blit(text_surface, text_rect)
                
            else:
                if(value == 0):
                    text_surface = font.render(' ', True, WHITE)  # Blank cell after 2 seconds
                    text_rect = text_surface.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                    screen.blit(text_surface, text_rect)
                else:
                    text_surface = font.render(str(value), True, WHITE)
                    text_rect = text_surface.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                    screen.blit(text_surface, text_rect)

def main():
    global level, numbers_remaining, game_over, game_start, end_game, quit_timer, start_time, screen
    # Generate grid and assign positions before updating screen dimensions
    generate_grid()  # Generate grid at the start of the game
    assign_positions()  # Assign positions of numbers on the grid
    update_screen_dimensions()  # Update the screen dimensions based on the grid size


    # Initial screen setup
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Grid Example")

    # Main game loop
    running = True
    generate_grid()  # Generate grid at the start of the game
    assign_positions()  # Assign positions of numbers on the grid
    start_time = pygame.time.get_ticks()
    while running:
        if(numbers_remaining==0):
            game_over=True
        elapsed_time = pygame.time.get_ticks() - start_time  # Calculate elapsed time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over and elapsed_time > 2000:
                checkMouseCoords(getMouseRow(), getMouseCol())
                pygame.display.flip()
        if end_game and quit_timer is None:  # Start the 5-second timer once game is over
            quit_timer = pygame.time.get_ticks()        

        # Fill the screen with black
        screen.fill(BLACK)

        # Draw the grid (this handles the blank grid after 2 seconds)
        if elapsed_time < 2000:  # 2 seconds
            game_start = False
            draw_grid(GRID)
            #GRID.fill(0)  # clears grid
        else:
            draw_grid(clicked_grid)
            game_start = True


        # If the game is over, display the result message
        if game_over:
            if numbers_remaining == 0:
                time.sleep(1)
                # Increment level and reset game state for the next level
                level += 1
                numbers_remaining = level + 3  
                generate_grid()  # Regenerate grid with updated size
                assign_positions()  # Assign numbers in new grid
                update_screen_dimensions()  # Update screen size based on new grid size

                # Update the display mode based on new screen size
                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

                game_over = False  
                start_time = pygame.time.get_ticks()  # Reset the timer for next level



        if(end_game):
            display_message("You Lose", SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) - 30, RED)
            if pygame.time.get_ticks() - quit_timer > 5000:
                running = False
        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()