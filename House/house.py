class House:

    ##Consturctor, initilizes across, left, right, corner to be empty
    def __init__(self,neighborhood,block,lot):
        self.neighborhood = neighborhood
        self.block = block
        self.lot = lot
        self.across = []
        self.left = [None,None,None]
        self.right = [None,None,None]
        self.corner = []

    ##Effects: Returns an array of neighborhood, block, lot for this house
    def getID(self):
        temp = []
        temp.append(self.neighborhood)
        temp.append(self.block)
        temp.append(self.lot)
        return temp
    
    ##Effects: Appends the house to the end of the across list
    def insertAcross(self,house):
        self.across.append(house)

    ##Effects: Appends the house to the end of the left list
    ##         Order of insertions matters
    def insertLeft(self,house,position):
        if (position >=0 and position <= 2):
            self.left[position] = house

    ##Effects: Appends the house to the end of the right list
    ##         Order of insertions matters
    def insertRight(self,house,position):
        if (position >=0 and position <= 2):
            self.right[position] = house

    ##Effects: Appends the house to the end of the corner list
    def insertCorner(self,house):
        self.corner.append(house)

    
objA = House("A",1,2)
objB = House("B",3,4)
objC = House("C",5,6)




    