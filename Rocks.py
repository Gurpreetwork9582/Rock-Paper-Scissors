import pygame as pg



class Rock():
    def __init__(self):
        self.Rock_img=pg.transform.scale_by(pg.image.load(r'/Users/guri/Rock-Paper-scissors/assets/Rock.png', "Rock").convert_alpha(),.5)
        self.Rock_rect=self.Rock_img.get_rect(center=(230,80))
        
        
    def Display(self,win):
        win.blit(self.Rock_img,self.Rock_rect)
            
            
            
    def Selection_rock(self):
        return self.Rock_img