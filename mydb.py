import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'welcome@123',
    auth_plugin = 'mysql_native_password' # Explicitly specify the plugin if needed
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE abinesh")

print("All Done!")

