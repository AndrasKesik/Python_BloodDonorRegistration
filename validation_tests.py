# -*- coding: UTF-8 -*-

import unittest
from blood.validation import ValidateName


class ValidateNameTests(unittest.TestCase):
    def test_name_contains_only_letter(self):
        self.assertFalse(ValidateName.validate_name('Joska1'))

    def test_number_of_names(self):
        self.assertFalse(ValidateName.validate_name('Joska'))

    def test_gender(self):
        self.assertTrue(ValidateName.valid_gender("f"))

    def test_email_contains_at(self):
        self.assertFalse(ValidateName.validate_email('jdat.com'))

    def test_email_ending_wrong(self):
        self.assertFalse(ValidateName.validate_email('j@dat.con'), ValidateName.validate_email('j@dat.net'))

    def test_email_ending_right(self):
        self.assertTrue(ValidateName.validate_email('j@dat.com'), ValidateName.validate_email('j@dat.hu'))

    def test_email_not_starts_with_at(self):
        self.assertFalse(ValidateName.validate_email('@dat.com'))


if __name__ == '__main__':
    unittest.validation()
