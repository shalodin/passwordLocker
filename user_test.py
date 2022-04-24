import unittest # Importing the unittest module
from user import User # Importing the User class

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.

        '''
        self.new_user=User("shalodin sigei","shalodin41")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"shalodin sigei")
        self.assertEqual(self.new_user.password,"shalodin41")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    #second Test, to confirm if new user has been saved to the new user list
    def test_save_user(self):
        '''
        test to confirm if new user has been saved to the new user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list))

    #Third test,to check if user details exist
    def test_user_exists(self):
        '''
        test to check if user  exist list
        '''
        self.new_user.save_user()
        check_user=User("shalodin sigei","shalodin41")
        check_user.save_user()
        user_exists=User.user_exist("shalodin sigei","shalodin41")
        self.assertTrue(user_exists)

if __name__ == '__main__':
    unittest.main()

    