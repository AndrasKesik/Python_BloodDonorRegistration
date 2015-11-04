# -*- coding: UTF-8 -*-
import datetime
blood_type = ("A+", "A-", "B+", "B-", "AB+", "AB-", "0+", "0-")
cities = ("Miskolc", "Kazincbacika", "Szerencs", "Sarospatak")


class Validate():

    @staticmethod
    def valid_gender(gender_string):
        """Checks the gender input"""
        return gender_string.upper() == "F" or gender_string.upper() == "M"

    @staticmethod
    def validate_name(name_string):
        """Checks the name input"""
        return name_string.isalpha() and len(name_string) > 1

    @staticmethod
    def validate_email(email_string: str):
        """Checks the email input"""
        return '@' in email_string and email_string.endswith(('.hu', '.com')) and \
            email_string.index('@') > 0

    @staticmethod
    def validate_date(date):
        """Checks that the date format is correct"""
        date_format = "%Y.%m.%d"
        try:
            datetime.datetime.strptime(date, date_format)
        except:
            return False
        return True



    @staticmethod
    def validate_time():
        pass

    @staticmethod
    def validate_positive_int(number):
        """Checks the weight, hemoglobin, bed and donor number is positive integer"""
        return number.isdigit and int(number) > 1

    @staticmethod
    def validate_blood_type(type_of_blood):
        """Checks that the blood type is in the given list"""
        if type_of_blood.upper() in blood_type:
            return True


    @staticmethod
    def validate_city_name(city):
        """Checks that the input is in the given list"""
        if city.capitalize() in cities:
            return True

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

