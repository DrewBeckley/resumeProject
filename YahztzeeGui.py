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
    xyz=DoSomething
    dice.bind("<Button-1>",xyz)
    dice.place(x=10,y=10,height=20,width=100)
    
    
    
    def mypyTest(self,intiger:int)->None:
        print(intiger)
    diceList=[]
    for n in range(4):
        x=D.Dice(n)
        diceList.append(x)
#     mypyTest("This shouldn't work because of mypy(str !=int)")

    #logic part/archive
    def rerollAll(self):
        for diceRerolled in self.diceList:
            diceRerolled.reroll()
        return self.diceList 

    def DoSomething(self):
        print(self.rerollAll())
    #util vital could go into its own class
    def rerollSome(self,dices):
        try:
            dices.index(0)
            raise TypeError("lists only! you gave it a "+type(dices)) 
        except ValueError:
            for diceRerolled in dices:#diceCurrent[diceRerolled]=reroll()
                diceRerolled.reroll()



    #just to keep the interpriter from complaining
    def reroll(self):
        return R.randint(1,6)
    #diceCurrenit={1:reroll(),2:reroll(), 3:reroll(),4:reroll(),5:reroll()}
    YGui.mainloop()
    
