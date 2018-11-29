import unittest
from app.models import Get_comment

class Get_commentTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Get_comment class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_get_comment=Get_comment()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_get_comment,Get_comment))