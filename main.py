import YahtzeeLogic as Y

from testingLogic import cases#,cases.getFullHouse
import unittest
#this will be the main that kick off everything but for now just testing the logic
x=Y.YahtzeeLogic()

print(dir())
fullhouse=cases.getFullHouse()
#print(fullhouse)
print(list(x.dictBreakDown(fullhouse)))