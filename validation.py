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
    def validate_zipcode(zipcode):
        return len(zipcode) == 4 and zipcode.isdigit() and zipcode[0] != 0

    @staticmethod
    def validate_id(doc_id:str):
        if doc_id[:-2].isdigit() and doc_id[-2:].isalpha() or doc_id[2:].isdigit() and doc_id[:2].isalpha():
            return True
        else:
            return False

    @staticmethod
    def validate_mobilnumber():
        pass


    @staticmethod
    def validate_sickness():
        pass

print(Validate.validate_id("233222as"))
print(Validate.validate_id("as322223"))
print(Validate.validate_id("as3222233asd"))