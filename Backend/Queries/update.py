import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Backend.Connection.connection import getConnection

##Effects: Updates the house with neighborhood, block, lot with the given model, elevation, color
##TODO     If model elevation or colors is not given, then do not update that value
def update(neighborhood, block, lot, model, elevation, colour,connection):
    try:
        cursor = connection.cursor()
        query = "UPDATE Houses SET Model = :model, Elevation = :elevation, Extcolour = :colour WHERE Neighborhood = :neighborhood AND Lot = :lot AND Block = :block"
        cursor.execute(query, {'model':model,'elevation':elevation,'colour':colour,'neighborhood':neighborhood,'lot': lot, 'block': block})
        connection.commit()
    except Exception as e:

        print("Error:", e)
    finally:
        # Close the cursor and connection
        cursor.close()