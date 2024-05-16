import pygame
import random
import numpy as np
from robots import Robot  # Import the Robot class
import math

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CELL_SIZE = 20
FPS = 60
ROBOT_SIZE = 20

# Initialize pygame
pygame.init()

# Initialize the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vacuum Cleaning Robot")

# Environment class
class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((height // CELL_SIZE, width // CELL_SIZE), dtype=int)
        self._place_walls()

    def _place_walls(self):
        self.grid[0, :] = 1
        self.grid[-1, :] = 1
        self.grid[:, 0] = 1
        self.grid[:, -1] = 1

    def draw(self, screen):
        for y in range(self.grid.shape[0]):
            for x in range(self.grid.shape[1]):
                if self.grid[y, x] == 1:
                    pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def sense_wall(self, robot):
        front_x = int((robot.x + ROBOT_SIZE * math.cos(robot.angle)) // CELL_SIZE)
        front_y = int((robot.y + ROBOT_SIZE * math.sin(robot.angle)) // CELL_SIZE)
        return self.grid[front_y, front_x] == 1
    
    def sense_left(self, robot):
        left_x = int((robot.x + ROBOT_SIZE * math.cos(robot.angle - math.pi / 2)) // CELL_SIZE)
        left_y = int((robot.y + ROBOT_SIZE * math.sin(robot.angle - math.pi / 2)) // CELL_SIZE)
        return self.grid[left_y, left_x] == 1

# Create walls
env = Environment(WIDTH, HEIGHT)

# Initialize robot at a random position
robot = Robot(random.randint(ROBOT_SIZE, WIDTH - ROBOT_SIZE), random.randint(ROBOT_SIZE, HEIGHT - ROBOT_SIZE), env)

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Draw environment
    env.draw(screen)

    # Update and draw robot
    robot.update()
    robot.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
