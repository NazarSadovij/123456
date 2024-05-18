from pygame import *
from button import Button
init()

info = display.Info()
screen_width, screen_height = info.current_w, info.current_h 

window = display.set_mode((screen_width, screen_height))
background = transform.scale(image.load("background_menu.jpg"), (screen_width, screen_height))
background_pause = transform.scale(image.load("pause.jpg"), (screen_width, screen_height))
game = True
pause = False


class Hero (sprite.Sprite):
    def __init__ (self, x, y, width, height, speed, img_name = "Players_1.jpg"):
        self.image = image.load(img_name)
        self.image = transform.scale(self.image, (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        super().__init__()

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player_1(Hero):
    def move (self):
        keys = key.get_pressed()
        if keys [K_a] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys [K_d] and self.rect.x < 700:
            self.rect.x += self.speed



player_1 = Player_1 (400, 400, 100, 100, 5)


clock = time.Clock()

def stop_game():
    global game
    game = False

btn1 =  Button(window, screen_width, screen_height,stop_game)

while game:

    player_1.reset()
    player_1.move()


    if pause:
        btn1.click(e)

    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                pause = not pause
                if e.type == MOUSEBUTTONDOWN:
                    btn1.click()
    
    if pause:

        window.blit(background_pause, (0,0))
        btn1.reset()

        display.update()
        clock.tick(60)
        continue

    

    window.blit(background, (0,0))
    display.update()
    clock.tick(60)