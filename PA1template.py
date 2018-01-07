       
class transportcenter(object):

    def __init__(self,numunits,uin,uout,spaces):
        self.beginningunits = 0
        self.numunits = numunits + self.beginningunits
        self.uin = uin
        self.uout = uout
        self.spaces = spaces
    
    def unitsIn(self,unitsIn):
        self.numunits += unitsIn
        self.uin += unitsIn
        return self.numunits

    def unitsOut(self,numOut):
        if numOut > self.numunits:
            print("Can't have more units out than in")
        else:
            self.numunits -= numOut
            self.uout+=numOut
            return self.numunits




    def unitsHere(self):
        return self.numunits

    def unitsPrint(self):
        print("Total units in {}, Total units out {}".format(self.uin,self.uout))



    def unitCheck(self):
        print("Units here now {}".format(self.numunits))
        print("Units at start {} + units in {} - units out {} = {}".format(self.beginningunits,self.uin,self.uout,self.numunits))
class airport(transportcenter):
    def __init__(self,numunits,uin,uout,spaces):
        self.runnways = spaces
        super(airport,self).__init__(numunits,uin,uout,spaces)
    def addRunways(self,numRunways):
        pass

    def remRunways(self,numRunways):
        pass
        
    def unitsPrint(self):
        super(airport,self).unitsPrint(), print("", end = 'Total runways is {}'.format(self.runnways))


otc = transportcenter(0,0,0,100)
print(otc.unitsIn(100))
print(otc.uin)
otc.unitsOut(1000)
print(otc.unitsOut(10))
print(otc.unitsHere())
otc.unitsPrint()
otc.unitCheck()
print(otc.spaces)
x = airport(0,2,3,10)
x.unitsPrint()