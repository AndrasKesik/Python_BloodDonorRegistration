# -*- coding: UTF-8 -*-


class Validate():

    @staticmethod
    def valid_gender(gender_string):
        """Checks the gender input"""
        return gender_string.upper() == "F" or gender_string.upper() == "M"

    @staticmethod
    def validate_name(name_string):
        """Checks the name input"""
        name = name_string.split()
        return name_string.replace(' ', '').isalpha() and len(name) > 1

    @staticmethod
    def validate_email(email_string: str):
        """Checks the email input"""
        return '@' in email_string and email_string.endswith(('.hu', '.com')) and \
            email_string.index('@') > 0

    @staticmethod
    def validate_date():
        pass

    @staticmethod
    def validate_time(time_string):
        splitted_time = time_string.split(":")
        return len(splitted_time) == 2 and \
            splitted_time[0].isdigit() and int(splitted_time[0]) in range(0, 25) and \
            splitted_time[1].isdigit() and int(splitted_time[1]) in range(0, 60)

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
    def address(address_string):
        return len(address_string) < 25

    @staticmethod
    def validate_zipcode():
        pass

    @staticmethod
    def validate_id():
        pass

    @staticmethod
    def mobilnumber(number_string: str):
        country_prefix = ('+36', '06')
        provider_identifier = ('20', '30', '70')
        if number_string.startswith(country_prefix[0]):
            return len(number_string) == 12 and number_string[3:5] in provider_identifier and \
                   number_string[1:13].isnumeric()
        if number_string.startswith(country_prefix[1]):
            return len(number_string) == 11 and number_string[2:4] in provider_identifier and \
                   number_string[1:12].isnumeric()
        else:
            return False


    @staticmethod
    def validate_sickness(sickness_state):
        valid_answers = ('Y', 'N')
        return sickness_state.upper() == valid_answers[0] or sickness_state.upper() == valid_answers[0]

