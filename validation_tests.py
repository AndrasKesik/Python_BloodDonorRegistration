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
    def test_time_alpha(self):
        self.assertFalse(Validate.validate_time('5:w0'))

    def test_time_too_many_char(self):
        self.assertFalse(Validate.validate_time('005:30'))

    def test_time_too_much_hour(self):
        self.assertFalse(Validate.validate_time('25:30'))

    def test_time_too_much_min(self):
        self.assertFalse(Validate.validate_time('15:60'))

    def test_time_wrong_divider(self):
        self.assertFalse(Validate.validate_time('15.40'))

    def test_time_nothing(self):
        self.assertFalse(Validate.validate_time(''))

    def test_time_valid(self):
        self.assertTrue(Validate.validate_time('12:35'))


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
    def test_address_not_too_long(self):
        self.assertFalse(Validate.address('Jozsef Attila utca a kukak mogott a fagyott macskak mellett 36'))

    def test_address_nothing(self):
        self.assertFalse(Validate.address(''))

    def test_address_valid(self):
        self.assertTrue(Validate.address('Jozsef Attila u. 36. 30/1'))


class ZipCodeTests(unittest.TestCase):
    def test_zip_contains_alpha(self):
        self.assertFalse(Validate.validate_zipcode('a234'))

    def test_zip_not_four_char(self):
        self.assertFalse(Validate.validate_zipcode('12345'))

    def test_zip_starts_with_zero(self):
        self.assertFalse(Validate.validate_zipcode('0123'))

    def test_zip_contains_non_alphanum_char(self):
        self.assertFalse(Validate.validate_zipcode('-123'), Validate.validate_zipcode('12+4'))

    def test_zip_none(self):
        self.assertFalse(Validate.validate_zipcode(''))

    def test_zip_correct(self):
        self.assertTrue(Validate.validate_zipcode('1234'))


class IdTests(unittest.TestCase):
    pass


class MobilNumberTests(unittest.TestCase):
    def test_mobile_country_code(self):
        self.assertFalse(Validate.mobilnumber('+40702915521'))

    def test_mobile_provider(self):
        self.assertFalse(Validate.mobilnumber('06602915521'))

    def test_mobile_length(self):
        self.assertFalse(Validate.mobilnumber('067029155214'))

    def test_mobile_alpha(self):
        self.assertFalse(Validate.mobilnumber('+36702i15521'))

    def test_mobile_different_format(self):
        self.assertTrue(Validate.mobilnumber('+36/70 291 5521'))

    def test_mobile_nothing(self):
        self.assertFalse(Validate.mobilnumber(''))

    def test_mobile_valid(self):
        self.assertTrue(Validate.mobilnumber('+36702915521'), Validate.mobilnumber('06302915521'))


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
