##Handles queries for GET requests
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
sys.path.append(parent_dir)
from Connection.connection import getConnection
from Queries.format import format


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
        
        return format(results)

    except Exception as e:
        print("Error:", e)


##Effects: Queris the single house based on its neighborhood block and lot numbers
def selectSingle(neighborhood, block, lot,connection):
    try:
        cursor = connection.cursor()
        query = 'SELECT * FROM Houses WHERE Neighborhood = :neighborhood AND Lot = :lot AND Block = :block'
        cursor.execute(query, {'neighborhood':neighborhood,'lot': lot, 'block': block})
        results = cursor.fetchall()
        cursor.close()
        formatedResults = format(results)
        return formatedResults
    except Exception as e:
        print("Error:", e)

##Effects: Queries all the hosues on a specific block 
def selectBlock(neighborhood,block,connection):
    try:
        cursor = connection.cursor()
        query = 'SELECT * FROM Houses WHERE Block = :block AND Neighborhood = :neighborhood'
        cursor.execute(query, {'block': block, 'neighborhood' : neighborhood})
        results = cursor.fetchall()
        return format(results)
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()


block = selectBlock("Ryan",100,getConnection())
for b in block:
    print(b)