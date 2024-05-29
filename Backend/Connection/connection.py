import oracledb
import os
import Connection.config


    
    ##Effects: Returns the connection to the Oracle Database
def getConnection():

    connection_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    print(connection_dir)

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
        print(connection.version)
        return connection









