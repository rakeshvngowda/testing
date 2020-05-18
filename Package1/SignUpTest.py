import unittest


class SignUpTest(unittest.TestCase):
    def signUpbyEmail(self):
        print("this is signUp test by email")
        self.assertTrue(True)

    def signUpByFacebook(self):
        print("this is signUp test by facebook")
        self.assertTrue(True)

    def signUpByTwitter(self):
        print("this is signUp test by Twitter")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()

