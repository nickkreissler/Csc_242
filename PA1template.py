class transportcenter(object):
    def __init__(self,numunits,uin,uout,spaces):
        self.beginningunits = numunits
        self.numunits = numunits + uin
        self.uin = uin
        self.uout = uout
        self.spaces = spaces - self.numunits
    def unitsIn(self,unitsIn):
        self.numunits += unitsIn
        self.uin += unitsIn
        self.spaces -= unitsIn
    def unitsOut(self,numOut):
        if numOut > self.numunits:
            print("Can't have more units out than in")
        else:
            self.numunits -= numOut
            self.uout+=numOut
            self.spaces += numOut
    def unitsHere(self):
        return self.numunits
    def unitsPrint(self):
        print("Total units in {}, Total units out {}".format(self.uin,self.uout))
    def unitCheck(self):
        print("Units here now {}".format(self.numunits))
        print("Units at start {} + units in {} - units out {} = {}".format(self.beginningunits,self.uin,self.uout,self.numunits))
class airport(transportcenter):
    def __init__(self,numunits,uin,uout,spaces):
        self.runways = spaces
        super(airport,self).__init__(numunits,uin,uout,spaces)
    def addRunways(self,numRunways):
        self.runways += numRunways
    def remRunways(self,numRunways):
        self.runways -= numRunways
    def unitsPrint(self):
        print("Total units in: {}, Total units out: {} Total Runways: {}".format(self.uin,self.uout, self.runways))


otc = transportcenter(0,0,0,100)
print(otc.unitsIn(100))
print(otc.uin)
otc.unitsOut(1000)
print(otc.unitsOut(10))
print(otc.unitsHere())
otc.unitsPrint()
otc.unitCheck()
print(otc.spaces)
x = airport(1,3,0,100)
x.unitsPrint()
x.addRunways(39)
x.unitsPrint()
x.remRunways(10)
x.unitsPrint()
x.unitsIn(20)
x.unitsOut(10)
x.unitCheck()
print(x.spaces)