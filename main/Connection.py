"""
Created on Mar 11, 2019

@author: Noor Peersab
"""


class Connection(object):
    """
    Connection to the database
    """

    def __init__(self, connection_name, database, host, db_name, port):
        """
        constructor to create new Connection
        """
        
        self.name = connection_name
        self.database = database
        self.host = host
        self.db_name = db_name
        self.port = port
