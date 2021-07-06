from collections import Counter
class YahtzeeLogic:
    #could all be all static methods
    #This class is for the logic of yahtzee game. I was thinking of pure functions and inmutablitity
    #I will have 3 process method that will break it down in three ways:
    """The first way will be a dicinary of each side rolled.
This mean I can use this for the Yahtzee,upper section  of the score card, and x of a kind.
The next is a sorted list to see if it is a x of a kind,yahtzee(by seeing if ends match)
ordered list of sides for straights
"""
    
    def dictBreakDown(self,diceList):
        #testing out may need to adjust later
        #dictVerson={i:diceList for i in range(0,len(diceList))}
        data=Counter(diceList)
        return data#dictVerson
    #need to do a mutation check to see if it changes the orginal lists
    def sortedVersion(self,diceList):
        return diceList.sort()
    
    def isFullHouse(self,rolls):
        pass
#         try:
#             rolls.index(1)
#             
#         except valueError:
    
    #This could use small straight then
    def isLargeStraight(self):
        pass
    def isSmallStraight(self):
        pass
    def chance(self):
        ##sum up either using a build in function,reduce operation, or imperitive style
        pass
    def Breakdown(self):
        #Ths is where a list  or dict could be returned for the gui. I plan to have a gui
        #have all score boxes options and hilight the ones that are legal to pick for testing
        pass
        
#logic part for rolling the dice/archive
    def rerollAll(self,diceList):
        for diceRerolled in diceList:
            diceRerolled.reroll()
        return diceList 

    def DoSomething(self):
        print(self.rerollAll())
    def reroll(self):
        return R.randint(1,6)
    def rerollSome(self,dices):
        try:
            dices.index(0)
            raise TypeError("lists only! you gave it a "+type(dices)) 
        except ValueError:
            for diceRerolled in dices:
                diceRerolled.reroll()
                return dices
    def getNum(self,List):
        return list(map(lambda a:a.getNum(),List))
        #return list(map(Str,List))
print("this could be creating a gui")