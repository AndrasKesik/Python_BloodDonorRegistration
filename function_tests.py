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
    def test_something(self):
        self.assertFalse()

if __name__ == '__main__':
    unittest.main()
