##Handles the creation of the connection to the oracle database

import oracledb
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
sys.path.append(parent_dir)
import Connection.config


    
##Effects: Establishes and returns the connection to the Oracle Database
def getConnection():

    connection_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

    try:
        connection=oracledb.connect(
        config_dir=connection_dir + r"/conn",
        user="admin",
        password= Connection.config.password,
        dsn="wizarddb_tpurgent",
        wallet_location=connection_dir + r"/conn",
        wallet_password=Connection.config.password)

    except Exception as err:
        print("Error connecting to DB", err)
    else:
        print("Connected Sucessfully, version: ",connection.version)
        return connection










