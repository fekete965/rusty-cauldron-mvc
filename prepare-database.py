import os, glob
from sqlite3 import connect, OperationalError

from utils.main import get_database_path 

# Define the path of the database
database_path = get_database_path()
# Connect to our database
connection = connect(database_path)
# Create a cursor
cursor = connection.cursor()

# Define a function which reads a sql file and
def read_and_execute_sql(file_path_and_name: str):
    def filter_helper(cmd: str):
        return len(cmd) != 0 and not cmd.isspace()
    #
    if not file_path_and_name.endswith(".sql"):
        raise Exception(f"{file_path_and_name} is not a SQL file!")
    
    filename = file_path_and_name.split("/")[-1]
    print(f"Opening: {filename}")

    # Open the file
    buffer = open(file_path_and_name, "r")
    # Read the file in memory
    sql_file = buffer.read()
    # Split sql commands into a list if needed and remove spaces and new lines
    sql_commands = list(filter(filter_helper, sql_file.split(";")))
    
    # Iterate on the command list and execute them + raise any errors
    print(f"Running {len(sql_commands)} SQL command(s)")
    for command in sql_commands:
        try:
            cursor.execute(command)
        except OperationalError as msg:
            print(f"Command error: {msg}")
            
    # Close the file
    print(f"Closing: {filename}\n")
    buffer.close()

# Get all migration files
migration_files = os.path.join(os.getcwd(), "migrations", "*.sql")
# Read all SQL files from the migrations folder
for filename in glob.glob(migration_files, recursive=False):
    path_and_name = os.path.join(os.getcwd(), filename)
    read_and_execute_sql(path_and_name)
