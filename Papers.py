import pygame as pg



class Paper():
    def __init__(self):
        self.Paper_img=pg.transform.scale_by(pg.image.load(r'/Users/guri/Rock-Paper-scissors/assets/Paper.png',"Paper").convert_alpha(),0.10)
        self.Paper_rect=self.Paper_img.get_rect(center=(80,80))
        
        
        
        
    def Display(self,win):
        win.blit(self.Paper_img,self.Paper_rect)
            