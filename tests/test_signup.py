import unittest
from app.models import Signup

class SignupTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Signup class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_signup = Signup()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_signup,Signup))