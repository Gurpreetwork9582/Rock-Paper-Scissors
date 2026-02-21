import random

class RPS:
    def __init__(self, Player_selection):
        self.player_selection=Player_selection
    
    # Computer Selection
    def Comp_Selection(self):            
        Dict = {
                0:'Rock', 
                1:'Paper', 
                2:'Scissors'
                }
        self.a =random.randint(0,len(Dict)-1)
        self.comp_selec= Dict.get(self.a)
        print("Computer chooses: " +self.comp_selec)
        
    
    # Comparing the results to see the winner    
    def Comparing(self):
        self.result = self.a
        
        if self.player_selection == self.result:
            print("You Tie")
        
        elif (self.player_selection == 0 and self.result == 1) or (self.player_selection == 1 and self.result == 2) or (self.player_selection == 2 and self.result == 0):
            print("Computer 'Got you'")
            
        else:
            print("You Won 'Hurrah'")




print("\t**PLAY WITH THE COMPUTER** \nMAKE YOU SELCTION AND TRY TO WIN WITH COMP" )
print("0.ROCK \n1.PAPER\n2.SCISSORS\n")

Player_Selection = int(input("WHAT DO YOU CHOOSE\t"))
while True:
    if Player_Selection == 0:
        print("Your chose: Rock")
    elif Player_Selection == 1:
        print("Your chose: Paper")
    elif Player_Selection == 2:
        print("Your chose: Scissors")
    else:
        print("Not a right choice\nPlease enter numbers from the List")
        break
    break


c1 = RPS(Player_Selection)
c1.Comp_Selection()
c1.Comparing()