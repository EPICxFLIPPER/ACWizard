## Handles queries for DELETE requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

##Effects: Deletes the house with neighborhood block and lot numbers
def delete(neighborhood, block, lot,connection):
    try:
        cursor = connection.cursor()
        query = "DELETE FROM Houses WHERE Neighborhood = :neighborhood AND Lot = :lot AND Block = :block"
        cursor.execute(query, {'neighborhood':neighborhood,'block':block,'lot':lot})
        connection.commit()
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()