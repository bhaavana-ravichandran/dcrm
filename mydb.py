import mysql.connector

cursorObject = None  # Initialize cursorObject as None

try:
    # Establishing the connection
    database = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='Bhaavana@29',
        auth_plugin='mysql_native_password'  # Use mysql_native_password to avoid plugin issue
    )

    # Prepare cursor object
    cursorObject = database.cursor()

    # Create a database
    cursorObject.execute("CREATE DATABASE IF NOT EXISTS bhaavana")

    print("Database 'bhaavana' created successfully.")

except mysql.connector.Error as err:
    # Handle any MySQL specific errors
    print(f"Error: {err}")

finally:
    # Ensure that cursorObject and database connection are closed if they were successfully created
    if cursorObject:
        cursorObject.close()
    if database:
        database.close()