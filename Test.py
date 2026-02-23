import pygame as pg 
import sys,random
from Papers import Paper
from Rocks import Rock
from Scissors import Scissor
pg.init()


class RPS:
    def __init__(self):
        #Window
        self.win = pg.display.set_mode((470,650))
        pg.display.set_caption("Rock Paper Scissors")
        
        
        #Background
        self.bg_img=pg.transform.smoothscale_by(pg.image.load(r"/Users/guri/Rock-Paper-scissors/assets/Background.jpg").convert_alpha(),0.75)
        self.bg_rect=self.bg_img.get_rect(center=(100,200))
    
    
        #Calling Other Classes
        self.paper=Paper()
        self.rock=Rock()
        self.scissor=Scissor()
    
    
        #font 
        self.font=pg.font.Font(r"/Users/guri/Rock-Paper-scissors/assets/font.ttf",25)
        self.text=self.font.render("Select your option",True,(255,255,255),(0,0,0))
        self.text_rect=self.text.get_rect(center=(190,190))
    
    
    
    
        #Empty Place to place the hands for player
        self.option_img = None
        self.option_rect = pg.Rect(153,250,50,50)
        self.is_opt_selected= False
        
        
        #Empty Place for Computer to Select
        self.option_comp_img = None
        self.option_comp_rect=pg.Rect(153,400,50,50)
    
        #Score
        self.score_font=pg.font.Font("/Users/guri/Rock-Paper-scissors/assets/font.ttf",30)
        self.score=self.score_font.render("Score : 0", True, (255,255,255))
        self.score_rect=self.score.get_rect(center=(350,420))
        
        
        #Result
        self.result_font=pg.font.Font("/Users/guri/Rock-Paper-scissors/assets/font.ttf",30)
        self.result=self.result_font.render("Result", True, (255,255,255))
        self.result_rect=self.score.get_rect(center=( self.win.get_width() // 2,
        int(self.win.get_height() * 0.9)))

        
        
    def Gameloop(self):
        while True:                 #infinite loof for window to keep on displaying
            for event in pg.event.get():
                if event.type == pg.QUIT: #quiting when cliked on X
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.paper.Paper_rect.collidepoint(event.pos):
                        self.option_img = self.paper.Selection_paper()
                        self.is_opt_selected= True
                    if self.rock.Rock_rect.collidepoint(event.pos):
                        self.option_img = self.rock.Selection_rock()
                        self.is_opt_selected= True
                    if self.scissor.Scissors_rect.collidepoint(event.pos):
                        self.option_img = self.scissor.Selection_scissors()
                        self.is_opt_selected= True
                        
            #** need to place computer selection**#        
                if self.is_opt_selected:        
                    self.Comp_Selection() 
                    self.Comparing()
                    self.is_opt_selected=False 
                 
                    
            self.Display()          #Display function 
            pg.display.flip()       #Keep showing the display
            
            
            
            
    def Display(self):
        self.win.blit(self.bg_img,self.bg_rect) # Background 
        self.paper.Display(self.win)            # Called the Paper class and used the display
        self.rock.Display(self.win)             # Called the Rock class and used the display
        self.scissor.Display(self.win)          # Called the Scissors class and used the display
        self.win.blit(self.text,self.text_rect) # Text "choose you option"
        self.win.blit(self.score,self.score_rect)#Score 
        
        if self.option_img:                     # Player selection img
            self.win.blit(self.option_img,self.option_rect)
        
        if self.option_comp_img:                #Computer Chosen img
            self.win.blit(self.option_comp_img,self.option_comp_rect)
         
        if self.option_img and self.option_comp_img:    
            self.win.blit(self.result,self.result_rect)
        
        
    
    # Computer Selection
    def Comp_Selection(self):            
        Dict = {
                0:'Rock',                       #list of options
                1:'Paper', 
                2:'Scissors'
                }
        self.a =random.randint(0,len(Dict)-1) #Randomly selecting the option
        self.comp_selec= Dict.get(self.a)
        print("Computer chooses: " +self.comp_selec)
        
        if self.a == 0:
            self.option_comp_img = self.rock.Selection_rock()
        if self.a == 1:
            self.option_comp_img =self.paper.Selection_paper()
        if self.a == 2:
            self.option_comp_img = self.scissor.Selection_scissors()
        
        
            
    # Comparing the results to see the winner    
    def Comparing(self):
        
        if self.option_img == self.option_comp_img:
            self.result=self.result_font.render("YOU TIE", True, (255,255,255))
        
        elif (self.option_img == self.rock.Selection_rock() and self.option_comp_img  == self.paper.Selection_paper()) or (self.option_img == self.paper.Selection_paper() and self.option_comp_img  == self.scissor.Selection_scissors()) or (self.option_img == self.scissor.Selection_scissors() and self.option_comp_img  == self.rock.Selection_rock()):
            self.result=self.result_font.render("COMPUTER GOT YA", True, (255,255,255))
            
        else:
             self.result=self.result_font.render("Hurrehhh, YOU WON!!!", True, (255,255,255))
            
            
c1=RPS()
c1.Gameloop()