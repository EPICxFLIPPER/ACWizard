import getpass
import oracledb


pw = getpass.getpass(prompt = 'Input the Password:')  


try:
    connection=oracledb.connect(
     config_dir=r"/opt/oracle/ACWDB",
     user="admin",
     password= pw,
     dsn="lzad5447gxxjj799_tpurgent",
     wallet_location=r"/opt/oracle/ACWDB",
     wallet_password=pw)

except Exception as err:
    print("Error connecting to DB", err)
else:
    print(connection.version)





# Establish the connection

print("here")

