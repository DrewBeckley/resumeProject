import random as R
from tkinter import *
import Dice as D
import YahtzeeLogic as logic#import *
#I chosse this name becuse it
#class pigPile:
def main():
    #try pygame once logic is up and correct
    YGui=Tk()
    YGui.title("Yahtzee")
    YGui.minsize(504,336)
    #mypyTest("This shouldn't work because of mypy(str !=int)")
    def testingRollAll():
        test=logic.YahtzeeLogic()
        output=test.rerollAll(diceList)
        print(output)
        try:
            print(test.getNum(output))
        except Exception as e:
            print("error "+str(e))
    
    
    dice=Button(YGui,text="Confirm",command=testingRollAll)
    #trying to add argument to bind when I had this in a class
    xyz=lambda:testingRollAll()
    #dice.bind("<Button-1>",xyz)
    dice.place(x=10,y=10,height=20,width=100)


    diceList=[]
    for n in range(5):
        x=D.Dice(n)
        diceList.append(x)
    #     for _ in range(4):
    #         dicelist=dicelist.
        
    #thinking about mypy for static
    def mypyTest(intiger:int)->None:
        print(intiger)
    #    mypyTest("This shouldn't work because of mypy(str !=int)")
    #diceCurrenit={1:reroll(),2:reroll(), 3:reroll(),4:reroll(),5:reroll()}
    YGui.mainloop()
#could uise the import 
if __name__=="__main__":
    main()
    
