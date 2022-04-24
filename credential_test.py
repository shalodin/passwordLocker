import unittest # Importing the unittest module
from credential import Credential # Importing the contact class

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Credential("Facebook", "shalodin sigei", "shalodin41")# create credential object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_account.account_name,"Facebook")
        self.assertEqual(self.new_account.username,"shalodin sigei")
        self.assertEqual(self.new_account.password,"shalodin41")


    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []

    #second Test, to test if account credentials are already saved
    def test_save_account(self):
        '''
        test if new credentials has  been saved to new credential list
        '''
        self.new_account.save_account()
        self.assertEqual(len(Credential.credential_list),1)

    #Third Test, to test if multiple account credentials are saved
    def test_save_multiple_accounts(self):
        '''
        test_save_multiple_account to check if we can save multiple accounts
        objects to our credential_list
        '''
        self.new_account.save_account()
        test_account = Credential("Facebook","shalodin sigei","shalodin41") # new account
        test_account.save_account()
        self.assertEqual(len(Credential.credential_list),2)

    #Fourth Test, test to check if  can find a account by account name and display information
    def test_find_account_by_name(self):
        '''
        test to check if  can find a account by account name 
        '''
        self.new_account.save_account()
        test_account = Credential("Facebook", "shalodin sigei", "shalodin41")  # new account
        test_account.save_account()

        found_account = Credential.find_account_by_name("Facebook")
        self.assertEqual(found_account.username, test_account.username)


    #Fifth Test, to test if we can remove account  credentials
    def test_delete_contact(self):
        '''
        test_delete_account credentials to test if we can remove a credentials from our credential list
        '''
        self.new_account.save_account()
        test_account = Credential("Test","username","password") # new credentials
        test_account.save_account()

        self.new_account.delete_account()# Deleting account credentials
        self.assertEqual(len(Credential.credential_list),1)

    #sixth Test,to test if account exist
    def account_exists(self):
        '''
        test test case to check if account exist
        '''
        self.new_account.save_account()
        check_account=Credential("Facebook","shalodin sigei","shalodin41")
        check_account.save_account()
        account_exists=Credential.account_exist("Facebook","shalodin sigei","shalodin41")
        self.assertTrue(account_exists)

    #seventh Test,to check if it  returns a list of all credentials saved

    def test_display_all_accounts(self):
        '''
        test that returns a list of all credentials saved
        '''

        self.assertEqual(Credential.display_account(),Credential.credential_list)

if __name__ == '__main__':
    unittest.main()