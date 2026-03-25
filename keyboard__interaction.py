import pygame
import sys

try:
    radius = int(input("Enter the radius of the circle (e.g., 20-50): "))
except ValueError:
    print("Invalid input. Defaulting to radius 30.")
    radius = 30

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Animated Circle")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

x, y = WIDTH // 2, HEIGHT // 2
velocity = 5
color = BLUE

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)  # Clear screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                color = RED if color == BLUE else BLUE

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - radius > 0:
        x -= velocity
    if keys[pygame.K_RIGHT] and x + radius < WIDTH:
        x += velocity
    if keys[pygame.K_UP] and y - radius > 0:
        y -= velocity
    if keys[pygame.K_DOWN] and y + radius < HEIGHT:
        y += velocity

    pygame.draw.circle(screen, color, (x, y), radius)

    pygame.display.flip()  # Update display
    clock.tick(60)  # Maintain 60 Frames Per Second

pygame.quit()
sys.exit()