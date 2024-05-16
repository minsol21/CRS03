import numpy as np
import random
import pygame

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int)
        self._place_walls()
    
    def _place_walls(self):
        self.grid[0, :] = 1
        self.grid[-1, :] = 1
        self.grid[:, 0] = 1
        self.grid[:, -1] = 1

class Robot:
    def __init__(self, env):
        self.env = env
        self.position = self._get_random_position()
        self.direction = random.choice(['up', 'down', 'left', 'right'])
        self.last_positions = []
        self.max_stuck_count = 4  # Max times the robot can be in the same position before considering it stuck
    
    def _get_random_position(self):
        while True:
            x = random.randint(1, self.env.width - 2)
            y = random.randint(1, self.env.height - 2)
            if self.env.grid[y, x] == 0:
                return (y, x)
    
    def _move_forward(self):
        y, x = self.position
        if self.direction == 'up':
            self.position = (y - 1, x)
        elif self.direction == 'down':
            self.position = (y + 1, x)
        elif self.direction == 'left':
            self.position = (y, x - 1)
        elif self.direction == 'right':
            self.position = (y, x + 1)
    
    def _move_backward(self):
        y, x = self.position
        if self.direction == 'up':
            self.position = (y + 1, x)
        elif self.direction == 'down':
            self.position = (y - 1, x)
        elif self.direction == 'left':
            self.position = (y, x + 1)
        elif self.direction == 'right':
            self.position = (y, x - 1)
    
    def _turn_left(self):
        if self.direction == 'up':
            self.direction = 'left'
        elif self.direction == 'down':
            self.direction = 'right'
        elif self.direction == 'left':
            self.direction = 'down'
        elif self.direction == 'right':
            self.direction = 'up'
    
    def _turn_right(self):
        if self.direction == 'up':
            self.direction = 'right'
        elif self.direction == 'down':
            self.direction = 'left'
        elif self.direction == 'left':
            self.direction = 'up'
        elif self.direction == 'right':
            self.direction = 'down'
    
    def _sense_wall(self):
        y, x = self.position
        if self.direction == 'up' and self.env.grid[y - 1, x] == 1:
            return True
        if self.direction == 'down' and self.env.grid[y + 1, x] == 1:
            return True
        if self.direction == 'left' and self.env.grid[y, x - 1] == 1:
            return True
        if self.direction == 'right' and self.env.grid[y, x + 1] == 1:
            return True
        return False
    
    def _sense_left(self):
        y, x = self.position
        if self.direction == 'up' and self.env.grid[y, x - 1] == 1:
            return True
        if self.direction == 'down' and self.env.grid[y, x + 1] == 1:
            return True
        if self.direction == 'left' and self.env.grid[y + 1, x] == 1:
            return True
        if self.direction == 'right' and self.env.grid[y - 1, x] == 1:
            return True
        return False
    
    def _sense_right(self):
        y, x = self.position
        if self.direction == 'up' and self.env.grid[y, x + 1] == 1:
            return True
        if self.direction == 'down' and self.env.grid[y, x - 1] == 1:
            return True
        if self.direction == 'left' and self.env.grid[y - 1, x] == 1:
            return True
        if self.direction == 'right' and self.env.grid[y + 1, x] == 1:
            return True
        return False
    
    def is_stuck(self):
        if len(self.last_positions) < self.max_stuck_count:
            return False
        return len(set(self.last_positions[-self.max_stuck_count:])) == 1
    
    def wall_follow(self):
        if self.is_stuck():
            self._move_backward()
            self._turn_right()
            self._move_forward()
        elif self._sense_wall():
            self._turn_left()
        elif not self._sense_left():
            self._turn_left()
            self._move_forward()
        else:
            self._move_forward()
        
        self.last_positions.append(self.position)
        if len(self.last_positions) > self.max_stuck_count:
            self.last_positions.pop(0)

# Initialize pygame
pygame.init()

# Constants
CELL_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def draw_environment(screen, env, robot):
    screen.fill(WHITE)
    for y in range(env.height):
        for x in range(env.width):
            if env.grid[y, x] == 1:
                pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    ry, rx = robot.position
    pygame.draw.rect(screen, RED, (rx * CELL_SIZE, ry * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()

# Initialize environment and robot
env = Environment(width=20, height=15)
robot = Robot(env)

# Set up display
screen = pygame.display.set_mode((env.width * CELL_SIZE, env.height * CELL_SIZE))
pygame.display.set_caption("Wall Following Robot")

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    robot.wall_follow()
    draw_environment(screen, env, robot)
    
    clock.tick(FPS)

pygame.quit()
