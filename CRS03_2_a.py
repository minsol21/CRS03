import pygame
import random
import math
import imageio 
import os

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ROBOT_SIZE = 20
FRAME_RATE = 30
DURATION = 10  #duration of gif file (s)
IMAGE_DIR = "images"

# Check if the directory exists, if not create it
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)


# Initialize the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robot Arena")

# Robot class
class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = 10
    
    def move(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
    
    def draw(self, screen):
        pygame.draw.circle(screen, BLUE, (int(self.x), int(self.y)), ROBOT_SIZE)

    def check_collision(self, walls):
        for wall in walls:
            bumper_size=10
            if wall.colliderect(self.x - (ROBOT_SIZE+bumper_size), self.y - (ROBOT_SIZE+bumper_size), (ROBOT_SIZE+bumper_size) * 2, (ROBOT_SIZE+bumper_size) * 2):
                return True
        return False

    def avoid_collision(self, walls):
        if self.check_collision(walls):
            self.angle += random.uniform(1.3 * math.pi / 2, 3.3 * math.pi / 2)  # Turn a random angle between 

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

# Image saving for GIF
images = []

# Main loop
running = True
clock = pygame.time.Clock()
frame_count = 0
total_frames = FRAME_RATE * DURATION

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

    # Save frame
    if frame_count <= total_frames:
        filename = os.path.join(IMAGE_DIR, f"frame_{frame_count}.jpg")
        pygame.image.save(screen, filename)
        images.append(filename)
    else:
        running = False #Stop the game after DURATION
    
    frame_count += 1

    pygame.display.flip()
    clock.tick(FRAME_RATE)

# Convert to GIF
imageio.mimsave('robot_arena.gif', [imageio.imread(image) for image in images], fps=FRAME_RATE)

# Clean up individual frames
for image in images:
    os.remove(image)

pygame.quit()

