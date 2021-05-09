from pygame import *
import play

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.size_x = size_x
        self.size_y = size_y
        self.image = transform.scale(image.load(player_image), (self.size_x, self.size_y))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

speed_x = 3
speed_y = 3
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Пинг-понг")
background = (255, 255, 255)
window.fill(background)
hero1 = Player('Hero.png', 600, 100, 20, 150, 5)
hero2 = Player('Hero.png', 20, 100, 20, 150, 5)
ball = GameSprite('asteroid.png', 350, 250, 50, 50, 5)

game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        if ball.rect.y >= 400:
            ball.rect.y -= speed_y
        elif ball.rect.y <= 5:
            ball.rect.y += speed_y
        elif sprite.collide_rect(hero2, ball):
            ball.rect.x += speed_x
        elif sprite.collide_rect(hero1, ball):
            ball.rect.x -= speed_x
        window.fill(background)
        hero1.update1()
        hero2.update2()
        hero1.reset()
        hero2.reset()
        ball.reset()

    clock.tick(FPS)
    display.update()