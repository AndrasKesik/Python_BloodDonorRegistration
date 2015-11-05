# -*- coding: UTF-8 -*-
import datetime
blood_type = ("A+", "A-", "B+", "B-", "AB+", "AB-", "0+", "0-")
cities = ("Miskolc", "Kazincbacika", "Szerencs", "Sarospatak")


class Validate():

    @staticmethod
    def validate_gender(gender_string):
        """Checks the gender input"""
        return gender_string.upper() == "F" or gender_string.upper() == "M"

    @staticmethod
    def validate_name(name_string):
        """Checks the name input"""
        name = name_string.split()
        return name_string.replace(' ', '').isalpha() and len(name) > 1


    @staticmethod
    def validate_email(email_string):
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
    def validate_time(time_string):
        splitted_time = time_string.split(":")
        return len(splitted_time) == 2 and len(splitted_time[0])==2 and len(splitted_time[1])==2 and \
            splitted_time[0].isdigit() and int(splitted_time[0]) in range(0, 25) and \
            splitted_time[1].isdigit() and int(splitted_time[1]) in range(0, 60)

    @staticmethod
    def validate_positive_int(number):
        """Checks the weight, hemoglobin, bed and donor number is positive integer"""
        try:
            if int(number) > 0:
                return True
        except:
            return False

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
    def validate_address(address_string):
        return 0 < len(address_string) < 25

    @staticmethod
    def validate_zipcode(zipcode):
        return len(zipcode) == 4 and zipcode.isdigit() and zipcode[0] != 0 and not zipcode.startswith("0")

    @staticmethod
    def validate_id(doc_id):
        if doc_id[:-2].isdigit() and doc_id[-2:].isalpha() or doc_id[2:].isdigit() and doc_id[:2].isalpha():
            return True
        else:
            return False

    @staticmethod
    def validate_mobilnumber(number_string):
        country_prefix = ('+36', '06')
        provider_identifier = ('20', '30', '70')
        if number_string.startswith(country_prefix[0]):
            return len(number_string) == 12 and number_string[3:5] in provider_identifier and \
                   number_string[4:13].isnumeric()
        elif number_string.startswith(country_prefix[1]):
            return len(number_string) == 11 and number_string[2:4] in provider_identifier and \
                   number_string[3:12].isnumeric()
        else:
            return False


    @staticmethod
    def validate_sickness(sickness_state):
        if sickness_state.upper() in "YN" and len(sickness_state)==1:
            return True
        else:
            return False

print(Validate.validate_id("233222as"))
print(Validate.validate_id("as322223"))
print(Validate.validate_id("as3222233asd"))

