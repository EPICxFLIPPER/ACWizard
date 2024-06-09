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

        # Print the fetched rows
        for row in results:
            print(row)

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

##Effects, prints the house at specified block and lot number
def selectSingle(neighborhood, block, lot,connection):
    try:
        cursor = connection.cursor()
        query = 'SELECT * FROM Houses WHERE Neighborhood = :neighborhood AND Lot = :lot AND Block = :block'
        cursor.execute(query, {'neighborhood':neighborhood,'lot': lot, 'block': block})
        results = cursor.fetchall()
        return results
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()


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


selectAll()
