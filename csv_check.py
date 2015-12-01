# -*- coding: UTF-8 -*-
import os
DONORS_ELSOSOR = "name,weight,gender,date_of_birth,last_donation,last_month_sickness,unique_identifier,expiration_of_id,blood_type,hemoblogin,email,mobil\n"
EVENT_ELSOSOR = "id,date_of_event,start_time,end_time,zip_code,city,address,number_of_available_beds,planned_donor_number,final_donor_number\n"

#
# DONORS.CSV CHECK
#
class CsvChecker():
    @staticmethod
    def donor_file_check():
        if not os.path.isfile("Data/donors.csv"):
            with open("Data/donors.csv", "w") as f:
                f.write(DONORS_ELSOSOR)
        with open("Data/donors.csv", "r") as f:
            donorselso = f.readline()
            content = [line for line in f]
        if donorselso != DONORS_ELSOSOR:
            with open("Data/donors.csv", "w") as f:
                f.truncate()
                f.write(DONORS_ELSOSOR)
                for i in content:
                    f.write(i)

    @staticmethod
    def donations_file_check():
        if not os.path.isfile("Data/donations.csv"):
            with open("Data/donations.csv", "w") as f:
                f.write(EVENT_ELSOSOR)
        with open("Data/donations.csv", "r") as f:
            donorselso = f.readline()
            content = [line for line in f]
        if donorselso != EVENT_ELSOSOR:
            with open("Data/donations.csv", "w") as f:
                f.truncate()
                f.write(EVENT_ELSOSOR)
                for i in content:
                    f.write(i)
