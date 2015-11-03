__author__ = 'kesikandras'


def validate_name(name_string):
	name = name_string.split()
	return name_string.isalpha() and len(name) > 1


def validate_email(email_string: str):
	return '@' in email_string and email_string.endswith(('.hu', '.com')) and \
		email_string.index('@') > 0


