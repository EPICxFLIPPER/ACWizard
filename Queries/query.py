import sys
import os

# Add the parent directory to the Python module search path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# Now import the Connection module
from Connection.connection import getConnection

# Now you can use the Connection class
connection = getConnection()

cursor = connection.cursor()

try:
    # Execute the insert statement

    # Fetch all rows from the Houses table
    cursor.execute('SELECT * FROM Houses')
    results = cursor.fetchall()

    # Print the number of rows fetched
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