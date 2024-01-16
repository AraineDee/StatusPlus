import os
import mysql.connector
from StatusPlusRequest import Request, register_response
from dotenv import load_dotenv

load_dotenv()
MYSQL_USERNAME = os.getenv("MYSQL_USERNAME")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

mydb = mysql.connector.connect(
  host="localhost",
  user=MYSQL_USERNAME,
  password=MYSQL_PASSWORD,
  database=MYSQL_DATABASE
)

mycursor = mydb.cursor()

#   1. get request
#   2. parse request and build query
#   3. execute query
#   4. send response

#types of queries
#   1. Insert value
#   2. Update value
#   3. Select value
#   4. Delete value


#returns the type of query as a string
def identify_query_type(request : Request) -> str:
    pass

#builds and executes an insert query, boolean returns whether query was succesful
def insert_query(request : Request) -> bool:
    sql = "INSERT INTO {} ({}) VALUES ({})"

    table = request.get_table()
    col = request.get_columns()
    val = tuple(request.get_values())
    
    col_formatting = ""
    val_formatting = ""
    for i in range(len(val)):
        if i != 0:
            val_formatting += ", "
            col_formatting += ", "
        val_formatting += "%s"
        col_formatting += col[i]
    
    sql.format(table, col_formatting, val_formatting)
    print(sql)
    print(val)

#builds and executes an update query, boolean returns whether query was succesful
def update_query(request : Request) -> bool:
    pass

#builds and executs a select query, returns result
def select_query(request : Request):
    pass

#builds and executes a delete query, boolean returns whether query was succesful
def delete_query(request : Request) -> bool:
    pass

#accepts request, uses request to build and execute query, and then sends a response back
def execute_request(request):
    type = identify_query_type(request)
    result = None

    if type == "INSERT":
        result = insert_query(request)
    elif type == "UPDATE":
        result = update_query(request)
    elif type == "SELECT":
        result = select_query(request)
    elif type == "DELETE":
        result = delete_query(request)
    else:
        raise Exception("Query Type was not what was expected. Query Type: " + type)
    
    register_response(request, result)



if __name__ == "__main__":
    pass