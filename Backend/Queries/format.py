##Responsible for formatting the returned data from queries

##Transforms the raw house data into a json array
def format(rawHouseData):
    rows =[]
    for house in rawHouseData:
        house_data = {
                "lotjob": house[0],
                "typedescription": house[1],
                "phase": house[2],
                "block": house[3],
                "lot": house[4],
                "model": house[5],
                "elevation": house[6],
                "extcolour": house[7],
                "neighborhood": house[8],
                "footage": house[9]
            }
        rows.append(house_data)
    return rows