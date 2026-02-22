import pygame as pg 
import sys
from Papers import Paper
from Rocks import Rock
from Scissors import Scissor
pg.init()


class RPS:
    def __init__(self):
        #Window
        self.win = pg.display.set_mode((400,600))
        pg.display.set_caption("Rock Paper Scissors")
        
        
        #Background
        self.bg_img=pg.transform.scale_by(pg.image.load(r"/Users/guri/Rock-Paper-scissors/assets/Background.jpg").convert_alpha(),20)
        self.bg_rect=self.bg_img.get_rect(center=(100,200))
    
    
        #Calling Other Classes
        self.paper=Paper()
        self.rock=Rock()
        self.scissor=Scissor()
    
    
        #font 
        self.font=pg.font.Font(r"/Users/guri/Rock-Paper-scissors/assets/font.ttf",25)
        self.text=self.font.render("Select your option",True,(255,255,255),(0,0,0))
        self.text_rect=self.text.get_rect(center=(190,190))
    
    
    def Gameloop(self):
        while True:                 #infinite loof for window to keep on displaying
            for event in pg.event.get():
                if event.type == pg.QUIT: #quiting when cliked on X
                    sys.exit()
                    
                    
            self.Display()          #Display function 
            pg.display.flip()       #Keep showing the display
            
            
            
            
    def Display(self):
        self.win.blit(self.bg_img,self.bg_rect) # Background 
        self.paper.Display(self.win)            # Called the Paper class and used the display
        self.rock.Display(self.win)             # Called the Rock class and used the display
        self.scissor.Display(self.win)          # Called the Scissors class and used the display
        self.win.blit(self.text,self.text_rect)
            
            
            
            
            
            
c1=RPS()
c1.Gameloop()