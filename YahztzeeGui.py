import random as R
from tkinter import *
YGui=Tk()
##frame=Frame(top)
YGui.title("Test 123")
YGui.minsize(504,336)
diceCurrent={1:reroll(),2:reroll(), 3:reroll(),4:reroll(),5:reroll()}
dice=Button(YGui,text="Confirm", command=lambda:print(list(rerollAll().values())))
dice.place(x=100,y=100,height=20,width=100) 
def rerollAll():
	for diceRerolled in diceCurrent:
            diceCurrent[diceRerolled]=reroll()
	return diceCurrent
#I used this because it gives unque	
def reroll():
    return R.randint(1,6)
def rerollSome(dices):
    try:
        #if type(dices) is list
        dices.index(0)
        raise TypeError("lists only") 
    except ValueError:
        #print("it doesn't have 0 being changed")
        for diceRerolled in dices:
            diceCurrent[diceRerolled]=reroll()
#tesing class
#class:
#
#def __init__(self, name, age):
    #self.name = name
    #self.isin
####
def testing():
	print(diceCurrent.values())
	#this will be replaced by gui 
	listtochange=[1,3,5]
	rerollSome(listtochange)
	print(diceCurrent.values())
mainloop()