'''
Created on Mar 11, 2019

@author: Noor Peersab
'''

class Connection(object):
    '''
    Connection to the database
    '''


    def __init__(self, connection_name, database, host, dbname, port):
        '''
        constructor to create new Connection
        '''
        
        self.name = connection_name
        self.database = database
        self.host = host
        self.dbname = dbname,
        self.port = port    
    