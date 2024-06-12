import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
sys.path.append(parent_dir)

from Connection.connection import getConnection


##Effects: Selects all from Houses table
def selectAll():
    try:
        connection = getConnection()
        cursor = connection.cursor()
        
        cursor.execute('SELECT * FROM Houses')
        results = cursor.fetchall()

        print("Number of rows fetched:", len(results))
        cursor.close()
        connection.close()
        
        return results

    except Exception as e:
        print("Error:", e)


##Effects, prints the house at specified block and lot number
def selectSingle(neighborhood, block, lot,connection):
    try:
        cursor = connection.cursor()
        query = 'SELECT * FROM Houses WHERE Neighborhood = :neighborhood AND Lot = :lot AND Block = :block'
        cursor.execute(query, {'neighborhood':neighborhood,'lot': lot, 'block': block})
        results = cursor.fetchall()
        cursor.close()
        return results
    except Exception as e:
        print("Error:", e)


def selectBlock(neighborhood,block,connection):
    try:
        cursor = connection.cursor()
        query = 'SELECT * FROM Houses WHERE Block = :block AND Neighborhood = :neighborhood'
        cursor.execute(query, {'block': block, 'neighborhood' : neighborhood})
        results = cursor.fetchall()
        return results
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()