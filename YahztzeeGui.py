import random as R
from tkinter import *
YGui=Tk()
##frame=Frame(top)
YGui.title("Test 123")
YGui.minsize(504,336)

dice=Button(YGui,text="Confirm", command=lambda:print(list(rerollAll().values())))
dice.place(x=10,y=10,height=20,width=100) 
def rerollAll():
	for diceRerolled in diceCurrent:
            diceCurrent[diceRerolled]=reroll()
	return diceCurrent
#I used this because it gives unique every time	
def reroll():
    return R.randint(1,6)

#util vital could go into its own class
def rerollSome(dices):
    try:
        #if type(dices) is list
        dices.index(0)
        raise TypeError("lists only") 
    except ValueError:
        #print("it doesn't have 0 being changed")
        for diceRerolled in dices:
            diceCurrent[diceRerolled]=reroll()
diceCurrent={1:reroll(),2:reroll(), 3:reroll(),4:reroll(),5:reroll()}

mainloop()
#tesing class will be in seperate file. I think this will be {name here}
class testing:#Dice:#rapid swap
	##test
	def __init__(self,dicegroup, numside,place):
		self.num = numside
		self.place=place
		self.inorder=isinorder(place,dicegroup)
	#def test(self):
		#print(diceCurrent.values())
		#this will be replaced by gui 
		#listtochange=[1,3,5]
		#rerollSome(listtochange)
		#print(diceCurrent.values())
	def isinorder(self,position,dices):
		if position != 1 and dices.get(position-1) is self.num-1:
			print("me and the dice before")
		#dice.get()
	def reroll():
   		return R.randint(1,6)

