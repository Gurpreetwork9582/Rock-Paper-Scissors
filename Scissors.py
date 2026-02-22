import pygame as pg



class Scissor():
    def __init__(self):
        self.Scissors_img=pg.transform.scale_by(pg.image.load(r'/Users/guri/Rock-Paper-scissors/assets/Scissors.png', "Scissors").convert_alpha(),0.10)
        self.Scissors_rect=self.Scissors_img.get_rect(center=(320,80))
        
        
    def Display(self,win):
        win.blit(self.Scissors_img,self.Scissors_rect)
            
            
    def Selection_scissors(self):
        return self.Scissors_img