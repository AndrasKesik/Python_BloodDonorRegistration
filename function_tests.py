# -*- coding: UTF-8 -*-

import unittest
from functions import Donor


# Donor Tests
class ParseNameTests(unittest.TestCase):
    def test_parse_name(self):
        bela = Donor()
        bela.name = "bela"
        # Act
        splitted_name_list = bela.parse_name()
        # Assert
        self.assertEqual(1, len(splitted_name_list))

    def test_parse_name_two_part_name(self):
        # arrange
        kesik_andras = Donor()
        kesik_andras.name = "Kesik Andras"
        name_parts = ["Kesik", "Andras"]
        # act
        result = kesik_andras.parse_name()
        # assert
        self.assertEqual(name_parts, result)


class SuitabilityTests(unittest.TestCase):
    def test_too_skinny(self):
        weight = 49
        last_donation_date = datetime.strptime('2013.11.05', '%Y.%m.%d')
        date_of_birth = datetime.strptime('1990.02.26', '%Y.%m.%d')
        self.assertFalse(Donor.is_suitable(weight, last_donation_date, date_of_birth))

    def test_too_early_last_donation(self):
        weight = 75
        date_of_testing = datetime.today()
        last_donation_date = datetime.strptime('2013.11.05', '%Y.%m.%d')
        date_of_birth = datetime.strptime('1990.02.26', '%Y.%m.%d')
        self.assertFalse(Donor.is_suitable(weight, last_donation_date, date_of_birth))

    def test_donor_too_young(self):
        weight = 75
        date_of_testing = datetime.today()
        last_donation_date = date_of_testing - timedelta(days=31)
        date_of_birth = date_of_testing - timedelta(days=750)
        self.assertFalse(Donor.is_suitable(weight, last_donation_date, date_of_birth))


class DonorAgeTests(unittest.TestCase):
    def test_donor_age(self):
        date_of_testing = datetime.today()
        birthday = datetime.strptime('1990.02.26', '%Y.%m.%d')
        age = (birthday - date_of_testing).days // 365
        self.assertEqual(Donor.donor_age(birthday), age)


class IDExpirationTests(unittest.TestCase):
    def test_ID_expired_8_days_ago(self):
        date_of_testing = datetime.today()
        expired_date = date_of_testing - timedelta(days=8)
        self.assertFalse(Donor.id_not_expired(expired_date))

    def test_ID_expired_1_days_ago(self):
        date_of_testing = datetime.today()
        expired_date = date_of_testing - timedelta(days=1)
        self.assertFalse(Donor.id_not_expired(expired_date))

    def test_ID_not_expired(self):
        date_of_testing = datetime.today()
        expiration_date = date_of_testing + timedelta(days=3)
        self.assertFalse(Donor.id_not_expired(expiration_date))


class DocTypeTests(unittest.TestCase):
    def test_valid_passport(self):
        self.assertEqual(Donor.type_of_doc('ASDFGH12'), 'PASSPORT')

    def test_valid_ID(self):
        self.assertEqual(Donor.type_of_doc('123456AB'), 'ID')


class DataOutTests(unittest.TestCase):
    def test_something(self):
        self.assertFalse()


class HemoglobinTests(unittest.TestCase):
    pass


# Event Tests
class TenDaysRegTests(unittest.TestCase):
    # needs review and edit
    date_of_testing = datetime.today()
    plus_12_days = date_of_testing + timedelta(days=12)
    plus_8_days = date_of_testing + timedelta(days=8)

    def test_more_than_ten_days(self):
        self.assertTrue(Event.registration_in_tendays(plus_12_days))

    def test_less_than_ten_days(self):
        self.assertFalse(Event.registration_in_tendays(plus_8_days))


class IsWeekdayTests(unittest.TestCase):
    # needs review and edit
    def test_valid_case(self):
        friday = datetime.strptime('2015.11.06', '%Y.%m.%d')
        self.assertTrue(Event.is_weekday(friday))

    def test_invalid_case(self):
        saturday = datetime.strptime('2015.11.07', '%Y.%m.%d')
        self.assertFalse(Event.is_weekday(saturday))

    def test_invalid_case2(self):
        sunday = datetime.strptime('2015.11.08', '%Y.%m.%d')
        self.assertFalse(Event.is_weekday(sunday))


class CalculateDurationTests(unittest.TestCase):
    def test_valid_calculation(self):
        start_time = datetime.strptime('10:00', '%H:%M')
        end_time = datetime.strptime('18:00', '%H:%M')
        duration = end_time - start_time
        self.assertEqual(Event.caculate_duration(start_time, end_time), duration)


class MaxDonorNumberTests(unittest.TestCase):
    def test_max_donor_with_2_beds(self):
        start_time = datetime.strptime('10:00', '%H:%M')
        end_time = datetime.strptime('18:00', '%H:%M')
        duration = end_time - start_time
        available_beds = 2
        self.assertEqual(Event.max_donor_number(duration, available_beds), 30)

if __name__ == '__main__':
    unittest.main()
