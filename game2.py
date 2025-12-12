import pygame
import sys
import time
import random


# Configurable settings
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
WINDOW_WIDTH = CELL_SIZE * GRID_WIDTH
WINDOW_HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS_START = 10
FPS_INCREMENT = 1

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (200, 30, 30)
GREEN = (30, 200, 30)
GRAY  = (40, 40, 40)

# Directions
UP    = (0, -1)
DOWN  = (0, 1)
LEFT  = (-1, 0)
RIGHT = (1, 0)
STILL = (0,0)


def random_food_position(snake):
    """Return a random empty cell not occupied by snake."""
    while True:
        pos = (random.randrange(GRID_WIDTH), random.randrange(GRID_HEIGHT))
        if pos not in snake:
            return pos

def draw_rect(surface, pos, color):
    x, y = pos
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(surface, color, rect)


def initializeGameState():
    global snake
    global direction
    global next_direction
    global food
    global growing
    global score
    global fps
    global game_over
    global paused
    global running

    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2),
             (GRID_WIDTH // 2 - 1, GRID_HEIGHT // 2),
             (GRID_WIDTH // 2 - 2, GRID_HEIGHT // 2)]
    direction = RIGHT
    next_direction = RIGHT 
    food = random_food_position(snake)
    growing = False
    score = 0
    fps = FPS_START
    game_over = False
    paused = False
    # Note: 'running' global variable should ideally be handled outside initialize, 
    # but kept here to match user's global usage pattern

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# Initial game state (global variables)
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2),
         (GRID_WIDTH // 2 - 1, GRID_HEIGHT // 2),
         (GRID_WIDTH // 2 - 2, GRID_HEIGHT // 2)]
direction = RIGHT
next_direction = RIGHT
food = random_food_position(snake)
growing = False
score = 0
fps = FPS_START
game_over = False
paused = False
running = True # This needs to be True to start the while loop

# Initialize the joystick module
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()

if joystick_count == 0:
     print("No joystick detected. Using keyboard only.  Please connect your controller and restart the script.")
else:
     joystick = pygame.joystick.Joystick(0)
     joystick.init()
     print(f"Detected Joystick: {joystick.get_name()}")
     # ... (rest of joystick debug prints) ...


# Game loop
while running:

    # Process events
    # FIX 1: Consolidated event loops.
    for event in pygame.event.get(): 

        # Check for quit event
        if event.type == pygame.QUIT:
            running = False
            continue

        # Key pressed event (This handles the game movement)
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w) and direction != DOWN:
                next_direction = UP
            elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != UP:
                next_direction = DOWN
            elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != RIGHT:
                next_direction = LEFT
            elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != LEFT:
                next_direction = RIGHT
            elif event.key == pygame.K_p:
                paused = not paused
            elif event.key == pygame.K_r:
                initializeGameState()
                game_over = False 
                paused = False 
            elif event.key in (pygame.K_1, pygame.K_KP1):
                print("Key 1 pressed (example action)") # Replace with desired functionality
            elif event.key in (pygame.K_2, pygame.K_KP2):
                print("Key 2 pressed (example action)")
            elif event.key in (pygame.K_3, pygame.K_KP3):
                print("Key 3 pressed (example action)")
            elif event.key in (pygame.K_4, pygame.K_KP4):
                print("Key 4 pressed (example action)")
            elif event.key in (pygame.K_5, pygame.K_KP5):
                print("Key 5 pressed (example action)")
            elif event.key in (pygame.K_6, pygame.K_KP6):
                print("Key 6 pressed (example action)")
            elif event.key in (pygame.K_7, pygame.K_KP7):
                print("Key 7 pressed (example action)")
            elif event.key in (pygame.K_8, pygame.K_KP8):
                print("Key 8 pressed (example action)")
            elif event.key in (pygame.K_9, pygame.K_KP9):
                print("Key 9 pressed (example action)")

        
        # --- CONTROLLER INPUT HANDLING ---
        if joystick:
            # Handle controller buttons (START/SELECT work here)
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 8: # SELECT button for restart
                    initializeGameState()
                    game_over = False
                    paused = False
                elif event.button == 9: # START button for pause
                    paused = not paused 
      
            elif event.type == pygame.JOYHATMOTION:
                if event.value == (0, 1) and direction != DOWN:
                    next_direction = UP
                elif event.value == (0, -1) and direction != UP:
                    next_direction = DOWN
                elif event.value == (-1, 0) and direction != RIGHT:
                    next_direction = LEFT
                elif event.value == (1, 0) and direction != LEFT:
                    next_direction = RIGHT
            
             elif event.type == pygame.JOYAXISMOTION:
                axis_0_value = joystick.get_axis(0) # X-axis
                axis_1_value = joystick.get_axis(1) # Y-axis
                
                # Check for significant movement (tolerance for analog noise)
                if abs(axis_0_value) > 0.5:
                    if axis_0_value < 0 and direction != RIGHT:
                        next_direction = LEFT
                    elif axis_0_value > 0 and direction != LEFT:
                        next_direction = RIGHT
                
                if abs(axis_1_value) > 0.5:
                    if axis_1_value < 0 and direction != DOWN:
                        next_direction = UP
                    elif axis_1_value > 0 and direction != UP:
                        next_direction = DOWN
    # Handle Game Over 
    if game_over:
        screen.fill(BLACK)
        game_over_surf = font.render("Game Over - press R to restart", True, WHITE)
        screen.blit(game_over_surf, (10, 10))
        pygame.display.flip()
        clock.tick(FPS_START)
        continue

    # Handle Pause
    if paused:
        screen.fill(BLACK)
        pause_surf = font.render("PAUSED - press P to resume", True, WHITE)
        screen.blit(pause_surf, (10, 10))
        pygame.display.flip()
        clock.tick(FPS_START)
        continue

    # Movement & turning logic
    # FIX 2: Check for opposite direction *before* setting the direction
    opposite = (-direction[0], -direction[1])
    if next_direction != opposite:
         direction = next_direction

    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = (head_x + dx, head_y + dy)

    # Wall collision
    if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
        new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
        game_over = True
    # Self collision
    elif new_head in snake:
        game_over = True

    # Moving snake and growing
    snake.insert(0, new_head)  # move head

    if new_head == food:
        score += 1
        growing = True
        food = random_food_position(snake)
        fps += FPS_INCREMENT
    if not growing:
        snake.pop()  # remove tail
    else:
        growing = False

    # FIX 3: Clear screen *once* before drawing everything in its new position
    screen.fill(BLACK)
        
    for x_pos in range(GRID_WIDTH):
        for y_pos in range(GRID_HEIGHT):
            pos = (x_pos, y_pos)
            if pos in snake:
                draw_rect(screen, pos, GREEN)
            elif pos == food:
                draw_rect(screen, pos, RED)
            else:
                # FIX 4: Only draw gray background if you want a checkerboard/grid background.
                # If you want a plain black background, comment out this else block.
                draw_rect(screen, pos, GRAY) 

    # FIX 5: Remove redundant/incorrect screen blit
    # screen.blit(screen, (0, 0)) 
    
    pygame.display.flip()
    clock.tick(fps)
    
# Quit pygame
pygame.quit()
sys.exit()




