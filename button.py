from pygame import *

class Button:
    def __init__ (self, window,screen_width, screen_height, onclick_function):
        self.window = window
        self.width = 70
        self.height = 30
        self.x = 100
        self.y = 100
        self.onclick_function = onclick_function

        font.init()
        self.font1 = font.Font(None, 50)
        self.rect = rect.Rect(self.x, self.y, self.width, self.height)

    def reset(self):
        draw.rect(self.window, (255,255,255), rect.Rect(self.x, self.y, self.width, self.height))
        self.window.blit(self.font1.render("Exit", True, (0, 0, 0)),(self.x, self.y))

        
    def click(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):   
                self.onclick_function()

            
