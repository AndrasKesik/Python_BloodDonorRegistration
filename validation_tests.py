import unittest
from blood.validation import valid_gender

class validate_gender(unittest.TestCase):
    def test_valid_input(self):
        self.assertTrue(valid_gender("f"))

if __name__ == '__main__':
    unittest.main()