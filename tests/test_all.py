import unittest
from app.models import Login,Logout,Register

class LoginTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Login class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_login =Login()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_login,Login))


class LogoutTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Logout class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_logout =Logout()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_logout,Logout))

