# -*- coding: UTF-8 -*-

import unittest
from functions import Donor

class DonorTests(unittest.TestCase):
    def test_parse_name_single_name(self):
        # arrange
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

class EventTests(unittest.TestCase):
    def test_something(self):
        pass

if __name__ == '__main__':
    unittest.main()
