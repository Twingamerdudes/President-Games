import pygame
import random

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Player dimensions
PLAYER_SIZE = 20
PLAYER_SPEED = 100

# Create a class for the player
# Create a class for the player
class Player:
    def __init__(self):
        self.position = pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.velocity = pygame.Vector2(0, 0)
        self.rect = pygame.Rect(self.position.x, self.position.y, PLAYER_SIZE, PLAYER_SIZE)

    def move(self, dx, dy):
        self.velocity.x = dx
        self.velocity.y = dy

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.x, self.rect.y = self.position.x, self.position.y

    def draw(self):
        pygame.draw.rect(screen, YELLOW, self.rect)

# Create a class for the collectibles
class Collectible:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.rect)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Prison Escape Game")

# Create the player and collectibles
player = Player()
collectibles = [Collectible(random.randint(50, SCREEN_WIDTH - 50), random.randint(50, SCREEN_HEIGHT - 50)) for _ in range(10)]

# Clock to control frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    dt = clock.tick(60) / 1000.0  # Convert to seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement with delta time
    keys = pygame.key.get_pressed()
    dx = 0
    dy = 0
    if keys[pygame.K_LEFT]:
        dx = -PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        dx = PLAYER_SPEED
    if keys[pygame.K_UP]:
        dy = -PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        dy = PLAYER_SPEED
    player.move(dx, dy)

    # Update player position
    player.update(dt)

    # Check for collision with collectibles
    for collectible in collectibles[:]:
        if player.rect.colliderect(collectible.rect):
            collectibles.remove(collectible)

    # Draw everything on the screen
    screen.fill(WHITE)
    player.draw()
    for collectible in collectibles:
        collectible.draw()

    pygame.display.flip()

    # Check if all collectibles are collected
    if not collectibles:
        font = pygame.font.SysFont(None, 48)
        text = font.render("You escaped!", True, BLUE)
        screen.blit(text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(2000)  # Show the message for 2 seconds before closing the game
        running = False

pygame.quit()