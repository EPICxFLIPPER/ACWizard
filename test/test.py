import getpass
import oracledb
import os



# pw = getpass.getpass(prompt = 'Input the Password:')  
pw = "Liam/Ryan9904"

##connection_directory = os.path.join(current_directory, '..', 'Connection')
connection_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Connection'))
##config_file_path = os.path.join(current_directory, 'Connection')
print(connection_dir)

try:
    connection=oracledb.connect(
     config_dir=r"/conn",
     user="admin",
     password= pw,
     dsn="wizarddb_tpurgent",
     wallet_location=r"/conn",
     wallet_password=pw)

except Exception as err:
    print("Error connecting to DB", err)
else:
    print(connection.version)









