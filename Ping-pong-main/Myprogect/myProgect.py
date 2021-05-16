from pygame import *
import play

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed_x, speed_y):
        super().__init__()
        self.size_x = size_x
        self.size_y = size_y
        self.image = transform.scale(image.load(player_image), (self.size_x, self.size_y))    
        self.speed_x = speed_x
        self.speed_y = speed_y 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed_y
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed_y
    def update2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed_y
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed_y

speed_x = 3
speed_y = 3
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Пинг-понг")
background = (255, 255, 255)
window.fill(background)
hero1 = Player('Hero.png', 600, 100, 20, 150, 0, 9)
hero2 = Player('Hero.png', 20, 100, 20, 150, 0, 9)
ball = GameSprite('asteroid.png', 350, 250, 50, 50, 9, 9)
font.init()
game = True
finish = False
clock = time.Clock()
FPS = 60
font.init()
text_lose = font
font.init()
font = font.Font(None, 50)
win = font.render("2 PLAYER WIN!", True, (255, 215, 0))
lose = font.render("1 PLAYER WIN!", True, (255, 215, 0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:

        ball.rect.y -= ball.speed_y
        ball.rect.x += ball.speed_x
        if sprite.collide_rect(hero2, ball) or sprite.collide_rect(hero1, ball):
            ball.speed_x *= -1
        
        if ball.rect.y <= 5:
            ball.speed_y *= -1

        if ball.rect.y >= 450:
            ball.speed_y *= -1
        
        window.fill(background)
        hero1.update1()
        hero2.update2()
        hero1.reset()
        hero2.reset()
        ball.reset()

    if ball.rect.x <= 5:
        finish = True
        window.blit(win, (300, 250))
    
    if ball.rect.x >= 700:
        finish = True
        window.blit(lose, (300, 250))

    clock.tick(FPS)
    display.update()