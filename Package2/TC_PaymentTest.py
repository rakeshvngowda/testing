import unittest

class PaymentTest(unittest.TestCase):
    def paymentInDollar(self):
        print("this is payment in dollar")
        self.assertTrue(True)

    def paymentInRupees(self):
        print("this is payment in Rupees")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()
