import pygame
import sys

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Controller Mapper - Press Buttons/Move Axes")

# Set up a small window to ensure the event queue works
screen = pygame.display.set_mode((300, 300))

# Initialize the joystick module
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()

if joystick_count == 0:
    print("No joystick detected. Please connect your controller and restart the script.")
    sys.exit()
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

# Main event loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle Joystick Button events
        elif event.type == pygame.JOYBUTTONDOWN:
            print(f"Button {event.button} DOWN (Pressed)")
        elif event.type == pygame.JOYBUTTONUP:
            # You can also detect button release if needed
            print(f"Button {event.button} UP (Released)")

        # Handle Joystick Axis motion events (analog sticks or triggers)
        elif event.type == pygame.JOYAXISMOTION:
            # The value is usually between -1.0 and 1.0
            if abs(event.value) > 0.1: # Add a small threshold to avoid jitter
                print(f"Axis {event.axis} motion: {event.value:.2f}")

        # Handle Hat Switch events (D-pad)
        elif event.type == pygame.JOYHATMOTION:
            # The value is a tuple (x, y). e.g., (0, 1) is Up, (-1, 0) is Left
            print(f"Hat {event.hat} motion: {event.value}")

        # Handle Keyboard/Numpad input events
        elif event.type == pygame.KEYDOWN:
            print(f"Keyboard Key pressed: {pygame.key.name(event.key)}")

    # Call pygame.event.pump() regularly if not using pygame.event.get() in the loop
    # pygame.event.pump() 

# Quit pygame
pygame.quit()
sys.exit()
