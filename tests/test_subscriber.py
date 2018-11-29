import unittest
from app.models import Subscriber

class SubscriberTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Subscriber class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_subscriber = Subscriber()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_subscriber,Subscriber))