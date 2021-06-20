import random as R
from tkinter import *
YGui=Tk()
##frame=Frame(top)
YGui.title("Test 123")
YGui.minsize(504,336)


dice=Button(YGui,text="Submit Text")
dice.place(x=100,y=100,height=20,width=100)
def reroll():
    roled=R.randint(1,7)
    return roled
def rerollSome(dices):
    try:
        #if type(dices) is list
        dices.index(0)
        raise TypeError("lists only") 
    except ValueError:
        #print("it doesn't have 0 being changed")
        for diceRerolled in dices:
            diceCurrent[diceRerolled]=reroll()
#roll=R.randint(0,7)
diceCurrent={1:reroll(),2:reroll(), 3:reroll(),4:reroll(),5:reroll()}
print(diceCurrent.values())
#this will be replaced by gui 
listtochange=[1,3,5]
rerollSome(listtochange)
#print(diceCurrent.values())
