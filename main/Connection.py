'''
Created on Mar 11, 2019

@author: Noor Peersab
'''

class Connection(object):
    '''
    classdocs
    '''


    def __init__(self, connection_name, database, host, dbname, port):
        '''
        Constructor
        '''
        
        self.name = connection_name
        self.database = database
        self.host = host
        self.dbname = dbname,
        self.port = port
    
    def set_username(self, username):
        
        self.username = username
        
    def set_password(self, password):
        self.password = password
        
        
    