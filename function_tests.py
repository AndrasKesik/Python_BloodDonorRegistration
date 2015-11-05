# -*- coding: UTF-8 -*-

from datetime import datetime
from datetime import timedelta
import unittest
from functions import Donor
from functions import Event


# Donor Tests
class ParseNameTests(unittest.TestCase):
    def test_parse_name(self):
        bela = Donor()
        self.assertEqual(1, len(bela.parse_name("bela")))
        self.assertEqual(2, len(bela.parse_name("movacs bela")))
        self.assertEqual(3, len(bela.parse_name("movacs bela pista")))


class SuitabilityTests(unittest.TestCase):
    def test_something(self):
        self.assertFalse()


class DonorAgeTests(unittest.TestCase):
    def test_something(self):
        self.assertFalse()


class IDExpirationTests(unittest.TestCase):
    def test_something(self):
        self.assertFalse()


class DocTypeTests(unittest.TestCase):
    def test_valid_passport(self):
        self.assertEqual(Donor.type_of_doc('ASDFGH12'), 'PASSPORT')

    def test_valid_ID(self):
        self.assertEqual(Donor.type_of_doc('123456AB'), 'ID')


class DataOutTests(unittest.TestCase):
    def test_something(self):
        self.assertFalse()


class HemoglobinTests(unittest.TestCase):
    def test_hemoglobin_too_high(self):
        self.assertFalse(Donor.generate_hemoglobin_level())


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

