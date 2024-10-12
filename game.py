import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Ігра на пайтон :)")

player_image = pygame.image.load("homak.png")
bg = pygame.image.load("bambuk.jpg")

x = 50
y = 50
speed = 5

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("idle.png")
        self.rect = self.image.get_rect()

        self.change_x = 0
        self.change_y = 0

        self.level = None

    def update(self):
        self.calc_gravity()
        self.rect.x += self.change_x

class Level(object):
    def __init__(self):
        self.platforms = pygame.sprite.Group()
        self.player = Player()  # Створюємо об'єкт Player
        self.background = None

    def update(self):
        win.blit(bg, (0, 0))
        self.platforms.draw(win)  # Замінили 'self.platform' на 'self.platforms'

clock = pygame.time.Clock()
run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()  # Виправлено на 'keys'

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    win.blit(bg, (0, 0))
    win.blit(player_image, (x, y))  # Виправлено на (x, y)
    pygame.display.update()
    clock.tick(50)

pygame.quit()
