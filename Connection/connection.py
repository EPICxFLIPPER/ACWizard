import getpass
import oracledb
import os


    
    ##Effects: Returns the connection to the Oracle Database
def getConnection():

    pw = getpass.getpass(prompt = 'Input the Password:')  

    connection_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    print(connection_dir)

    try:
        connection=oracledb.connect(
        config_dir=connection_dir + r"/conn",
        user="admin",
        password= pw,
        dsn="wizarddb_tpurgent",
        wallet_location=connection_dir + r"/conn",
        wallet_password=pw)

    except Exception as err:
        print("Error connecting to DB", err)
    else:
        print(connection.version)
        return connection









