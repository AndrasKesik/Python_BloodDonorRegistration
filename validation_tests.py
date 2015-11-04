# -*- coding: UTF-8 -*-

import unittest
from validation import Validate


class DateTests(unittest.TestCase):
    def test_mukodo(self):
        self.assertTrue(Validate.validate_date("1991.02.10"))

    def test_pontalkezdodo(self):
        self.assertFalse(Validate.validate_date(".02.10"))

    def test_nemteljes(self):
        self.assertFalse(Validate.validate_date("1991.02."))

    def test_nemmukodo(self):
        self.assertFalse(Validate.validate_date("19910210"))

    def test_nothing(self):
        self.assertFalse(Validate.validate_date(""))

class TimeTests(unittest.TestCase):
    pass
#
#
#
#
#
#
#
#

class PositiveIntTests(unittest.TestCase):
    def test_positive(self):
        self.assertTrue(Validate.validate_positive_int("42"))

    def test_string(self):
        self.assertFalse(Validate.validate_positive_int("hsvee"))

    def test_nothing(self):
        self.assertFalse(Validate.validate_positive_int("-15"))

    def test_null(self):
        self.assertFalse(Validate.validate_positive_int("0"))

    def test_nothing(self):
        self.assertFalse(Validate.validate_positive_int(""))


class BloodTypeTests(unittest.TestCase):
    def test_bpluslower(self):
        self.assertTrue(Validate.validate_blood_type("b+"))

    def test_abminusupper(self):
        self.assertTrue(Validate.validate_blood_type("AB-"))

    def test_oplus(self):
        self.assertTrue(Validate.validate_blood_type("0+"))

    def test_null(self):
        self.assertFalse(Validate.validate_blood_type("0"))

    def test_ofalse(self):
        self.assertFalse(Validate.validate_blood_type("O+"))

    def test_a(self):
        self.assertFalse(Validate.validate_blood_type("A"))

    def test_long(self):
        self.assertFalse(Validate.validate_blood_type("ggsiiuh sv448hg hsuh94"))

    def test_nothing(self):
        self.assertFalse(Validate.validate_blood_type(""))

class CityNameTests(unittest.TestCase):
    def test_azavaroslower(self):
        self.assertTrue(Validate.validate_city_name("miskolc"))

    def test_azavarosupper(self):
        self.assertTrue(Validate.validate_city_name("SZERENCS"))

    def test_longstring(self):
        self.assertFalse(Validate.validate_city_name("gegwv_svsv"))

    def test_number(self):
        self.assertFalse(Validate.validate_city_name("29"))

    def test_nemazavaros(self):
        self.assertFalse(Validate.validate_city_name("Budapest"))

    def test_nothing(self):
        self.assertFalse(Validate.validate_city_name(""))

class AddressTests(unittest.TestCase):
    pass
class ZipCodeTests(unittest.TestCase):
    pass

class IdTests(unittest.TestCase):
    pass
class MobilNumberTests(unittest.TestCase):
    pass
#
#
#
#
#
#
#
#
#
#
#
#

class SicknessTests(unittest.TestCase):
    def test_Nupper(self):
        self.assertTrue(Validate.validate_sickness("N"))

    def test_ylower(self):
        self.assertTrue(Validate.validate_sickness("y"))

    def test_number(self):
        self.assertFalse(Validate.validate_sickness("-436"))

    def test_longstring(self):
        self.assertFalse(Validate.validate_sickness("iuahivuseiu4988hf"))

    def test_nothing(self):
        self.assertFalse(Validate.validate_sickness(""))

class NameTests(unittest.TestCase):
    def test_name_contains_only_letter(self):
        self.assertFalse(Validate.validate_name("Joska1"))

    def test_number_of_names3(self):
        self.assertTrue(Validate.validate_name('Joska'))

    def test_number_of_names2(self):
        self.assertTrue(Validate.validate_name('asd'))

    def test_number(self):
        self.assertFalse(Validate.validate_name("568 958"))

    def test_number_of_names(self):
        self.assertTrue(Validate.validate_name('Jóska Aladár'))

    def test_nothing(self):
        self.assertFalse(Validate.validate_name(""))


class GenderTests(unittest.TestCase):
    def test_(self):
        self.assertTrue(Validate.valid_gender("f"))

    def test_lower(self):
        self.assertFalse(Validate.valid_gender("b"))

    def test_upper(self):
        self.assertTrue(Validate.valid_gender("M"))

    def test_number(self):
        self.assertFalse(Validate.valid_gender("5"))

    def test_long(self):
        self.assertFalse(Validate.valid_gender("agogioivsonvoeinoioin44ö9jos"))

    def test_nothing(self):
        self.assertFalse(Validate.valid_gender(""))


class EmailTests(unittest.TestCase):
    def test_email_contains_at(self):
        self.assertFalse(Validate.validate_email('jdat.com'))

    def test_email_ending_wrong(self):
        self.assertFalse(Validate.validate_email('j@dat.con'), Validate.validate_email('j@dat.net'))

    def test_email_ending_right(self):
        self.assertTrue(Validate.validate_email('j@dat.com'), Validate.validate_email('j@dat.hu'))

    def test_email_not_starts_with_at(self):
        self.assertFalse(Validate.validate_email('@dat.com'))

    def test_number(self):
        self.assertFalse(Validate.validate_email("5462"))

    def test_nothing(self):
        self.assertFalse(Validate.validate_email(""))


if __name__ == '__main__':
    unittest.main()
