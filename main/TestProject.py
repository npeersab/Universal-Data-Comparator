'''
Created on Mar 11, 2019

@author: Noor Peersab
'''


class TestProject(object):
    '''
    Contains all details about Test Project
    '''

    def __init__(self, project_name):
        '''
        Create new Test Project with name
        '''
        
        self.name = project_name
        self.connections = []
        self.test_cases = []
        
    def add_connection(self, connection):
        '''
        Add new Connection to the Test Project
        '''
        
        self.connections.append(connection)
        
    def add_test_case(self, test_case):
        '''
        Add new Test Case in the Test Project
        '''
        
        self.test_cases.append(test_case)
        
    