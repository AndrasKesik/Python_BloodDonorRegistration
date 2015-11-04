# -*- coding: UTF-8 -*-

import unittest
from validation import Validate


class DateTests(unittest.TestCase):
    pass
class TimeTests(unittest.TestCase):
    pass
class PositiveIntTests(unittest.TestCase):
    pass
class BloodTypeTests(unittest.TestCase):
    pass
class CityNameTests(unittest.TestCase):
    pass
class AddressTests(unittest.TestCase):
    pass
class ZipCodeTests(unittest.TestCase):
    pass
class IdTests(unittest.TestCase):
    pass
class MobilNumberTests(unittest.TestCase):
    pass
class WassickTests(unittest.TestCase):
    pass

class NameTests(unittest.TestCase):
    def test_name_contains_only_letter(self):
<<<<<<< HEAD
        self.assertFalse(ValidateName.validate_name('Joska1'))

    def test_number_of_names(self):
        self.assertFalse(ValidateName.validate_name('Joska'))

    def test_gender(self):
        self.assertTrue(ValidateName.valid_gender("f" or "m"))

    def invalid_gender(self):
        self.assertFalse(ValidateName.valid_gender("FM"))
=======
        self.assertFalse(Validate.validate_name("Joska1"))

    def test_number_of_names(self):
        self.assertTrue(Validate.validate_name('Joska'))

    def test_number_of_names(self):
        self.assertTrue(Validate.validate_name('asd'))

    def test_number_of_names(self):
        self.assertTrue(Validate.validate_name('Jóska Aladár'))




class GenderTests(unittest.TestCase):
    def test_gender(self):
        self.assertTrue(Validate.valid_gender("f"))


class EmailTests(unittest.TestCase):
    def test_email_contains_at(self):
        self.assertFalse(Validate.validate_email('jdat.com'))

    def test_email_ending_wrong(self):
        self.assertFalse(Validate.validate_email('j@dat.con'), Validate.validate_email('j@dat.net'))

    def test_email_ending_right(self):
        self.assertTrue(Validate.validate_email('j@dat.com'), Validate.validate_email('j@dat.hu'))

    def test_email_not_starts_with_at(self):
        self.assertFalse(Validate.validate_email('@dat.com'))
>>>>>>> f5b970c96c7289ee7d534b0510daa0b9b1eefdc5


if __name__ == '__main__':
    unittest.main()
