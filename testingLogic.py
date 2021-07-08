import unittest as T

#This class is for test data and asert =,not,and or
class TestLogic:
    import unittest as T
    
    def resultTestEquals(self,function,properResult):
        return function==properResult
    def testFullHouseCheck():
        import YahtzeeLogic as Y
        print(dir())
        x=Y.YahtzeeLogic()
        print(x.isFullHouse([1,1,1,2,2]))
        print(dir(T.TestCase))
        #T.assertEquals('foo'.upper(), 'FOO')
        print(x.isFullHouse([1,1,1,2,2]))
        print(x.isFullHouse([1,1,1,2,2]))
class cases:
    def getFullHouse():
        return [1,1,1,2,2]
    def notgetFullHouse():
        return [1,1,1,2,3]
#print("import success")