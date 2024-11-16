import numpy as np
import time
from IPython.display import clear_output

def show_and_hide(message, duration):
    # show the numpy array for the set duration and then hide it
    # currently not working
    print(message)
    time.sleep(duration)
    clear_output(wait=True)

def game():
    # All game mechanics stored here
    while True:
    # Create a numpy array
        array_2d = np.zeros((5, 5))
        # Make one of the zeros a random number
        row, col = np.random.randint(0, array_2d.shape[0]), np.random.randint(0, array_2d.shape[1])
        # Set the random number from 1-100
        random_number = np.random.randint(0, 100)
        array_2d[row, col] = random_number

        show_and_hide(array_2d, 2) # show the array for 2 seconds

        number_guess = int(input('Guess the number: '))  # User input
        row_guess = int(input('Guess the row: '))  # User input
        while row_guess > 5 or row_guess < 1:
            print("please guess a number between 1 and 5")
            column_guess = int(input('Guess the column: '))  # User input
        while column_guess > 5 or row_guess < 1:
            print("please guess a number between 1 and 5")
            column_guess = int(input('Guess the column: '))

            # Use conditionals to figure out if the user is right
        if number_guess == random_number and row_guess == row + 1 and column_guess == col + 1:
            print("Good job!!")
            break
        elif number_guess != random_number or row_guess != row + 1 or column_guess != col + 1:
            print("Oh no you got it wrong, try again")
game()