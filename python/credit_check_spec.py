# Can you translate this driver code to unit tests?

from credit_check import credit_check

# print(credit_check('5541808923795240') == "The number is valid!")
# print(credit_check("4024007136512380") == "The number is valid!")
# print(credit_check("6011797668867828") == "The number is valid!")

# print(credit_check("5541801923795240") == "The number is invalid!")
# print(credit_check("4024007106512380") == "The number is invalid!")
# print(credit_check("6011797668868728") == "The number is invalid!")

import unittest
class TestCredit(unittest.TestCase):

    def test_valid_credit(self):
        self.assertEqual(credit_check('5541808923795240'), "The number is valid!")
        self.assertEqual(credit_check("4024007136512380"), "The number is valid!")
        self.assertEqual(credit_check("6011797668867828"), "The number is valid!")
    
    def test_unvalid_credit(self):
        self.assertEqual(credit_check("5541801923795240"), "The number is invalid!")
        self.assertEqual(credit_check("4024007106512380"), "The number is invalid!")
        self.assertEqual(credit_check("6011797668868728"), "The number is invalid!")
  
if __name__ == '__main__':
    unittest.main()

