import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
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
def selectSingle(block, lot):
    try:
        connection = getConnection()
        cursor = connection.cursor()
        query = 'SELECT * FROM Houses WHERE Lot = :lot AND Block = :block'
        cursor.execute(query, {'lot': lot, 'block': block})
        results = cursor.fetchall()
        print(results)
        print(len(results))
        return results
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        connection.close()
