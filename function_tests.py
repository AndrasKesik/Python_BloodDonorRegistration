# -*- coding: UTF-8 -*-

import unittest
from functions import Donor


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
    def test_something(self):
        self.assertFalse()


# Event Tests
class TenDaysRegTests(unittest.TestCase):
    def test_something(self):
        self.assertFalse()


class IsWeekdayTests(unittest.TestCase):
    def test_something(self):
        self.assertFalse()


class CalculateDurationTests(unittest.TestCase):
    def test_something(self):
        self.assertFalse()


class MaxDonorNumberTests(unittest.TestCase):
    def test_something(self):
        self.assertFalse()

if __name__ == '__main__':
    unittest.main()
