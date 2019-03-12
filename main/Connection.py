"""
Created on Mar 11, 2019

@author: Noor Peersab
"""

from main.UserDetails import UserDetails
import psycopg2


class Connection(object):
    """
    Connection to the database
    """
    name: str
    database: str
    host: str
    db_name: str
    port: str

    def __init__(self, *, connection_name: str, database: str, host: str, db_name: str, port: str) -> None:
        """
        constructor to create new Connection
        """
        
        self.name = connection_name
        self.database = database
        self.host = host
        self.db_name = db_name
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self, user_details: UserDetails):
        """
        Create connection with database
        """

        url = 'dbname={0} host={1} port={2} user={3} password={4}'.format(
            self.db_name, self.host, self.port, user_details.username, user_details.password)
        self.connection = psycopg2.connect(url)

    def execute_query(self, query: str):
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)
