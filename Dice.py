import random as R
class Dice:
    def __init__(self,place):
        self.num = R.randint(1,6)
        self.place=place
        #self.inorder=isinorder(place,dicegroup)
    def isinorder(self,position,dices):
        if self.position != 1 and dices.get(self.position-1) is self.num-1:
            print("me and the dice before are in order")
        #dice.get()
    #I used this because it gives unique every time
    def reroll(self):
        self.num=R.randint(1,6)

