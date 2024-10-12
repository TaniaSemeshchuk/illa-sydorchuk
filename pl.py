import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Налаштування вікна
win_width, win_height = 800, 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Платформер")

# Кольори
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Налаштування персонажа
player_size = 50
player_x = 50
player_y = win_height - player_size
player_speed = 5
velocity_y = 0
gravity = 0.5
jump_height = 10
is_jumping = False

# Платформи
platforms = []
platform_height = 20
for i in range(5):
    platform_x = random.randint(0, win_width - 100)
    platform_y = random.randint(100, win_height - 100)
    platforms.append(pygame.Rect(platform_x, platform_y, 100, platform_height))

# Монети
coins = []
for i in range(10):
    coin_x = random.randint(0, win_width - 20)
    coin_y = random.randint(100, win_height - 200)
    coins.append(pygame.Rect(coin_x, coin_y, 20, 20))

# Гра
clock = pygame.time.Clock()
run = True
score = 0

while run:
    clock.tick(60)
    win.fill(WHITE)

    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Клавіші для переміщення
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < win_width - player_size:
        player_x += player_speed
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
            velocity_y = -jump_height
    else:
        velocity_y += gravity  # Додаємо гравітацію
        player_y += velocity_y

    # Перевірка зіткнення з платформами
    on_platform = False
    for platform in platforms:
        if player_x + player_size > platform.x and player_x < platform.x + platform.width:
            if player_y + player_size >= platform.y and player_y + player_size <= platform.y + velocity_y + 1:
                player_y = platform.y - player_size
                is_jumping = False
                velocity_y = 0
                on_platform = True

    # Якщо не на платформі, то додаємо гравітацію
    if not on_platform:
        player_y += velocity_y
        if player_y >= win_height - player_size:
            player_y = win_height - player_size
            is_jumping = False
            velocity_y = 0

    # Малювання персонажа
    pygame.draw.rect(win, GREEN, (player_x, player_y, player_size, player_size))

    # Малювання платформ
    for platform in platforms:
        pygame.draw.rect(win, (0, 0, 0), platform)

    # Малювання монет
    for coin in coins[:]:
        pygame.draw.rect(win, YELLOW, coin)
        if pygame.Rect(player_x, player_y, player_size, player_size).colliderect(coin):
            coins.remove(coin)
            score += 1

    # Виведення рахунку
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    win.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
