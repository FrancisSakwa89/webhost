import unittest
from app.models import View_comment

class View_commentTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the View_comment class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_view_comment=View_comment()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_view_comment,View_comment))