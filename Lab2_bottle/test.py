import unittest
from myform import mail_valid

class TestEmailValidation(unittest.TestCase):
    
    def test_valid_email(self):
        list_mail_cor = ["m.m@mail.ru", "m1@gmail.com", "m-123@ya.ru", "a@b.co.uk", "a.b.c@mail.ru"]
        for mail in list_mail_cor:
            self.assertTrue(mail_valid(mail))

    def test_invalid_email(self):
        list_mail_uncor = ["", "1", "m1@", "@mail", "m@mail.", "m@mail..ru", "m@mail", "m@@mail.ru", 
                           "m@mail.ru.", "m@.mail.ru", "m@mail..com", "m@@mail.ru", "a@b.co..uk"]
        for mail in list_mail_uncor:
            self.assertFalse(mail_valid(mail))

if __name__ == '__main__':
    unittest.main()