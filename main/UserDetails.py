"""
Created on Mar 12, 2019

@author: Noor Peersab
"""


class UserDetails(object):
    """
    Store Username and password
    """

    def __init__(self, *, password: str, username: str) -> str:
        """
        Create new user details
        :rtype: None
        :param username: str
        :param password: str
        """

        self.username = username
        self.password = password
