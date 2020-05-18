import unittest

class LoginTest(unittest.TestCase):
    def loginbyEmail(self):
        print("this is login test by email")
        self.assertTrue(True)

    def loginByFacebook(self):
        print("this is login test by facebook")
        self.assertTrue(True)


    def loginByTwitter(self):
        print("this is login test by Twitter")
        self.assertTrue(True)


if __name__=="__main__":
    unittest.main()
