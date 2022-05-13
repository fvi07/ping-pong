from pygame import *
font.init()

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


window = display.set_mode((1000,700))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('bg.jpg'),(1000,700))
player1 = Player('rocket-left.png',5,250,20,150,5)
player2 = Player('rocket-right.png',975,250,20,150,5)
ball = GameSprite('ball.png',475,325,100,100,10)

game = True
finish = False
clock = time.Clock()
FPS = 60
speed_x = 10
speed_y = 10
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

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y < 0 or ball.rect.y > 600:
            speed_y *= -1

        if sprite.collide_rect(ball,player1) or sprite.collide_rect(ball,player2):
            speed_x *= -1
        
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(375,325))
        if ball.rect.x > 900:
            finish = True
            window.blit(lose2,(375,325))
        

    clock.tick(FPS)
    display.update()

