##Handles specific queries needed for house logic
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
sys.path.append(parent_dir)
from Connection.connection import getConnection

        
##Effects: Queries the database and retuns the counts of each model for a specific block and elevation
def modelCountsBlockElevation(neighborhood, block,elevation,connection):
    try:
        cursor = connection.cursor()
        query = 'SELECT Model, Count(*) FROM Houses WHERE Block = :block AND Neighborhood = :neighborhood AND Elevation = :elevation GROUP BY Model'
        cursor.execute(query, {'block': block, 'neighborhood' : neighborhood, 'elevation' : elevation})
        results = cursor.fetchall()
        print(results)
        print(len(results))
        return results
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()

##Effects: Queries the database and retuns the size of the specific block in the neigbohood
def blockSize(neighborhood, block,connection):
    try:
        cursor = connection.cursor()
        query = 'SELECT Count(*) FROM Houses WHERE Block = :block AND Neighborhood = :neighborhood'
        cursor.execute(query, {'block': block, 'neighborhood' : neighborhood})
        results = cursor.fetchall()
        print(results)
        print(len(results))
        return results
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()



