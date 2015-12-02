# -*- coding: UTF-8 -*-
import os
from constant_variables import *

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
