from pygame import *
font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,player_w,player_h, player_speed,speed_x,speed_y):
        super().__init__()
        self.w = player_w
        self.h = player_h
        self.image = transform.scale(image.load(player_image),(player_w,player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed_x = speed_x
        self.speed_y = speed_y
        
    
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 545:
            self.rect.y += self.speed
    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 545:
            self.rect.y += self.speed 

class Ball(GameSprite):
    def update(self):
    
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y < 0 or self.rect.y > 600:
            self.speed_y *= -1

        if sprite.collide_rect(self,player1) or sprite.collide_rect(self,player2):
            self.speed_x *= -1

        if self.rect.x < 0:
            finish = True
            window.blit(lose1,(375,325))
        if self.rect.x > 900:
            finish = True
            window.blit(lose2,(375,325))
        


window = display.set_mode((1000,700))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('background.jpg'),(1000,700))
player1 = Player('rocket-left.png',5,250,20,150,5,0,0)
player2 = Player('rocket-right.png',975,250,20,150,5,0,0)
ball = Ball('ball.png',475,325,100,100,6,6,6)

game = True
finish = False
clock = time.Clock()
FPS = 60
speed_x = 6
speed_y = 6
font1 = font.SysFont('Arial', 35)
lose1 = font1.render('PLAYER 1 LOSE',True, (255,0,0))
lose2 = font1.render('PLAYER 2 LOSE',True, (255,0,0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 
    if finish != True:
        
        window.blit(background,(0,0))
        player1.reset()
        player2.reset()
        player1.update_left()
        player2.update_right()
        ball.reset()
        ball.update()
        
       
        

    clock.tick(FPS)
    display.update()
