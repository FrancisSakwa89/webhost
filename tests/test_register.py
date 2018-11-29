import unittest
from app.models import Register

class RegisterTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the register class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_register=Register()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_register,Register))