# -*- coding: UTF-8 -*-

import unittest
from functions import Donor
from functions import Event
import datetime


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
    def test_enough_weight(self):
        bela = Donor()
        bela.weight = 51
        bela.lastdonationdate = '2013.11.05'
        bela.dateofbirth = '1990.02.26'
        self.assertTrue(bela.is_suitable())

    def test_too_skinny(self):
        bela = Donor()
        bela.weight = 50
        bela.lastdonationdate = '2013.11.05'
        bela.dateofbirth = '1990.02.26'
        self.assertFalse(bela.is_suitable())

    def test_too_early_last_donation(self):
        bela = Donor()
        bela.weight = 75
        bela.lastdonationdate = (datetime.datetime.today()-datetime.timedelta(days=70)).strftime("%Y.%m.%d")
        bela.dateofbirth = '1990.02.26'
        self.assertFalse(bela.is_suitable())

    def test_more_than_three_months(self):
        bela = Donor()
        bela.weight = 75
        bela.lastdonationdate = (datetime.datetime.today()-datetime.timedelta(days=100)).strftime("%Y.%m.%d")
        bela.dateofbirth = '1990.02.26'
        self.assertTrue(bela.is_suitable())

    def test_donor_too_young(self):
        bela = Donor()
        bela.weight = 75
        bela.lastdonationdate = "2014.01.01"
        bela.dateofbirth = "2014.01.01"
        self.assertFalse(bela.is_suitable())

    def test_donor_old_enough(self):
        bela = Donor()
        bela.weight = 75
        bela.lastdonationdate = "2014.01.01"
        bela.dateofbirth = "1956.01.01"
        self.assertTrue(bela.is_suitable())


class DonorAgeTests(unittest.TestCase):
    def test_donor_age(self):
        bela = Donor()
        bela.dateofbirth = '1990.02.26'
        szuletes = datetime.datetime.strptime(bela.dateofbirth, "%Y.%m.%d")
        kor = (datetime.datetime.today() - szuletes).days // 365
        self.assertEqual(bela.donor_age(), kor)


class IDExpirationTests(unittest.TestCase):
    def test_ID_expired_8_days_ago(self):
        bela = Donor()
        bela.expofid = (datetime.datetime.today() - datetime.timedelta(days=8)).strftime("%Y.%m.%d")
        self.assertFalse(bela.id_not_expired())

    def test_ID_expired_1_days_ago(self):
        bela = Donor()
        bela.expofid = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%Y.%m.%d")
        self.assertFalse(bela.id_not_expired())

    def test_ID_not_expired(self):
        bela = Donor()
        bela.expofid = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime("%Y.%m.%d")
        self.assertTrue(bela.id_not_expired())


class DocTypeTests(unittest.TestCase):
    def test_valid_passport(self):
        bela = Donor()
        bela.uniqueid = 'ASDFGH12'
        self.assertEqual(bela.type_of_doc(), 'PASSPORT')

    def test_valid_ID(self):
        bela = Donor()
        bela.uniqueid = '123456AB'
        self.assertEqual(bela.type_of_doc(), 'ID')

# Event Tests
class TenDaysRegTests(unittest.TestCase):
    def test_more_than_ten_days(self):
        vampireparty = Event()
        vampireparty.date_of_event = (datetime.datetime.today() + datetime.timedelta(days=11)).strftime("%Y.%m.%d")
        self.assertTrue(vampireparty.registration_in_tendays())

    def test_less_than_ten_days(self):
        vampireparty = Event()
        vampireparty.date_of_event = (datetime.datetime.today() + datetime.timedelta(days=9)).strftime("%Y.%m.%d")
        self.assertFalse(vampireparty.registration_in_tendays())

class IsWeekdayTests(unittest.TestCase):
    def test_friday(self):
        vampireparty = Event()
        vampireparty.date_of_event = '2015.11.06'
        self.assertTrue(vampireparty.is_weekday())

    def test_saturday(self):
        vampireparty = Event()
        vampireparty.date_of_event = '2015.11.07'
        self.assertFalse(vampireparty.is_weekday())

    def test_sunday(self):
        vampireparty = Event()
        vampireparty.date_of_event = '2015.11.08'
        self.assertFalse(vampireparty.is_weekday())


class CalculateDurationTests(unittest.TestCase):
    def test_valid_calculation(self):
        vampireparty = Event()
        vampireparty.start_time = '10:00'
        vampireparty.end_time = '18:00'
        self.assertEqual(vampireparty.calculate_duration(), 480)


class MaxDonorNumberTests(unittest.TestCase):
    def test_max_donor_with_2_beds(self):
        vampireparty = Event()
        vampireparty.start_time = '10:00'
        vampireparty.end_time = '18:00'
        vampireparty.duration = vampireparty.calculate_duration()
        vampireparty.available_beds = 2
        self.assertEqual(vampireparty.max_donor_number(), 30)

if __name__ == '__main__':
    unittest.main()
