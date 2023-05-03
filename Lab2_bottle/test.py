import unittest
from myform import mail_valid

class TestEmailValidation(unittest.TestCase):
    
    def test_valid_email(self):
        valid_email = 'test.email@gmail.com'
        self.assertTrue(mail_valid(valid_email))

    def test_invalid_email(self):
        invalid_email = 'test.email'
        self.assertFalse(mail_valid(invalid_email))

if __name__ == '__main__':
    unittest.main()