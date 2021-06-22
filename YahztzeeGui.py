import random as R
from tkinter import *
import Dice as D
#I chosse this name becuse it
class pigPile:
    YGui=Tk()
    YGui.title("Yahtzee")
    YGui.minsize(504,336)
    #mypyTest("This shouldn't work because of mypy(str !=int)")
    def DoSomething(self,event):
        print(self.rerollAll()) 
    dice=Button(YGui,text="Confirm")
    #trying to add argument to bind 
    xyz=lambda:DoSomething()
    dice.bind("<Button-1>",xyz)
    dice.place(x=10,y=10,height=20,width=100)
    
    
    diceList=[]
    for n in range(4):
        x=D.Dice(n)
        diceList.append(x)
#     for _ in range(4):
#         dicelist=dicelist.
        
    #thinking about mypy for static
    def mypyTest(self,intiger:int)->None:
        print(intiger)
#    mypyTest("This shouldn't work because of mypy(str !=int)")
    #diceCurrenit={1:reroll(),2:reroll(), 3:reroll(),4:reroll(),5:reroll()}
    YGui.mainloop()
    
