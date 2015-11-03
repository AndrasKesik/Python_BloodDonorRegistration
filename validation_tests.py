import unittest
<<<<<<< HEAD
from blood.validation import valid_gender

class validate_gender(unittest.TestCase):
    def test_valid_input(self):
        self.assertTrue(valid_gender("f"))

if __name__ == '__main__':
    unittest.main()
=======
from blood.validation import validate_name


class ValidateName(unittest.TestCase):
    def test_name_contains_only_letter(self):
        self.assertFalse(validate_name('Joska1'))

    def test_number_of_names(self):
        self.assertFalse(validate_name('Joska'))


if __name__ == '__main__':
    unittest.validation()
>>>>>>> aabdb4a9d9bb868ff5d3652e00d18ead4167b8dd
