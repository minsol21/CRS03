import random
import math
import time
import pygame

# Constants
ROBOT_SIZE = 20

class Robot:
    def __init__(self, x, y, env):
        self.x = x
        self.y = y
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = 2
        self.env = env
        self.mode = 'random'
        self.last_positions = []
        self.max_stuck_count = 10  # Max times the robot can be in the same position before considering it stuck
        self.ts = time.time()
    
    def move(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        self.record_position()

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (int(self.x), int(self.y)), ROBOT_SIZE)

    def record_position(self):
        self.last_positions.append((int(self.x), int(self.y)))
        if len(self.last_positions) > self.max_stuck_count:
            self.last_positions.pop(0)

    def is_stuck(self):
        if len(self.last_positions) < self.max_stuck_count:
            return False
        return len(set(self.last_positions[-self.max_stuck_count:])) == 1

    def avoid_collision(self):
        if self.env.sense_wall(self) or self.is_stuck():
            self.angle += random.uniform(math.pi / 2, 3 * math.pi / 2)  # Turn a random angle between 90 and 270 degrees
            self.record_position()  # Update position after turning
    
    def wall_follow(self):
        if self.env.sense_wall(self):
            self.turn_left()
        elif not self.env.sense_left(self):
            self.turn_left()
            self.move()
        else:
            self.move()
    
    def turn_left(self):
        self.angle -= math.pi / 2
    
    def turn_right(self):
        self.angle += math.pi / 2

    def random_walk(self):
        current = time.time()
        elapsed = current - self.ts
        if elapsed <= 5:
            self.move()
        elif elapsed <= 6:
            if random.choice(['left', 'right']) == 'left':
                self.turn_left()
            else:
                self.turn_right()
            self.move()
        else:
            self.ts = time.time()

    def update(self):
        if self.mode == 'random':
            self.avoid_collision()
            self.random_walk()
            if self.env.sense_wall(self):
                self.mode = 'wall_following'
        elif self.mode == 'wall_following':
            self.wall_follow()
            if not self.env.sense_wall(self):
                self.mode = 'random'
        self.move()
