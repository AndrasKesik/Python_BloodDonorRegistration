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

    def parse_name(self):
        """Parses the name.
            Returns a list"""
        name = self.name.split()
        return name

    def is_suitable(self):
        """Is the donor suitable for donation?
            Returns True or False"""

        lastdonation = (datetime.datetime.now() - self.lasdonationdate).days
        age = (datetime.datetime.now() - self.dateofbirth).days // 365
        return self.weight >= 50 and self.lastdonation > 90 and age >= 18

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
        self.hemoglobin = random.randint(80, 200)
        return self.hemoglobin >= 110
    """
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

    def registration_in_tendays(self, date_of_event):
        """Checks if the registration occoured at least 10 days before the event
            Returns True or False"""
        return (date_of_event - datetime.datetime.now().date()).days > 10

    def is_weekday(self, date_of_event):
        """Checks if the Date is on a weekday or not
            Returns True or False"""
        return date_of_event.isoweekday() < 5


    def caculate_duration(self, start_time, end_time):
        """Calculates the duration of the donation based on start- and endtime
            Returns the duration"""
        return (end_time - start_time).min


    def max_donor_number(self, duration, available_beds):
        """Calculates the maximum donor numbers
            Returns an integer"""
        preparation_time = 30
        donation_time = 30
        max_donor_number = ((duration - preparation_time) / donation_time) * available_beds
        return int(max_donor_number)


