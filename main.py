# -*- coding: UTF-8 -*-
import os
import time
clear = lambda: os.system('cls')

class Donor():
    """
       - A Donor Adatai
        name=
        weight=
        gender=
        dateofbirth=
        lastdonationdate=
        washesick=
        unique id
        bloodtype
        expiration of id
        email adress
        mobilnumber
    """
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


#MAIN MENU
clear()
while True:
    print("\n\t\t\t--- WELCOME TO THE BLOOD DONATION SYSTEM ---\t\t\t")
    print("\t\t\t\t - Made By the Code Stars -\t\t\t\t\n\n")
    try:
        user_input = input("(1) Blood Donor Registration\n(2) Event Registration\n(3) EXIT\n\n> ")
        if user_input not in '123' or len(user_input)>1:
            raise ValueError
        clear()

        #BLOOD DONATION MENUPONT
        if user_input=='1':
            while True:
                print("\n\t\t\t--- WELCOME TO THE BLOOD DONATION SYSTEM ---\t\t\t")
                print("\t\t\t\t - Made By the Code Stars -\t\t\t\t\n\n")
                try:
                    user_input=input('(1) Add New Donor\n(2) Remove Donor\n(3) Back\n\n> ')
                    if user_input not in '123' or len(user_input)>1:
                        raise ValueError
                    clear()

                    if user_input=='1':
                        print("----Adding new donor----\n")
                        input()
                        clear()

                    elif user_input=='2':
                        print("----Removing donor-----\n")
                        input()
                        clear()

                    elif user_input=='3':
                        clear()
                        break

                    else:
                         raise ValueError

                except:
                    print("\n\t\t! ! !  Please choose from the given numbers.  ! ! !\t\t\n ")
                    time.sleep(2)
                    clear()

        #EVENT REGISTER MENUPONT
        elif user_input=='2':
            while True:
                print("\n\t\t\t--- WELCOME TO THE BLOOD DONATION SYSTEM ---\t\t\t")
                print("\t\t\t\t - Made By the Code Stars -\t\t\t\t\n\n")
                try:
                    user_input=input('(1) Add New Event\n(2) Remove Event\n(3) Back\n\n> ')
                    clear()
                    if user_input=='1':
                        print("----Adding new event----\n")
                        input()
                        clear()
                    elif user_input=='2':
                        print("----Removing event-----\n")
                        input()
                        clear()
                    elif user_input=='3':
                        clear()
                        break
                    else:
                         raise ValueError
                except:
                    print("\n\t\t! ! !  Please choose from the given numbers.  ! ! !\t\t\n ")
                    time.sleep(2)
                    clear()

        #EXIT
        elif user_input=='3':
            clear()
            print("\n\n\n\n\n\n\t\t\t   - Thank you for using our software -\t\t\t\t")
            print("\t\t\t      - Made By the Code Stars - ")
            print("\n\n\t\t\t\t    --- GOODBYE ---")
            time.sleep(3)
            clear()
            break
        else:
            raise ValueError
    except:
        print("\n\t\t! ! !  Please choose from the given numbers.  ! ! !\t\t\n ")
        time.sleep(2)
        clear()