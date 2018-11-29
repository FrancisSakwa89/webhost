import unittest
from app.models import Password

class Password(unittest.TestCase):
    '''
    Test Class to test the behaviour of the password class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_password=Password()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_password,Password))