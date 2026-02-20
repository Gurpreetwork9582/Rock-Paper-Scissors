import random

class RPS:
    def __init__(self):
        pass
    
    
    def Comp_Selection(self):            
        list = ["Rock", "paper", "Scissor"]
        a =random.randint(0,len(list)-1)
        print(list[a])








print("\t**PLAY WITH THE COMPUTER** \nMAKE YOU SELCTION AND TRY TO WIN WITH COMP" )
print("1.ROCK \n2.PAPER\n3.SCISSORS\n")

Player_Selection = int(input("WHAT DO YOU CHOOSE"))


c1 = RPS()
c1.Selection()