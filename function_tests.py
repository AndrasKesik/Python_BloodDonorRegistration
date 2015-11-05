# -*- coding: UTF-8 -*-

import unittest
from functions import Donor

class DonorTests(unittest.TestCase):
    def test_parse_name(self):
        bela = Donor()
        self.assertEqual(1, len(bela.parse_name("bela")))
        self.assertEqual(2, len(bela.parse_name("movacs bela")))
        self.assertEqual(3, len(bela.parse_name("movacs bela pista")))

class EventTests(unittest.TestCase):
    def test_something(self):
        self.assertFalse()

if __name__ == '__main__':
    unittest.main()
