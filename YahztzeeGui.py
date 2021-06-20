import random as R
from tkinter import *
YGui=Tk()
##frame=Frame(top)
YGui.title("Test 123")
YGui.minsize(504,336)

dice=Button(YGui,text="Confirm", command=lambda:print(list(rerollAll().values())))
dice.place(x=10,y=10,height=20,width=100) 

#diceList=[Dice(),Dice(),Dice(),Dice(),Dice()]
#logic part/archive***********
def rerollAll(diceCurrent):
	for diceRerolled in diceCurrent:
		diceRerolled.reroll()
	#return diceCurrent


#util vital could go into its own class
def rerollSome(dices):
	try:
		dices.index(0)
		raise TypeError("lists only! you gave it a "+type(dices)) 
	except ValueError:
		for diceRerolled in dices:#diceCurrent[diceRerolled]=reroll()
			diceRerolled.reroll()



#just to keep the interpriter from complaining
def reroll():
	return R.randint(1,6)
diceCurrent={1:reroll(),2:reroll(), 3:reroll(),4:reroll(),5:reroll()}
mainloop()