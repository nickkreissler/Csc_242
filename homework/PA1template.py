class transportcenter(object):

    def __init__(self,numunits,uin,uout,spaces):
        self.beginningunits = numunits
        self.numunits = numunits + uin - uout
        self.uin = uin
        self.uout = uout
        self.spaces = spaces - self.numunits
        if self.spaces > spaces:
            print("more units are going out than coming in")
            self.spaces = spaces
        if self.spaces < 0:
            print("too many units are here currently")
            self.spaces = 0

    def unitsIn(self,unitsIn):
        self.numunits += unitsIn
        self.uin += unitsIn
        self.spaces -= unitsIn
        if self.spaces < 0:
            print('to many units...')

    def unitsOut(self,numOut):
        if numOut > self.numunits:
            print("Can't have more units out than in")
        else:
            self.numunits -= numOut
            self.uout+=numOut
            self.spaces += numOut

    def unitsHere(self):
        print(self.numunits)

    def unitsPrint(self):
        print("Total units in {}, Total units out {}".format(self.uin,self.uout))

    def unitCheck(self):
        print("Units here now {}".format(self.numunits))
        print("Units at start {} + units in {} - units out {} = {}".format(self.beginningunits,self.uin,self.uout,self.numunits))

class airport(transportcenter):

    def __init__(self,numunits,uin,uout,spaces):
        self.runways = 0
        super(airport,self).__init__(numunits,uin,uout,spaces)

    def addRunways(self,numRunways):
        self.runways += numRunways

    def remRunways(self,numRunways):
        self.runways -= numRunways
        if self.runways < 0:
            print("Can't have negative runways")
            self.runways = 0

    def unitsPrint(self):
        print("Total units in: {}, Total units out: {} Total Runways: {}".format(self.uin,self.uout, self.runways))



