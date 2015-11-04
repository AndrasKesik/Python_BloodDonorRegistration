# -*- coding: UTF-8 -*-


class Validate():

    @staticmethod
    def valid_gender(gender_string):
        """Checks the gender input"""
        return gender_string.upper() == "F" or gender_string.upper() == "M"

    @staticmethod
    def validate_name(name_string):
        """Checks the name input"""
        return name_string.isalpha() and len(name) > 1

    @staticmethod
    def validate_email(email_string: str):
        """Checks the email input"""
        return '@' in email_string and email_string.endswith(('.hu', '.com')) and \
            email_string.index('@') > 0

    @staticmethod
    def validate_date():
        pass

    @staticmethod
    def validate_time():
        pass

    @staticmethod
    def validate_positive_int():
        pass

    @staticmethod
    def validate_blood_type():
        pass


    @staticmethod
    def validate_city_name():
        pass

    @staticmethod
    def validate_address():
        pass


    @staticmethod
    def validate_zipcode():
        pass

    @staticmethod
    def validate_id():
        pass

    @staticmethod
    def validate_mobilnumber():
        pass


    @staticmethod
    def validate_sickness():
        pass

