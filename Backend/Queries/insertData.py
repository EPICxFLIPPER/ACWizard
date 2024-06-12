##Handles the insertion of new data
import sys
import os
import csv
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from Connection.connection import getConnection

##Effects: Handles the insertion of new data
##       -fileLocation - String that is the location of the csv file to be inserted
def insertData(fileLocaiton):

    connection = getConnection()
    cursor = connection.cursor()

    file = open(fileLocaiton)

    csvreader = csv.reader(file, delimiter=',')
    query_string = "INSERT INTO Houses (LotJob, TypeDescription, Phase, Block, Lot, Model, Elevation, ExtColour, Neighborhood, Footage) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10)"
    next(csvreader)

    try:
        # Execute the insert statement
        for row in csvreader:
            if not row:
                continue
            data = []
            first,second = row[1].split(" - ")
            data.append((row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],first,second))
            #print(data)

            cursor.executemany(query_string, data)

        connection.commit()
    except Exception as e:
        print("Error:", e)
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()
