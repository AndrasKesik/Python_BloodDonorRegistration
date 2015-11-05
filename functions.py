# -*- coding: UTF-8 -*-
import random
import datetime

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

    def is_suitable(self, weight, lasdonationdate, dateofbirth):
        """Is the donor suitable for donation?
            Returns True or False"""
        lastdonation = (datetime.datetime.now() - lasdonationdate).days
        age = (datetime.datetime.now() - dateofbirth).days // 365
        return weight > 50 and lastdonation > 90 and age > 18

    def donor_age(self, dateofbirth):
        """Calculates the donor's age based on birth date
            Returns an integer"""
        birth = datetime.datetime.strptime(dateofbirth, "%Y.%m.%d")
        age = (datetime.datetime.now() - birth).days // 365
        return int(age)


    def id_not_expired(self, expiration_date):
        """Checks for ID
            Returns True or False"""
        return expiration_date < datetime.datetime.now()

    def type_of_doc(self, doc_id):
        """Decides whether it's an ID or a Passport
            Returns 'ID' or 'PASSPORT' strings """
        if doc_id[-2:].isdigit() and doc_id[:-2].isalpha():
            return "PASSPORT"
        elif doc_id[:-2].isdigit() and doc_id[-2:].isalpha():
            return "ID"

    def data_out(self, name, weight, birthdate, age, emailaddress):
        """Writes out the donor's data in the given form.
            Returns string"""
        return "{} \n {}kg \n {} - {} years old \n {}".format(name, weight, birthdate, age, emailaddress)


    def generate_hemoglobin_level(self):
        """Generate hemoglobin level and decides if the donor is suitable or not
            Returns True or False"""
        hemoglobin = random.randint(80, 200)
        return hemoglobin > 110


class Event():
    """
        -Az event adatai:
        date_of_event
        startime of donation
        end time of donation
        zip code
        city address
        available_beds
        planned donor number

    """
    def registration_in_tendays(self, date_of_event):
        """Checks if the registration occoured at least 10 days before the event
            Returns True or False"""
        pass

    def is_weekday(self, date_of_event):
        return (date_of_event - datetime.datetime.now().date()).days > 10

    def is_weekday(self):
        """Checks if the Date is on a weekday or not
            Returns True or False"""
        return date_of_event.isoweekday() < 5


    def caculate_duration(self, starttime, endtime):
        """Calculates the duration of the donation based on start- and endtime
            Returns the duration"""
        return (endtime - starttime).min


    def max_donor_number(self, duration, available_beds):
        """Calculates the maximum donor numbers
            Returns an integer"""
        preparation_time = 30
        donation_time = 30
        max_donor_number = ((duration - preparation_time) / donation_time) * available_beds
        return int(max_donor_number)

