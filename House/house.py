import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from House.exceptions import *
from Queries.query import *

class House:

    modelToColorDict = {'CL' : ['CL - 1.1', 'CL - 2.1', 'CL - 3.1', 'CL - 4.1','CL - 5.1','CL - 6.1','CL - 7.1','CL - 8.1','CL - 9.1','CL - 10.1'],
                        'CR' : ['CR - 1.1', 'CR - 2.1', 'CR - 3.1', 'CR - 4.1','CR - 5.1','CR - 6.1','CR - 7.1','CR - 8.1','CR - 9.1','CR - 10.1'],
                        'PR' : ['PR - 1.1', 'PR - 2.1', 'PR - 3.1', 'PR - 4.1','PR - 5.1','PR - 6.1','PR - 7.1','PR - 8.1','PR - 9.1','PR - 10.1']}

    ##Consturctor, initilizes across, left, right, corner to be empty
    def __init__(self,neighborhood,block,lot,across,left,right,corner,pair):
        self.neighborhood = neighborhood
        self.block = block
        self.lot = lot
        self.across = across
        self.left = left
        self.right = right
        self.corner = corner
        self.pair = pair

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

    ##Effects: Returns a list of all colours this house can be,
    ##         If this house does not yet have a model, returns []
    def colours(self):
        id = self.getID()
        
        model = self.getModel(id[0],id[1],id[2])
        if (model == "PR"):
            return self.getPrarieColors(self.modelToColorDict['PR'])
        elif (model == "CR"):
            return self.getCraftsmanColors(self.modelToColorDict['CR'])
        elif (model == "CL"):
            return self.getColonialColors(self.modelToColorDict['CL'])
        else:
            raise InvalidModelException(model)
        
    ## EFFECTS: returns a list of all the possible colors a house can be based on the list of possiblities
    def getColorsForModel(self,possibleColors):
        oneLeftColor = self.getColor(self.left[0][0],self.left[0][1],self.left[0][2])
        twoLeftColor = self.getColor(self.left[1][0],self.left[1][1],self.left[1][2])
        oneRightColor = self.getColor(self.right[0][0],self.right[0][1],self.right[0][2])
        twoRightColor = self.getColor(self.right[1][0],self.right[1][1],self.right[1][2])
        possibleColors.remove(oneLeftColor)
        possibleColors.remove(twoLeftColor)
        possibleColors.remove(oneRightColor)
        possibleColors.remove(twoRightColor)
        for cross in self.across:
            possibleColors.remove(self.getColor(cross[1],cross[2],cross[3]))
        return possibleColors
        

    
    
    ##Effects: Returns a list of all medels this house can be
    def models(self):
        print("Stub")

    ##Effects: Returns a list of all elevations this house can be
    def elevations(self):
        print("Stub")

    ##Effects: Queries the database and retruns the color of the house with 
            ##Provided neighborhood, block, lot numbers
            ##If the house does not exist, returns ""
    def getColor(self,neighborhood,block,lot):
        result = selectSingle(neighborhood,block,lot)
        if (len(result) == 0):
            return ""
        else:
            return result[0][7]
        
        
     ##Effects: Queries the database and retruns the color of the house with 
            ##Provided neighborhood, block, lot numbers
            ##If the house does not exist, returns ""
    def getModel(self,neighborhood,block,lot):
        print("stub")

     ##Effects: Queries the database and retruns the color of the house with 
            ##Provided neighborhood, block, lot numbers
            ##If the house does not exist, returns ""
    def getElevation(self,neighborhood,block,lot):
        print("stub")

obj = House("A",1,1,[],[],[],[],[])
try:
    obj.colours()
except InvalidModelException as e:
    print("Error", e)







    