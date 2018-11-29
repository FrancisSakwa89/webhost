import unittest
from app.models import Get_comment,Delete_comment,Update_post

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

class Delete_commentTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the DElete_comment class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_delete_comment=Delete_comment()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_delete_comment,Delete_comment))

class Update_postTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Update_comment class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_update_post=Update_post()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_update_post,Update_post))