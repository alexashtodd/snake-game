from pynput import keyboard
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

    if(eatfood == True): #if eats food, increse snake length
        return(snakePartxy) #increse snake length and returns to replace main snakePartXY
    else:
        snakePartxy.pop() #remove last segment of snake to avoid incresing length
        return(snakePartxy) #returns new list to replace main snakePartXY
    
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
    running = True

def nes
    if event.type == pygame.KEYDOWN:
            print(f"Keyboard Key pressed: {pygame.key.name(event.key)}")
            # You can map keyboard keys to NES actions here, e.g.:
            if event.key == pygame.K_z:
                print("NES Button B (via keyboard)")
            elif event.key == pygame.K_x:
                print("NES Button A (via keyboard)")


        # --- Handle Joystick Button events (e.g., A, B, Start, Select) ---
        elif event.type == pygame.JOYBUTTONDOWN:
            # Button 0 is often 'B', Button 1 is often 'A' on USB SNES pads
            if event.button == 0:
                print("NES Button B (via controller)")
            elif event.button == 1:
                print("NES Button A (via controller)")
            elif event.button == 8:
                print("NES SELECT (via controller)") # Check docs for your specific pad
            elif event.button == 9:
                print("NES START (via controller)") # Check docs for your specific pad

        
        # --- Handle Hat Switch events (D-pad UP/DOWN/LEFT/RIGHT) ---
        elif event.type == pygame.JOYHATMOTION:
            # The value is a tuple (x, y)
            if event.value == (0, 1):
                print("NES D-pad UP")
            elif event.value == (0, -1):
                print("NES D-pad DOWN")
            elif event.value == (-1, 0):
                print("NES D-pad LEFT")
            elif event.value == (1, 0):
                print("NES D-pad RIGHT")


#head and segments
snakePartXY = [(0,0)] 

#diretion x and y
dx = 0 
dy = 0

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# Initial game state
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
running = True

# # Initialize the joystick module
 pygame.joystick.init()
 joystick_count = pygame.joystick.get_count()

 if joystick_count == 0:
     print("No joystick detected. Using keyboard only.  Please connect your controller and restart the script.")
     # sys.exit()
 else:
     # Get the first joystick (index 0)
     joystick = pygame.joystick.Joystick(0)
     joystick.init()
     print(f"Detected Joystick: {joystick.get_name()}")
     print(f"Number of buttons: {joystick.get_numbuttons()}")
     print(f"Number of axes: {joystick.get_numaxes()}")
     print(f"Number of hat switches (D-pads): {joystick.get_numhats()}")
     print("-" * 30)
     print("Press buttons or move sticks to see their mappings...")

# Game loop
while running:

    # Process events
    events = pygame.event.get()
    for event in events: 
    # for event in pygame.event.get():

        # Check for quit event
        if event.type == pygame.QUIT:
            running = False
            continue

        # Key pressed event 
        if event.type == pygame.KEYDOWN:
            # print("Key down:", event.key)
            if event.key in (pygame.K_UP, pygame.K_w):
                next_direction = UP
                continue
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                next_direction = DOWN
                continue
            elif event.key in (pygame.K_LEFT, pygame.K_a):
                next_direction = LEFT
                continue
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                next_direction = RIGHT
                continue
            elif event.key == pygame.K_p:
                paused = not paused
                continue
            elif event.key == pygame.K_r:
                initializeGameState()
                game_over = False 
                paused = False 
                continue
            # print("Next Direction:", next_direction)

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
        
    for x_pos in range(GRID_WIDTH):
        for y_pos in range(GRID_HEIGHT):
            if (x_pos, y_pos) in snake:
                draw_rect(screen, (x_pos, y_pos), GREEN)
            elif (x_pos, y_pos) == food:
                draw_rect(screen, (x_pos, y_pos), RED)
            else:
                draw_rect(screen, (x_pos, y_pos), GRAY) 

    screen.blit(screen, (0, 0))
    pygame.display.flip()

    clock.tick(fps)
# Quit pygame
pygame.quit()
sys.exit()
