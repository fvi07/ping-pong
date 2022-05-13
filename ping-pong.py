from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,player_w,player_h, player_speed):
        super().__init__()
        self.w = player_w
        self.h = player_h
        self.image = transform.scale(image.load(player_image),(player_w,player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y < 505:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y > 5:
            self.rect.y += self.speed
    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y < 505:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y > 5:
            self.rect.y += self.speed 


window = display.set_mode((1000,700))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('фон.jpg'),(1000,700))
player1 = Player('rocket-left.png',5,250,20,150,5)
player2 = Player('rocket-right.png',975,250,20,150,5)


game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background,(0,0))
    player1.reset()
    player2.reset()
    player1.update_left()
    player2.update_right()

    clock.tick(FPS)
    display.update()

