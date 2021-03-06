#Nick Kreissler

#Collaborators = 0


class Building:
    def __init__(self,squarefootage, yearbuilt):
        self.squarefootage = squarefootage
        self.yearbuilt = yearbuilt
        self.age = 2018 - yearbuilt

    def __repr__(self):
        return "({}, {})".format(self.squarefootage, self.yearbuilt)

    def __str__(self):
        return "Building: {} years old, {} square feet".format(self.age, self.squarefootage)

class Residence(Building):
    def __init__(self, squarefootage, name, yearbuilt, rooms, boolean, value, squarefootagelot, squarefootagelot1):
        self.name = name
        self.squarefootagesquared = squarefootagelot*squarefootagelot1
        self.rooms = rooms
        self.value = value
        self.boolean = boolean
        if self.boolean == True:
            self.basement = 'basement'
        else:
            self.basement = 'no basement'
        super(Residence, self).__init__(squarefootage, yearbuilt)

    def setpropvalue(self, value):
        self.value = value

    def showsquarefootage(self):
        return self.squarefootagesquared

    def showpropvalue(self):
        return self.value

    def __repr__(self):
        return "Residence {}: {}, {:,}, {}, {:,}, {}, {:,}".format(self.name, self.age, self.squarefootage,self.rooms,self.squarefootagesquared, self.boolean,self.value)

    def __str__(self):
        return "Residence {}: {} years old, {:,} square feet, {} rooms, {:,} sq ft lot, {}, value ${:,}".format(self.name, self.age, self.squarefootage,self.rooms,self.squarefootagesquared, self.basement,self.value)

class Commercial(Building):
    def __init__(self, floors,value, zoning,squarefootage, yearbuilt):
        self.age = 2018 - yearbuilt
        self.floors = floors
        self.zoning = zoning
        self.value = value
        super(Commercial, self).__init__(squarefootage, yearbuilt)

    def showzoning(self):
        return self.zoning

    def setpropvalue(self, value):
        self.value = value

    def showpropvalue(self):
        return self.value

    def __repr__(self):
        return "Commercial: {}, {:,}, {}, {}, {:,}".format(self.age, self.squarefootage, self.floors, self.zoning, self.value)

    def __str__(self):
        return "Commercial: {} years old, {:,} square feet, {} floors, {} zoning, value ${:,}".format(self.age, self.squarefootage, self.floors, self.zoning, self.value)

class House(Residence):
    def __init__(self,squarefootage, name, yearbuilt, rooms, boolean, value, squarefootagelot, squarefootagelot1, name1):
        self.name1 = name1
        super(House, self).__init__(squarefootage, name, yearbuilt, rooms, boolean, value, squarefootagelot, squarefootagelot1)

    def __repr__(self):
        return "House {}: {} {}, {:,}, {}, {:,}, {}, {:,}".format(self.name, self.name1, self.age, self.squarefootage,self.rooms,self.squarefootagesquared, self.boolean,self.value)

    def __str__(self):
        return "House {}: {}, {} years old, {:,} square feet, {} rooms, {:,} sq ft lot, {}, value ${:,}".format(self.name, self.name1, self.age, self.squarefootage,self.rooms,self.squarefootagesquared, self.basement,self.value)

print("")
r1 = Building(6700, 1995)
print(r1.__repr__())
print(r1)

print("")
r1 = Residence(1200, "Windy Corners", 2000, 10 ,False, 55000,200,200)
print(r1.__repr__())
print(r1)

print("")
r1 = Commercial(10,50000,2,10000,1999)
print(r1.__repr__())
print(r1)

print("")
r1 = House(1200, "Windy Corners", 2000, 10 ,False, 55000,200,200,"Ranch")
print(r1.__repr__())
print(r1)
