from pygame import *
from button import Button


map = """ 
0 0 0 0 0 0 0 0 0 4
1 1 0 1 0 0 0 0 0 4
2 2 0 2 0 0 0 0 0 4
3 3 0 3 3 3 3 3 0 4
1 2 0 3 0 0 0 0 0 4
1 2 0 3 0 0 0 0 0 4
1 2 0 3 1 1 1 1 1 4
 """


init()

info = display.Info()
screen_width, screen_height = info.current_w, info.current_h 

window = display.set_mode((screen_width, screen_height))
background = transform.scale(image.load("level1.jpg"), (screen_width, screen_height))
background_pause = transform.scale(image.load("background_menu.jpg"), (screen_width, screen_height))
game = True
pause = True


class Hero (sprite.Sprite):
    def __init__ (self, x, y, width, height, speed, img_name = "Players_1.jpg"):
        self.image = image.load(img_name)
        self.image = transform.scale(self.image, (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.jump=False
        self.jumpCount = 10

        super().__init__()

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player_1(Hero):
    def move (self):
        keys = key.get_pressed()
        if keys [K_a] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys [K_d] and self.rect.x < 1200:
            self.rect.x += self.speed
        if keys[K_SPACE]:
            self.jump=True
        
        if(not self.jump):
            self.rect.y += 3
        else:
            if self.jumpCount >= -10:
                self.rect.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.jumpCount -= 1
            else: 
                self.jumpCount = 10
                self.jump = False

player_1 = Player_1 (400, 400, 100, 100, 5)

map_elements = []
x=0
y=670
for i in range(0, int(screen_width/50)+1):
   
    w = Hero(x, y,50, 50, 0, f"Map_tile_35.png"  )
    x+=50
    map_elements.append(w)

   


x=0
y=500

for el in map.split():
    x += 50
    if el == "1":
        w = Hero(x, y, 50, 50,0, "Map_tile_05.png")
        map_elements.append(w)

    if el == "2":
        w = Hero(x, y, 50, 50,0, "Map_tile_08.png")
        map_elements.append(w)

    if el == "3":
        w = Hero(x, y, 50, 50,0, "Map_tile_35.png")
        map_elements.append(w)
    if el == "4":
        y += 50
        x=0




clock = time.Clock()

def stop_game():
    global game
    game = False

def play_game():
    global pause 
    pause = False

btn1 =  Button(570, 450, stop_game, "button_EXIT.jpg")
btn2 =  Button(570, 380, play_game, "button_PLAY.jpg")

while game:
    for e in event.get():
        if pause:
            btn1.click(e)
            btn2.click(e)
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                if not pause: 
                    pause = not pause
            
            
    
    if pause:

        window.blit(background_pause, (0,0))
        btn1.reset(window)
        btn2.reset(window)

        display.update()
        clock.tick(60)
        continue

    
    window.blit(background, (0,0))

    for i in map_elements:
        if player_1.rect.colliderect(i.rect):
            player_1.rect.y=670-50
        i.reset()
    player_1.reset()
    player_1.move()    


    display.update()
    clock.tick(60)