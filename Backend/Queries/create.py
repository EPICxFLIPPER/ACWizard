import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Backend.Connection.connection import getConnection
from Backend.Queries.read import selectSingle

##Effects: Creats a new house with the given neigborhood, block and lot
def create(neighborhood, block, lot, connection):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO Houses (neighborhood, block, lot) VALUES (:neighborhood, :block , :lot)"
        cursor.execute(query, {'neighborhood':neighborhood,'lot': lot, 'block': block})
        connection.commit()
        ret = cursor.lastrowid
    except Exception as e:
        print("Error:", e)
        print("HERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
    finally:
        cursor.close()
        return ret