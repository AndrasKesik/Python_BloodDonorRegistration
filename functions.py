# -*- coding: UTF-8 -*-
import random
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

    age=""

    def parse_name(self):
        """Parses the name.
            Returns a list"""
        name = self.name.split()
        return name


    def donor_age(self):
        """Calculates the donor's age based on birth date
            Returns an integer"""
        birth = datetime.datetime.strptime(self.dateofbirth, "%Y.%m.%d")
        kor = (datetime.datetime.now() - birth).days // 365
        return kor

    def is_suitable(self):
        """Is the donor suitable for donation?
            Returns True or False"""
        last_don_dateformat = datetime.datetime.strptime(self.lastdonationdate, "%Y.%m.%d")
        birth = datetime.datetime.strptime(self.dateofbirth, "%Y.%m.%d")
        hanynapja_adott =  (datetime.datetime.now() - last_don_dateformat).days
        kor = (datetime.datetime.now() - birth).days // 365
        return self.weight > 50 and hanynapja_adott > 90 and kor > 18

    def id_not_expired(self):
        """Checks for ID
            Returns True or False"""

        lejarat = datetime.datetime.strptime(self.expofid, "%Y.%m.%d")
        return lejarat > datetime.datetime.now()

    def type_of_doc(self):
        """Decides whether it's an ID or a Passport
            Returns 'ID' or 'PASSPORT' strings """
        if self.uniqueid[-2:].isdigit() and self.uniqueid[:-2].isalpha():
            return "PASSPORT"
        elif self.uniqueid[:-2].isdigit() and self.uniqueid[-2:].isalpha():
            return "ID"

    def data_out(self):
        """Writes out the donor's data in the given form.
            Returns string"""
        return "{} \n {}kg \n {} - {} years old \n {}".format(self.name, self.weight, self.dateofbirth, self.age , self.emailaddress)


    def generate_hemoglobin_level(self):
        """Generate hemoglobin level and decides if the donor is suitable or not
            Returns True or False"""
        hemoglobin = random.randint(80, 200)
        return hemoglobin >= 110
    """
    ## FUTURE FEATURE NE NYULJ HOZZÁ ##
    def __str__(self):
        result = "Name: " + self.name
        if self.weight != "":
            result +="\nWeight: " + self.weight
        if self.gender != "":
            result +="\nGender: " + self.gender
        if self.dateofbirth != "":
            result +="\nDate of Birth: " + self.dateofbirth
        if self.lastdonationdate:
            result +="\nLast Donation: " + self.lastdonationdate
        if self.wassick != "":
            result +="\nWas he/she sick: " + self.wassick
        return result
    """

class Event():

    date_of_event = ""
    start_time = ""
    end_time = ""
    zip_code = ""
    city_address = ""
    available_beds = ""
    planned_donor_number = ""

    duration = ""

    def registration_in_tendays(self):
        """Checks if the registration occoured at least 10 days before the event
            Returns True or False"""
        datum = datetime.datetime.strptime(self.date_of_event, '%Y.%m.%d')
        return (datum - datetime.datetime.now()).days >= 10

    def is_weekday(self):
        """Checks if the Date is on a weekday or not
            Returns True or False"""
        datum = datetime.datetime.strptime(self.date_of_event, '%Y.%m.%d')
        return datum.isoweekday() < 6


    def calculate_duration(self):
        """Calculates the duration of the donation based on start- and endtime
            Returns the duration"""
        end = datetime.datetime.strptime(self.end_time, '%H:%M')
        start = datetime.datetime.strptime(self.start_time, '%H:%M')
        return (end - start).seconds//60


    def max_donor_number(self):
        """Calculates the maximum donor numbers
            Returns an integer"""
        preparation_time = 30
        donation_time = 30
        max_donor_number = ((self.duration - preparation_time) / donation_time) * self.available_beds
        return max_donor_number


