import unittest
from blood.validation import validate_name, validate_email


class ValidateName(unittest.TestCase):
	def test_name_contains_only_letter(self):
		self.assertFalse(validate_name('Joska1'))

	def test_number_of_names(self):
		self.assertFalse(validate_name('Joska'))


class ValidEmail(unittest.TestCase):
	def test_email_contains_at(self):
		self.assertFalse(validate_email('jdat.com'))

	def test_email_ending_wrong(self):
		self.assertFalse(validate_email('j@dat.con'), validate_email('j@dat.net'))

	def test_email_ending_right(self):
		self.assertTrue(validate_email('j@dat.com'), validate_email('j@dat.hu'))

	def test_email_not_starts_with_at(self):
		self.assertFalse(validate_email('@dat.com'))


if __name__ == '__main__':
	unittest.validation()
