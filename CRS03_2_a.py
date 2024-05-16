import pygame
import random
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ROBOT_SIZE = 20

# Initialize the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robot Arena")

# Robot class
class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = 2
    
    def move(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
    
    def draw(self, screen):
        pygame.draw.circle(screen, BLUE, (int(self.x), int(self.y)), ROBOT_SIZE)

    def check_collision(self, walls):
        for wall in walls:
            if wall.colliderect(self.x - ROBOT_SIZE, self.y - ROBOT_SIZE, ROBOT_SIZE * 2, ROBOT_SIZE * 2):
                return True
        return False

    def avoid_collision(self, walls):
        if self.check_collision(walls):
            self.angle += random.uniform(math.pi / 2, 3 * math.pi / 2)  # Turn a random angle between 90 and 270 degrees

# Create walls and obstacles
walls = [
    pygame.Rect(0, 0, WIDTH, 10),  # Top wall
    pygame.Rect(0, 0, 10, HEIGHT),  # Left wall
    pygame.Rect(0, HEIGHT - 10, WIDTH, 10),  # Bottom wall
    pygame.Rect(WIDTH - 10, 0, 10, HEIGHT)  # Right wall
]

# Create obstacles
obstacles = [
    pygame.Rect(200, 150, 50, 50),
    pygame.Rect(400, 300, 100, 100),
    pygame.Rect(600, 450, 30, 30)
]

# Initialize robot at a random position
robot = Robot(random.randint(ROBOT_SIZE, WIDTH - ROBOT_SIZE), random.randint(ROBOT_SIZE, HEIGHT - ROBOT_SIZE))

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Draw walls and obstacles
    for wall in walls:
        pygame.draw.rect(screen, BLACK, wall)
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)
    
    # Move and draw robot
    robot.avoid_collision(walls + obstacles)
    robot.move()
    robot.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
