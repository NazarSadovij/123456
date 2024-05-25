from pygame import *
from button import Button


map = """ 
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 4
1 0 0 0 0 0 0 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 4
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 4
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 4
1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 0 0 0 0 0 0 1 4
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 4
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 4
1 2 2 2 2 2 2 2 2 2 2 2 2 2 0 0 0 0 2 2 2 2 2 2 2 2 2 2 2 1 4
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 4
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 4
1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 0 0 0 0 0 2 2 1 4
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 4
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 4
1 2 2 2 2 2 2 0 0 0 0 0 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 4
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 4
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 4
3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4
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



exit1 = Hero(200, 100, 80, 80, 0, "warer20001.png")
exit2 = Hero(1400, 850, 30, 40, 0, "light.png")

class Player_1(Hero):
    def move (self):
        keys = key.get_pressed()
        if keys [K_a] and self.rect.x > 5:
            self.rect.x -= self.speed


        if keys [K_d] and self.rect.x < screen_width:
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

player_1 = Player_1 (400, 850, 100, 100, 5)



class Player_2(Hero):
    def move (self):
        keys = key.get_pressed()
        if keys [K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys [K_RIGHT] and self.rect.x < screen_width:
            self.rect.x += self.speed
        if keys[K_UP]:
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

player_2 = Player_2 (100, 100, 100, 100, 5, "Players_2.jpg")

map_elements = []


x=screen_width
y=screen_height

map = map.split()
map.reverse()


for el in map:
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
        y -= 50
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

font1 = font.Font(None, 80)


finish = False

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
            player_1.rect.y=i.rect.y - 50
            #if player_1.rect.bottom<=i.rect.bottom and player_1.rect.bottom>=i.rect.top:
                #player_1.rect.bottom=i.rect.top


        if player_2.rect.colliderect(i.rect):
            player_2.rect.y=i.rect.y - 50

        
        i.reset()

    if player_1.rect.colliderect(exit1.rect) and player_2.rect.colliderect(exit2.rect):
        finish = True

    if finish == True:
        font1.render
        window.blit(font1.render("You Win", True, (255, 255, 255)), (647, 500))



    player_1.reset()
    player_1.move()  


    player_2.reset()
    player_2.move()    
  
    exit1.reset()
    exit2.reset()
    

    display.update()
    clock.tick(60)