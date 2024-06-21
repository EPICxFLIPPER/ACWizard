## Defines the Arcitectural control logic for houses as well as the creation of house objects
import sys
import os
import copy
import threading
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from House.exceptions import *
from Queries.query import *
from Queries.read import selectSingle
from Queries.read import selectBlock
from Connection.connection import getConnection
from Threads.retThread import RetThread
import json
## A House object with realtional information to the the houses around it, and methods to handle arcitectrual controls
class House:

    connection = None

    elevationToColorDict = {'CL' : ['CL - 1.1', 'CL - 2.1', 'CL - 3.1', 'CL - 4.1','CL - 5.1','CL - 6.1','CL - 7.1','CL - 8.1','CL - 9.1','CL - 10.1'],
                        'CR' : ['CR - 1.1', 'CR - 2.1', 'CR - 3.1', 'CR - 4.1','CR - 5.1','CR - 6.1','CR - 7.1','CR - 8.1','CR - 9.1','CR - 10.1'],
                        'PR' : ['PR - 1.1', 'PR - 2.1', 'PR - 3.1', 'PR - 4.1','PR - 5.1','PR - 6.1','PR - 7.1','PR - 8.1','PR - 9.1','PR - 10.1']}

    footageToModels = {'44 ft\'s' : ['Armstrong','Bishop','Borgeua','Cline','Maclaren','Ptarmigan','Rutherford','Smythe','Bishop 2.0','Aberdeen','Rundle','Bluebell'],
                    '36 ft\'s' : ['Cypress','Fairview','Fullerton','Monarch','Whistler','Yamnuska','Norquay'],
                    '24 ft\'s' : ['Waputik','Palliser','Sundance','Finch','Cardinal','Starling']}

    elevationDict = {
            "" : 0,
            "CL": 0,
            "CR": 0,
            "PR": 0
        }

    ##Constructor, initilizes across, left, right, corner to be empty
    ## neighborhood - String
    ## block - int
    ## lot - int
    ## across - Array of Tuple
    ## left - Array of Tuple size 2, index 0 is two to left, index 1 is directly left
    ## right - Array of Tuple size 2, index 0 is directly right, index 1 is two to the right
    ## corner - Array of Tuple
    ## pari - the house that is a pair of this if it is a town house
    ## Tuples consist of (neighborhood,block,lot) of reatlional houses
    def __init__(self,neighborhood,block,lot,across,left,right,corner,pair):
        self.neighborhood = neighborhood
        self.block = block
        self.lot = lot
        self.across = across
        self.left = left
        self.right = right
        self.corner = corner
        self.pair = pair
        
            
    ##Effects: Returns a tuple of house identifiers (neighborhood, block, lot)
    def getID(self):
        temp = []
        temp.append(self.neighborhood)
        temp.append(self.block)
        temp.append(self.lot)
        return temp
    
    ##Effects: Appends the house identifier to the end of the across list
    def insertAcross(self,house):
        self.across.append(house)

    ##Effects: Appends the house identifier to the end of the left list
    ##         Order of insertions matters, list should be size 2
    def insertLeft(self,house,position):
        if (position >=0 and position <= 2):
            self.left[position] = house

    ##Effects: Appends the house identifier to the end of the right list
    ##         Order of insertions matters, list should be size 2
    def insertRight(self,house,position):
        if (position >=0 and position <= 2):
            self.right[position] = house

    ##Effects: Appends the house identifier to the end of the corner list
    def insertCorner(self,house):
        self.corner.append(house)

    ##Effects: Returns a list of all colours this house can be,
    ##         If this house does not yet have a elevation, returns []
    ##         If this house does not have a vailid elevation, throws invalid elevation exception
    def colours(self,tempElevation = None, connection = None):
        id = self.getID()
        if (connection is None):
            connection = getConnection()

        if (tempElevation is not None):
            elevation = tempElevation
        else:
            elevation = self.getElevation(id[0],id[1],id[2],connection)
        if (elevation == "PR" or elevation == "CR" or elevation == "CL"):
            return self.getColorsForElevation(copy.deepcopy(self.elevationToColorDict[elevation]),connection)
        elif (elevation is None or elevation == " " or elevation == ""):
            return []
        else:
            raise InvalidElevationException(elevation)
    
    ## EFFECTS: returns a list of all the possible colors a house can be based on the list of possiblities
    def getColorsForElevation(self,possibleColors,connection):
        colors = []
        threads = []

        if (len(self.left) > 1 and self.left[1] is not None):
            t = RetThread(target = self.getColor, args=(self.left[1][0],self.left[1][1],self.left[1][2],connection))
            t.start()
            threads.append(t)
        if (len(self.left) >= 1 and self.left[0] is not None):
            t = RetThread(target = self.getColor, args=(self.left[0][0],self.left[0][1],self.left[0][2],connection))
            t.start()
            threads.append(t)
        if (len(self.right) >= 1 and self.right[0] is not None):
            t = RetThread(target = self.getColor, args=(self.right[0][0],self.right[0][1],self.right[0][2],connection))
            t.start()
            threads.append(t)
        if (len(self.right) > 1 and self.right[1] is not None):
            t = RetThread(target = self.getColor, args=(self.right[1][0],self.right[1][1],self.right[1][2],connection))
            t.start()
            threads.append(t)

        for cross in self.across:
            t = RetThread(target = self.getColor, args=(cross[0],cross[1],cross[2],connection))
            t.start()
            threads.append(t)

        for t in threads:
            colors.append(t.join())
            
        for c in colors:
            try:
                possibleColors.remove(c)
            except ValueError as e:
                pass 

        return possibleColors
        
    ##Effects: Returns a list of all models this house can be, Throws InvalidFootageException if this house does not have valid Footage
    def models(self,tempElevation = None, connection = None):
        id = self.getID()
        if (connection is None):
            connection = getConnection()

        footage = self.getFootage(id[0],id[1],id[2],connection)
        if (footage == '44 ft\'s' or footage ==  '36 ft\'s' or footage ==  '24 ft\'s'):
            return self.modelsForSize(copy.deepcopy(self.footageToModels[footage]), tempElevation,connection)
        else:
            raise InvalidFootageException(footage)

    ##Effects: Returns all the models that this house can be by elimatating models from the possible starting models.    
    def modelsForSize(self,possibleModels,tempElevation,connection):
        id = self.getID()
        if (tempElevation is not None):
            elevation = tempElevation
        else:
            elevation = self.getElevation(id[0],id[1],id[2],connection)

        if (elevation != None and elevation != " " and elevation != ""):
            ##This house does have en elevation
            
            modelThreads = []
            elevationThreads = []
            toRemove = []

            threeThread = RetThread(target = self.ModelsThreeInRow, args=(connection,))
            threeThread.start()
            
            

            ##Two away / corner Rule
            effectsMod = []
            if (len(self.left) > 1 and self.left[1] is not None):
                effectsMod.append(self.left[1])
            if (len(self.left) >= 1 and self.left[0] is not None):
                effectsMod.append(self.left[0])
            if (len(self.right) >= 1 and self.right[0] is not None):
                effectsMod.append(self.right[0])
            if (len(self.right) > 1 and self.right[1] is not None):
                effectsMod.append(self.right[1])
       
            for h in self.corner:
                effectsMod.append(h)

            for h in effectsMod:
                tm = RetThread(target = self.getModel, args=(h[0],h[1],h[2],connection))
                tm.start()
                te = RetThread(target= self.getElevation, args=(h[0],h[1],h[2],connection))
                te.start()
                modelThreads.append(tm)
                elevationThreads.append(te)

            for index in range(len(modelThreads)):
                mod = modelThreads[index].join()
                ele = elevationThreads[index].join()
                if (ele == elevation):
                    toRemove.append(mod)

            ## 30% Rule
            modelCounts = self.getBlockModelsForElevations(id[0],id[1],elevation,connection)
            blocksize = self.getBlockSize(id[0],id[1],connection)
            cutoff = blocksize/3

            ##Possible need for delta when dividing
            for p in modelCounts:
                if (p[1] + 1 > cutoff):
                    toRemove.append(p[0])

            toRemove.extend(threeThread.join())
            for r in toRemove:
                try:
                    possibleModels.remove(r)
                except ValueError as e:
                    pass 



            return possibleModels
        
    ##Effects: Retuns a list of all the modles this house can not be via the 3 in row rule    
    def ModelsThreeInRow(self,connection):
        oneLeftModel = None
        twoLeftModel = None
        oneRightModel = None
        twoRightModel = None
        oneLeftBool = 0
        twoLeftBool = 0
        oneRightBool = 0
        twoRightBool = 0
        threads = [None,None,None,None]
        notModels = []

        if (len(self.left) > 1 and self.left[1] is not None):
            oneLeftBool = 1
            t = RetThread(target = self.getModel, args=(self.left[1][0],self.left[1][1],self.left[1][2],connection))
            t.start()
            threads[0] = t
        if (len(self.left) >= 1 and self.left[0] is not None):
            twoLeftBool = 1
            t = RetThread(target = self.getModel, args=(self.left[0][0],self.left[0][1],self.left[0][2],connection))
            t.start()
            threads[1] = t 
        if (len(self.right) >= 1 and self.right[0] is not None):
            oneRightBool = 1
            t = RetThread(target = self.getModel, args=(self.right[0][0],self.right[0][1],self.right[0][2],connection))
            t.start()
            threads[2] = t
        if (len(self.right) > 1 and self.right[1] is not None):
            twoRightBool = 1
            t = RetThread(target = self.getModel, args=(self.right[1][0],self.right[1][1],self.right[1][2],connection))
            t.start()
            threads[3] = t

        if (oneLeftBool):
            oneLeftModel = threads[0].join()
        if (twoLeftBool):
            oneRightModel = threads[1].join()
        if (oneRightBool):
            oneRightModel = threads[2].join()
        if (twoRightBool):
            oneRightModel = threads[3].join()
        
        if (oneLeftModel == twoLeftModel and (oneLeftModel is not None) and (twoLeftModel is not None)):
            notModels.append(oneLeftModel)
        if (oneLeftModel == oneRightModel and (oneLeftModel is not None) and (oneRightModel is not None)):
            notModels.append(oneLeftModel)
        if (oneRightModel == twoRightModel and (oneRightModel is not None) and (twoRightModel is not None)):
            notModels.append(twoRightModel)

        return notModels
            
    ##Effects: Returns a list of all elevations this house can be
    def elevations(house, tempModel = None, connection = None):
        elevationList = ["CR","PR","CL"]
        lock = threading.Lock()

        if (connection is None):
            connection = getConnection()

        def checkCorner(tempModel = None):
            curHouse = house.getID()

            if (tempModel is not None):
                houseModel = tempModel
            else:
                houseModel = house.getModel(curHouse[0], curHouse[1], curHouse[2],connection)
            
            if (houseModel is not None and houseModel != ""):
                for cornerHouse in house.corner:
                    cornerHouseElevation = house.getElevation(cornerHouse[0], cornerHouse[1], cornerHouse[2],connection)
                    cornerHouseModel = house.getModel(cornerHouse[0], cornerHouse[1], cornerHouse[2],connection)
                    lock.acquire()
                    if (cornerHouseElevation is not None and cornerHouseElevation in elevationList and cornerHouseModel == houseModel):
                        elevationList.remove(cornerHouseElevation)
                    lock.release()

                

        
        def alternatingElevation(tempModel = None):
            # get characteristics of left house
            if len(house.left) == 0:
                leftHouseModel = ""
                leftHouseElevation = ""
                leftHouse = None
            else:
                leftHouse = house.left[1]
                if leftHouse is not None:
                    leftHouseModel = house.getModel(leftHouse[0], leftHouse[1], leftHouse[2],connection)
                    leftHouseElevation = house.getElevation(leftHouse[0], leftHouse[1], leftHouse[2],connection)

            # get characteristics of right house
            if len(house.right) == 0:
                rightHouseModel = ""
                rightHouseElevation = ""
                rightHouse = None
            else: 
                rightHouse = house.right[0]
                if rightHouse is not None:
                    rightHouseModel = house.getModel(rightHouse[0], rightHouse[1], rightHouse[2],connection)
                    rightHouseElevation = house.getElevation(rightHouse[0], rightHouse[1], rightHouse[2],connection)

            # get characteristics of current house
            curHouse = house.getID()

            if (tempModel is not None):
                houseModel = tempModel
            else:
                houseModel = house.getModel(curHouse[0], curHouse[1], curHouse[2],connection)

            # if the model is the same, elevation must be alternating
            if houseModel is not None:
                if rightHouse is not None and rightHouseModel is not None:
                    if rightHouseModel == houseModel:
                        lock.acquire()
                        if rightHouseElevation is not None and rightHouseElevation in elevationList:
                            elevationList.remove(rightHouseElevation)
                        lock.release()
                if leftHouse is not None and leftHouseModel is not None:
                    if leftHouseModel == houseModel:
                        lock.acquire()
                        if leftHouseElevation is not None and leftHouseElevation in elevationList:
                            elevationList.remove(leftHouseElevation)
                        lock.release()

        def acrossElevation():
            # check across houses: directly across, left one of direct, right one of direct
            threads = []
            for cross in house.across:
                t = RetThread(target=house.getElevation, args = (cross[0], cross[1], cross[2],connection))
                t.start()
                threads.append(t)

            for t in threads:
                neighbourElevation = t.join()
                if neighbourElevation is not None:
                    lock.acquire()
                    if neighbourElevation in elevationList:
                        elevationList.remove(neighbourElevation)
                    lock.release()

        def maxThree(tempModel = None):
            possibleElevations = house.elevationDict
            houseArray = house.getID()
            if (tempModel is not None):
                houseModel = tempModel
            else:
                houseModel = house.getModel(houseArray[0], houseArray[1], houseArray[2],connection)
            houseBlock = selectBlock(house.neighborhood,house.block,connection)
            # loops through houses on the block
            for neighbour in houseBlock:
                print("neighborr:", neighbour)
                elevation = neighbour['elevation']
                model = neighbour['model']
                # increment elevation count of block
                if model is not None:
                    if model == houseModel:
                        if elevation is not None:
                            possibleElevations[elevation] += 1
            for elevation in possibleElevations:
                if possibleElevations[elevation]/len(houseBlock) >= 0.3:
                    lock.acquire()
                    if elevation in elevationList:
                        elevationList.remove(elevation)
                    lock.release()
                # reset counts
                possibleElevations[elevation] = 0

        
        def twoApart(tempModel = None):
            possibleElevations = house.elevationDict
            houseArray = house.getID()
            if (tempModel is not None):
                houseModel = tempModel
            else:
                houseModel = house.getModel(houseArray[0], houseArray[1], houseArray[2],connection)
            houseElevation = house.getElevation(houseArray[0], houseArray[1], houseArray[2],connection)

            # loop through left Neighbours
            for leftNeighbour in house.left:
                if leftNeighbour is not None:
                    elevation = house.getElevation(leftNeighbour[0], leftNeighbour[1], leftNeighbour[2],connection)
                    model = house.getModel(leftNeighbour[0], leftNeighbour[1], leftNeighbour[2],connection)
                    if model == houseModel:
                        possibleElevations[elevation] += 1

            # loop through right Neighbours
            for rightNeighbour in house.right:
                if rightNeighbour is not None:
                    elevation = house.getElevation(rightNeighbour[0], rightNeighbour[1], rightNeighbour[2],connection)
                    model = house.getModel(rightNeighbour[0], rightNeighbour[1], rightNeighbour[2],connection)
                    if model == houseModel:
                        possibleElevations[elevation] += 1

            # loop through elevation dictionary
            for elevation in possibleElevations:
                # if no neighbours within 2 houses have elevation, it is valid: add it to the list
                if possibleElevations[elevation] != 0:
                    if elevation != '':
                        lock.acquire()
                        try:
                            elevationList.remove(elevation)
                        except ValueError as e:
                            pass
                        lock.release()
                # reset elevation count
                possibleElevations[elevation] = 0

            # return list of valid elevations
        
        print(tempModel, "Temp model in models is")
        if (tempModel == ""):
            print("empty")
        if (tempModel == None):
            print("none")
        if (tempModel is not None):
            
            threads = [
                RetThread(target=twoApart, args=(tempModel,)),
                RetThread(target=maxThree, args=(tempModel,)),
                RetThread(target=acrossElevation),
                RetThread(target=alternatingElevation, args=(tempModel,)),
                RetThread(target=checkCorner, args=(tempModel,)) ]
        else:
            threads = [
                RetThread(target=twoApart),
                RetThread(target=maxThree),
                RetThread(target=acrossElevation),
                RetThread(target=alternatingElevation),
                RetThread(target=checkCorner) ]
        
        for t in threads:
            t.start()

        for t in threads:
            t.join()

        return elevationList



        

    ##Effects: Queries the database and retruns the color of the house with 
            ##Provided neighborhood, block, lot numbers
            ##If the house does not exist, returns ""
    def getColor(self,neighborhood,block,lot,connection):
        result = selectSingle(neighborhood,block,lot,connection)
        if (len(result) == 0):
            return ""
        else:
            return result[0]['extcolour']
        
        
     ##Effects: Queries the database and retruns the color of the house with 
            ##Provided neighborhood, block, lot numbers
            ##If the house does not exist, returns ""
  
    ##Effects: Queries the database and returns the model of the house with the provided identifier
    ##         If the house does not exist returns ""
    def getModel(self,neighborhood,block,lot,connection):
        result = selectSingle(neighborhood,block,lot,connection)
        if (len(result) == 0):
            return ""
        else:
            return result[0]['model']


     ##Effects: Queries the database and retruns the color of the house with 
            ##Provided neighborhood, block, lot numbers
            ##If the house does not exist, returns ""
 
    ##Effects: Queries the database and returns the elevation of the house with the provided identifier
    ##         If the house does not exist returns ""
    def getElevation(self,neighborhood,block,lot,connection):
        result = selectSingle(neighborhood,block,lot,connection)
        if (len(result) == 0):
            return ""
        else:
            return result[0]['elevation']
    
    ##Effects: Returns the footage value fo the given house
    def getFootage(self,neighborhood,block,lot,connection):
        result = selectSingle(neighborhood,block,lot, connection)
        if (len(result) == 0):
            return ""
        else:
            return result[0]['footage']
        
    ##Effects: Returns an array of all the models and elevation pairs for houses on
    ##         the given neighborhood and block
    def getBlockModelsForElevations(self,neighborhood,block,elevation,connection):
        return modelCountsBlockElevation(neighborhood,block,elevation,connection)
    
    ##Effects: Returns the nubmer of houses on the block
    def getBlockSize(self,neighborhood,block,connection):
        return blockSize(neighborhood,block,connection)[0][0]

    def toDict(self):
        return {
            'neighborhood': self.neighborhood,
            'block': self.block,
            'lot': self.lot,
            'across': self.across,
            'left': self.left,
            'right': self.right,
            'corner': self.corner,
            'pair': self.pair,
        }
    @classmethod
    def fromDict(cls,data):
        return cls(data['neighborhood'],data['block'],data['lot'],data['across'],data['left'],data['right'],data['corner'],data['pair'])
    
    ##Effects: Returns true if this house can be the given model elevation and colour
    def canBeSpecifics(self,neighborhood, block, lot, model,elevation,colour):
        conn = getConnection()
        if (model == ""):
            Newmodel = None
        else:
            Newmodel = model
        if (elevation == ""):
            Newelevation = None
        else:
            Newelevation = elevation

        print(Newmodel, "The new model in can Be Specifics")
        possibleModels = self.models(tempElevation=Newelevation,connection = conn)
        possibleElevations = self.elevations(tempModel=Newmodel,connection = conn)
        possibleColours = self.colours(tempElevation=Newelevation,connection = conn)

        if ((model in possibleModels or model == "") and (elevation in possibleElevations or elevation == "") and (colour in possibleColours or colour == "")):
            return {'neighborhood': neighborhood,
                    'block': block,
                    'lot': lot}
        else:
            return None




# n = "TestNode"
# oneOne = (n,1,1)
# twoOne = (n,2,1)
# twoTwo = (n,2,2)
# twoThree = (n,2,3)
# twoFour = (n,2,4)
# threeOne = (n,3,1)
# fourOne = (n,4,1)
# fourTwo = (n,4,2)
# fourThree = (n,4,3)
# fourFour = (n,4,4)
# fourFive = (n,4,5)
# fourSix = (n,4,6)

# ## (self,neighborhood,block,lot,across,left,right,corner,pair):

# oneOneH = House(n,1,1,[],[None,None],[None,None],[twoOne,threeOne,fourOne],[])
# twoOneH = House(n,2,1,[fourTwo],[None,None],[twoTwo,twoThree],[oneOne,threeOne,fourOne],[])
# twoTwoH = House(n,2,2,[fourOne,fourTwo,fourThree],[None,twoOne],[twoThree,twoFour],[],[])
# twoThreeH = House(n,2,3,[fourTwo,fourThree,fourFour],[twoOne,twoTwo],[twoFour,None],[],[])
# twoFourH = House(n,2,4,[fourThree,fourFour,fourFive],[twoTwo,twoThree],[None,None],[],[])
# threeOneH = House(n,3,1,[],[None,None],[None,None],[oneOne,twoOne,fourOne],[])
# fourOneH = House(n,4,1,[twoTwo],[None,None],[fourTwo,fourThree],[oneOne,twoOne,threeOne],[])
# fourTwoH = House(n,4,2,[twoOne,twoTwo,twoThree],[None,fourOne],[fourThree,fourFour],[],[])
# fourThreeH = House(n,4,3,[twoTwo,twoThree,twoFour],[fourOne,fourTwo],[fourFour,fourFive],[],[])
# fourFourH = House(n,4,4,[twoThree,twoFour],[fourTwo,fourThree],[fourFive,fourSix],[],[])
# fourFiveH = House(n,4,5,[twoFour],[fourThree,fourFour],[fourSix,None],[],[])
# fourSixH = House(n,4,6,[],[fourFour,fourFive],[None,None],[],[])

# houses = [oneOneH,twoOneH,twoTwoH,twoThreeH,twoFourH,threeOneH,fourOneH,fourTwoH,fourThreeH,fourFourH,fourFiveH,fourSixH]

# dictionaires = [h.toDict() for h in houses]

# json_data = json.dumps(dictionaires)
# print(json_data)
# with open('../Data/houses.json', 'w') as file:
#     file.write(json_data)

# with open('../Data/houses.json', 'r') as file:
#     data = json.load(file)

# print(data)

# for d in data:
#     ret = House.fromDict(d)
#     print(ret.neighborhood)
