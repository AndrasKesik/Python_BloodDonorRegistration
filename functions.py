# -*- coding: UTF-8 -*-

class Donor():

    name = ""
    weight = ""
    gender = ""
    dateofbirth = ""
    lastdonationdate = ""
    wassick = ""
    uniqueid = ""
    bloodtype = ""
    expofid = ""
    emailaddress = ""
    mobilnumber = ""

    def parse_name(self,name):
        """Parses the name.
            Returns a list"""
        name = name.split()
        return name

    def is_suitable(self):
        """Is the donor suitable for donation?
            Returns True or False"""
        pass

    def donor_age(self):
        """Calculates the donor's age based on birth date
            Returns an integer"""
        pass

    def id_not_expired(self):
        """Checks for ID
            Returns True or False"""
        pass

    def type_of_doc(self):
        """Decides whether it's an ID or a Passport
            Returns 'ID' or 'PASSPORT' strings """
        pass

    def data_out(self):
        """Writes out the donor's data in the given form.
            Returns string"""
        pass

    def generate_hemoglobin_level(self):
        """Generate hemoglobin level and decides if the donor is suitable or not
            Returns True or False"""
        pass

class Event():
    """
        -Az event adatai:
        date of event
        startime of donation
        end time of donation
        zip code
        city address
        available beds
        planned donor number

    """
    def registration_in_tendays(self):
        """Checks if the registration occoured at least 10 days before the event
            Returns True or False"""
        pass
    def is_weekday(self):
        """Checks if the Date is on a weekday or not
            Returns True or False"""
        pass

    def caculate_duration(self):
        """Calculates the duration of the donation based on start- and endtime
            Returns the duration"""
        pass

    def max_donor_number(self):
        """Calculates the maximum donor numbers
            Returns an integer"""
        pass



