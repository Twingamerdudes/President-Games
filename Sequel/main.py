import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cutscene System")

# Define colors
WHITE = (255, 255, 255)

# Define cutscene data
cutscene_frames = [
    ("In a time, where 5 PM is nap time.", 3000),
    ("Biden-Man is fast asleep!", 2000),
    ("And so Trump-Man must be the one to be indicted", 3000),
    ("Can he escape his fate?", 2500)
]

# Main function to play cutscene
def play_cutscene():
    frame_index = 0
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()

    while frame_index < len(cutscene_frames):
        elapsed_time = pygame.time.get_ticks() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        

        if elapsed_time >= cutscene_frames[frame_index][1]:
            frame_index += 1
            start_time = pygame.time.get_ticks()

        screen.fill(WHITE)

        if frame_index >= len(cutscene_frames):
            break
        # Render the current frame text
        font = pygame.font.Font(None, 36)
        text_surface = font.render(cutscene_frames[frame_index][0], True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    play_cutscene()
    import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Player dimensions
PLAYER_SIZE = 30

# Enemy dimensions
ENEMY_SIZE = 25

# Collectible dimensions
COLLECTIBLE_SIZE = 15

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collectible Game")

# Function to generate random positions on the screen
def random_position():
    return random.randint(0, WIDTH), random.randint(0, HEIGHT)

# Function to check for collisions between two rectangles
def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

# Main game loop
def game_loop():
    player_x, player_y = WIDTH // 2, HEIGHT // 2
    player_speed = 5

    enemy_x, enemy_y = random_position()
    enemy_speed = 2

    collectibles = [pygame.Rect(random_position(), (COLLECTIBLE_SIZE, COLLECTIBLE_SIZE)) for _ in range(20)]

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < HEIGHT - PLAYER_SIZE:
            player_y += player_speed

        # Make the enemy follow the player
        if enemy_x < player_x:
            enemy_x += enemy_speed
        elif enemy_x > player_x:
            enemy_x -= enemy_speed

        if enemy_y < player_y:
            enemy_y += enemy_speed
        elif enemy_y > player_y:
            enemy_y -= enemy_speed

        # Check for collisions between the player and collectibles
        for collectible in collectibles[:]:
            if check_collision(pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE), collectible):
                collectibles.remove(collectible)

        # Check for collisions between the player and the enemy
        if check_collision(pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE),
                           pygame.Rect(enemy_x, enemy_y, ENEMY_SIZE, ENEMY_SIZE)):
            print("Game Over!")
            pygame.quit()
            quit()

        # Clear the screen
        screen.fill(WHITE)

        # Draw the player
        pygame.draw.rect(screen, GREEN, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))

        # Draw the enemy
        pygame.draw.rect(screen, BLACK, (enemy_x, enemy_y, ENEMY_SIZE, ENEMY_SIZE))

        # Draw the collectibles
        for collectible in collectibles:
            pygame.draw.rect(screen, GREEN, collectible)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    game_loop()
