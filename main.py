import YahtzeeLogic as Y
from testingLogic import cases,TestLogic
#from testingLogic import cases,TestLogic#,cases.getFullHouse

#this will be the main that kick off everything but for now just testing the logic
x=Y.YahtzeeLogic()

print((dir()))
fullhouse=cases.getFullHouse()
#print(fullhouse)
print(len(x.dictBreakDown(fullhouse)))
TestLogic.testFullHouseCheck()