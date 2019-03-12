from main.Connection import Connection
from main.UserDetails import UserDetails

if __name__ == '__main__':
    user = UserDetails(username='postgres', password='123')
    connection = Connection(
        connection_name='Test', database='postgres', host='localhost', db_name='postgres', port='5432')
    connection.connect(user)
    connection.execute_query('select * from test2')
    pass
