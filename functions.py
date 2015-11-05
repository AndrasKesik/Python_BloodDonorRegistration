# -*- coding: UTF-8 -*-
import datetime

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

    def donor_age(self, dateofbirth):
        """Calculates the donor's age based on birth date
            Returns an integer"""
        birth = datetime.datetime.strptime(dateofbirth, "%Y.%m.%d")
        age = (datetime.datetime.now() - birth).days // 365
        return int(age)


    def id_not_expired(self):
        """Checks for ID
            Returns True or False"""
        pass

    def type_of_doc(self):
        """Decides whether it's an ID or a Passport
            Returns 'ID' or 'PASSPORT' strings """
        pass

    def data_out(self, name, weight, birthdate, age, emailaddress):
        """Writes out the donor's data in the given form.
            Returns string"""
        print(name, "\n", weight,"kg" "\n", birthdate, "-", age,"years old" "\n", emailaddress)


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
        available_beds
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

    def max_donor_number(self, duration, available_beds):
        """Calculates the maximum donor numbers
            Returns an integer"""
        preparation_time = 30
        donation_time = 30
        max_donor_number = ((duration - preparation_time) / donation_time) * available_beds
        return int(max_donor_number)



