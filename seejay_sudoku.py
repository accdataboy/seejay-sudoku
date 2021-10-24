"""
 The latest (October 2021) Sudoku attempt from C.J. Pitchford.

 Sample Python/Pygame/Py-sudoku
 Red Rocks Community College Computer Science / Computer Technology
 With gratitude to http://programarcadegames.com/
"""

import pygame
from sudoku import Sudoku

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

# Set the height and width of the screen
size = [700, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("SeeJay Sudoku")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

display_instructions = True
instruction_page = 1

# Use this boolean variable to trigger if the game is over.
game_over = False

# This is a font we use to draw text on the screen (size 36)
font = pygame.font.SysFont('Verdana', 24, True, False)
display = pygame.font.SysFont('Courier', 20, True, False)

# -------- Instruction Page Loop -----------
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            instruction_page += 1
            if instruction_page == 3:
                display_instructions = False

    # Set the screen background
    screen.fill(WHITE)

    if instruction_page == 1:
        # Draw instructions, page 1
        # This could also load an image created in another program.
        # That could be both easier and more flexible.

        text = font.render("Welcome to SeeJay Sudoku!", True, BLACK)
        screen.blit(text, [100, 200])

        text = font.render("Click to get ready...", True, BLACK)
        screen.blit(text, [100, 240])

    if instruction_page == 2:
        # Draw instructions, page 2
        text = font.render("Sudoku instructions!?!? Really!?!?", True, BLACK)
        screen.blit(text, [100, 200])

        text = font.render("Click to go!", True, BLACK)
        screen.blit(text, [100, 240])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# ---------- Main Program Loop --------------
# -------- ...including Game Over -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Create exit condition
            game_over = True

    # Set the screen background
    screen.fill(BLACK)

    # Use exit condition result
    if game_over:
        # If game over is true, draw game over
        text = display.render("Game Over", True, WHITE)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])

    else:
        # Create puzzle
        puzzle = Sudoku(3).difficulty(0.5)
        # realization = puzzle.__format_board_ascii()
        # print(puzzle.__str__())

        mod_y = 20
        row_y = 140
        # Display puzzle
        for row in puzzle.__str__().splitlines():
            row_y += mod_y
            result = display.render(row, True, WHITE)
            screen.blit(result, [100, row_y])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()
