import StatusPlusDB as db
import StatusPlusBot as interface

#used to build requests for the db script from the interface script
class Request:
    def __init__(self) -> None:
        self.pre_requests : list
        self.type : str
        self.table : str

        self.columns : list
        self.values : list

        #used in where queries, assume 'and' modifier between all restrictions for now
        self.restrictions : dict

        self.response : Response


    def set_type(self, type : str) -> None:
        self.type = type

    def get_type(self) -> str:
        return type

    
    def set_table(self, table : str) -> None:
        self.table = table

    def get_table(self) -> str:
        return self.table
    

    def add_pre_requests(self, new_request) -> None:
        self.pre_requests.append(new_request)


    def add_column(self, new_column : str) -> None:
        self.columns.append(new_column)

    def get_columns(self) -> list:
        return self.columns
    
    def add_value(self, new_value : str) -> None:
        self.columns.append(new_value)

    def get_values(self) -> list:
        return self.values
    

    def add_restriction(self, column : str, value : str) -> None:
        self.restrictions[column] = value




#used to build responses for the interface script from the db script
class Response:
    pass



#types of request
#   1. add info
#   2. remove info
#   3. modify info
#   4. get info
#   5. check info

#example request: 'register me'
#   1. identify as add info
#   2. get discord user
#   3. build request
#what request needs in this case:
#   1. that its an add request
#   2. that it relates to users
#   3. the discord user
#   4. the columns affected by addition
#   5. its response
#request anatomy:
#   1. check if user is already registered
#   2. if not then add info request



#example request: 'set relation with *discord user* to *relation type*'
#   1. identify as modify info
#   2. get discord user
#   3. parse message for other user and the relation type
#   4. build request
#what request needs in this case:
#   1. that its a modify request
#   2. that its related to relations
#   3. 
#request anatomy:
#   1. check if user 1 is registered
#   2. check if user 2 is registered
#   3. check if 

#takes a message and builds a request object
def register_request(message):
    pass

#takes a result and builds a response object
def register_response(request, result):
    pass