import sys
import os
import csv

# Add the parent directory to the Python module search path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# Now import the Connection module
from Connection.connection import getConnection

# Now you can use the Connection class
connection = getConnection()

cursor = connection.cursor()

# open csv
file = open('../data/housedata.csv')

# move to first line past header
csvreader = csv.reader(file, delimiter=',')
query_string = "INSERT INTO Houses (LotJob, TypeDescription, Phase, Block, Lot, Model, Elevation, ExtColour) VALUES (:1, :2, :3, :4, :5, :6, :7, :8)"
next(csvreader)

try:
    # Execute the insert statement
    for row in csvreader:
        if not row:
            continue
        data = []
        data.append((row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
        #print(data)

        cursor.executemany(query_string, data)

    
    connection.commit()
except Exception as e:
    print("Error:", e)

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()