from server.db_utils import *

def rebuild(){
    exec_sql_file('schema.sql')
    exec_sql_file('data.sql')
}