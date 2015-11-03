import unittest
from blood.validation import validate_name


class ValidateName(unittest.TestCase):
	def test_name_contains_only_letter(self):
		self.assertFalse(validate_name('Joska1'))

	def test_number_of_names(self):
		self.assertFalse(validate_name('Joska'))


if __name__ == '__main__':
	unittest.validation()
