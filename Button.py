import pygame as pg


class Button:
    def __init__(self,win):
        self.win = win
        self.Reset_button_font=pg.font.Font("assets/font.ttf",20)
        
        self.Reset_button_text=self.Reset_button_font.render("Click on the button to reset the game", True, (255,255,255))
        self.Reset_button_text_rect=self.Reset_button_text.get_rect(center=( self.win.get_width() // 2,425))  
        
        self.Reset_button=self.Reset_button_font.render("Button", True, (0,0,0))
        self.Reset_button_rect=self.Reset_button.get_rect(center=( self.win.get_width() // 2,475))  
        
        
    def draw(self):
        self.win.blit(self.Reset_button_text,self.Reset_button_text_rect)
        self.win.blit(self.Reset_button,self.Reset_button_rect)