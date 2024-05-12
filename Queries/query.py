import sys
import os

# Add the parent directory to the Python module search path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# Now import the Connection module
from Connection.connection import getConnection

# Now you can use the Connection class
connection = getConnection()
print(connection.version)