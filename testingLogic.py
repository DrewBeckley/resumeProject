#This class is for test data and asert =,not,and or
class TestLogic:
    from unittest import TestCase as T
    import YahtzeeLogic as Y
    
    def resultTestEquals(self,function,properResult):
        return function==properResult
    def testFullHouseCheck():
        #print(dir())
        x=Y.YahtzeeLogic()
        #print(x.isFullHouse([1,1,1,2,2]))
        tester=TestCase()
        tester.assertEquals('foo'.upper(), 'FOO')
        #print(x.isFullHouse([1,1,1,2,2]))
        #print(x.isFullHouse([1,1,1,2,2]))
class cases:
    def getFullHouse():
        return [1,1,1,2,2]
    def notgetFullHouse():
        return [1,1,1,2,3]
#print("import success")