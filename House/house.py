import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from House.exceptions import *
from Queries.query import *

class House:

    elevationToColorDict = {'CL' : ['CL - 1.1', 'CL - 2.1', 'CL - 3.1', 'CL - 4.1','CL - 5.1','CL - 6.1','CL - 7.1','CL - 8.1','CL - 9.1','CL - 10.1'],
                        'CR' : ['CR - 1.1', 'CR - 2.1', 'CR - 3.1', 'CR - 4.1','CR - 5.1','CR - 6.1','CR - 7.1','CR - 8.1','CR - 9.1','CR - 10.1'],
                        'PR' : ['PR - 1.1', 'PR - 2.1', 'PR - 3.1', 'PR - 4.1','PR - 5.1','PR - 6.1','PR - 7.1','PR - 8.1','PR - 9.1','PR - 10.1']}
    
    footageToModels = {'44 ft\'s' : ['Armstrong','Bishop','Borgeua','Cline','Maclaren','Ptarmigan','Rutherford','Smythe','Bishop 2.0','Aberdeen','Rundle','Bluebell'],
                    '36 ft\'s' : ['Cypress','Fairview','Fullerton','Monarch','Whistler','Yamnuska','Norquay'],
                    '24 ft\'s' : ['Waputik','Palliser','Sundance','Finch','Cardinal','Starling']}

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
    ##         If this house does not have a vailid elevation, throws invalid elevation exception
    def colours(self):
        id = self.getID()
        elevation = self.getElevation(id[0],id[1],id[2])
        if (elevation == "PR" or elevation == "CR" or elevation == "CL"):
            return self.getColorsForElevation(self.elevationToColorDict[elevation])
        else:
            raise InvalidElevationException(elevation)
        
    ## EFFECTS: returns a list of all the possible colors a house can be based on the list of possiblities
    def getColorsForElevation(self,possibleColors):
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
        

    
    
    ##Effects: Returns a list of all models this house can be, Throws InvalidFootageException if this house does not have valid Footage
    def models(self):
        id = self.getID()
        footage = self.getFootage(id[0],id[1],id[2])
        if (footage == '44 ft\'s' or footage ==  '36 ft\'s' or footage ==  '24 ft\'s'):
            return self.modelsForSize(self.footageToModels(footage))
        else:
            raise InvalidFootageException(footage)
        

    def modelsForSize(self,possibleModels):
        id = self.getId()
        elevation = self.getElevation(id[0],id[1],id[2])

        if (elevation != None and elevation != " "):
            ##This house does have en elevation

            ##3 in row rule
            oneLeftModel = self.getModel(self.left[0][0],self.left[0][1],self.left[0][2])
            twoLeftModel = self.getModel(self.left[1][0],self.left[1][1],self.left[1][2])
            oneRightModel = self.getModel(self.right[0][0],self.right[0][1],self.right[0][2])
            twoRightModel = self.getModel(self.right[1][0],self.right[1][1],self.right[1][2])
            if (oneLeftModel == twoLeftModel):
                possibleModels.remove(oneLeftModel)
            if (oneLeftModel == oneRightModel):
                possibleModels.remove(oneLeftModel)
            if (oneRightModel == twoRightModel):
                possibleModels.remove(twoRightModel)

            ##Two away / corner Rule
            effectsMod = [self.left[0],self.left[1],self.right[0],self.right[1]]

       
            for h in self.corner:
                effectsMod.append(h)

            for h in effectsMod:
                if (self.getElevation(h[0],h[1],h[2]) == elevation):
                    possibleModels.remove(self.getModel(h[0],h[1],h[2]))

            ## 30% Rule
            modelCounts = self.modelCountsBlockElevation(id[0],id[1],elevation)
            blocksize = self.getBlockSize(id[0],id[1])
            cutoff = blocksize/3

            ##Possible need for delta when dividing
            for p in modelCounts:
                if (p[1] + 1 > cutoff):
                    possibleModels.remove(p[0])

            return possibleModels
            





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
        result = selectSingle(neighborhood,block,lot)
        if (len(result) == 0):
            return ""
        else:
            return result[0][5]

     ##Effects: Queries the database and retruns the color of the house with 
            ##Provided neighborhood, block, lot numbers
            ##If the house does not exist, returns ""
    def getElevation(self,neighborhood,block,lot):
        result = selectSingle(neighborhood,block,lot)
        if (len(result) == 0):
            return ""
        else:
            return result[0][6]
    
    ##Effects: Returns the footage value fo the given house
    def getFootage(self,neighborhood,block,lot):
        result = selectSingle(neighborhood,block,lot)
        if (len(result) == 0):
            return ""
        else:
            return result[0][9]
        
    ##Effects: Returns an array of all the models and elevation pairs for houses on
    ##         the given neighborhood and block
    def getBlockModelsForElevations(self,neighborhood,block,elevation):
        return modelCountsBlockElevation(neighborhood,block,elevation)
    
    ##Effects: Returns the nubmer of houses on the block
    def getBlockSize(self,neighborhood,block):
        return blockSize(neighborhood,block)[0][0]


obj = House("A",1,1,[],[],[],[],[])








    