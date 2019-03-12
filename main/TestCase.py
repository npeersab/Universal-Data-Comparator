"""
Created on Mar 12, 2019

@author: Noor Peersab
"""


class TestCase(object):
    """
    Test Case
    """

    def __init__(self, *, test_case_name, source_connection, source_query, target_connection, target_query):
        """
        Constructor
        """
        self.test_case_name = test_case_name
        self.source_connection = source_connection
        self.source_query = source_query
        self.target_connection = target_connection
        self.target_query = target_query

    def execute(self):
        """
        Execute the Test Case
        """
        pass
