##Handles Queries for PUT requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Backend.Connection.connection import getConnection
from Backend.Queries.read import selectSingle

##Effects: Updates the house with neighborhood, block, lot with the given model, elevation, color
def update(neighborhood, block, lot, model, elevation, colour,connection = None):
    try:
        if (connection is None):
            connection = getConnection()
        cursor = connection.cursor()
        query = "UPDATE Houses SET Model = :model, Elevation = :elevation, Extcolour = :colour WHERE Neighborhood = :neighborhood AND Lot = :lot AND Block = :block"
        cursor.execute(query, {'model':model,'elevation':elevation,'colour':colour,'neighborhood':neighborhood,'lot': lot, 'block': block})
        connection.commit()
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()