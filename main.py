import YahtzeeLogic as Y
from testingLogic import cases
import unittest
#this will be the main that kick off everything but for now just testing the logic
x=Y.YahtzeeLogic()

print(dir())
x=cases.getFullHouse()
print(x)