from pygame import *

class GameSpirte(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w = 100, h = 100):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSpirte):
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

font.init()
CoLoR_1 = (200, 255, 255)
win_width = 1000; win_height = 600
window = display.set_mode((win_width, win_height))
window.fill(CoLoR_1)
font2 = font.Font(None, 80)
lose1 = font2.render("Перший гравець ПРОГРАВ!", True, (255, 255, 255))
lose2 = font2.render("Другий гравець ПРОГРАВ!", True, (255, 255, 255))

player_1 = Player("photo_2024.jpg", 5, win_height - 380, 10, 30, 180)
player_2 = Player("photo_2024.jpg", 965, win_height - 380, 10, 30, 180)
ball = GameSpirte("images__мяч-removebg-preview.png", 460, 250, 8, 100, 80)

clock = time.Clock()
FPS = 60 
game = True
speed_x = 3
speed_y = 3
finish = False


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if not finish:
        window.fill(CoLoR_1)
        player_1.reset()
        player_1.update_1()

        player_2.reset()
        player_2.update_2()

        ball.reset()
        ball.update()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(player_1, ball) or sprite.collide_rect(player_2, ball):
            speed_x *= -1

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (150, 200) )

        if ball.rect.x > 1000:
            finish = True
            window.blit(lose2, (150, 200) )

    display.update()
    clock.tick(FPS)



