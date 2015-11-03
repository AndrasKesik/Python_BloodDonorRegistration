__author__ = 'kesikandras'


def validate_name(name_string):
	name = name_string.split()
	return name_string.isalpha() and len(name) > 1

