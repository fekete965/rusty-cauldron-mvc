import os, glob
from sqlite3 import connect, OperationalError

from utils.main import getDatabasePath 

# Define the path of the database
databasePath = getDatabasePath()
# Connect to our database
connection = connect(databasePath)
# Create a cursor
cursor = connection.cursor()

# Define a function which reads a sql file and
def readAndExecuteSql(filePathAndName: str):
    def filterHelper(cmd: str):
        return len(cmd) != 0 and not cmd.isspace()
    #
    if not filePathAndName.endswith(".sql"):
        raise Exception(f"{filePathAndName} is not a SQL file!")
    
    filename = filePathAndName.split("/")[-1]
    print(f"Opening: {filename}")

    # Open the file
    buffer = open(filePathAndName, "r")
    # Read the file in memory
    sqlFile = buffer.read()
    # Split sql commands into a list if needed and remove spaces and new lines
    sqlCommands = list(filter(filterHelper, sqlFile.split(";")))
    
    # Iterate on the command list and execute them + raise any errors
    print(f"Running {len(sqlCommands)} SQL command(s)")
    for command in sqlCommands:
        try:
            cursor.execute(command)
        except OperationalError as msg:
            print(f"Command error: {msg}")
            
    # Close the file
    print(f"Closing: {filename}\n")
    buffer.close()

# Get all migration files
migrationFiles = os.path.join(os.getcwd(), "migrations", "*.sql")
# Read all SQL files from the migrations folder
for filename in glob.glob(migrationFiles, recursive=False):
    pathAndName = os.path.join(os.getcwd(), filename)
    readAndExecuteSql(pathAndName)
