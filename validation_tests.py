# -*- coding: UTF-8 -*-

import unittest
from blood.validation import ValidateName


class ValidateNameTests(unittest.TestCase):
    def test_name_contains_only_letter(self):
        self.assertFalse(ValidateName.validate_name('Joska1'))

    def test_number_of_names(self):
        self.assertFalse(ValidateName.validate_name('Joska'))

    def test_gender(self):
        self.assertTrue(ValidateName.valid_gender("f" or "m"))

    def invalid_gender(self):
        self.assertFalse(ValidateName.valid_gender("FM"))


if __name__ == '__main__':
    unittest.main()
