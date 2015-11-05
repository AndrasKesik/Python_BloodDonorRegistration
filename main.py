# -*- coding: UTF-8 -*-
import os
import time
from validation import Validate
from functions import Donor
from functions import Event
clear = lambda: os.system('cls')





#MAIN MENU
clear()
while True:
    print("\n\t\t\t--- WELCOME TO THE BLOOD DONATION SYSTEM ---\t\t\t")
    print("\t\t\t\t - Made By the Code Stars -\t\t\t\t\n\n")
    try:
        user_input = input("(1) Blood Donor Registration\n(2) Event Registration\n(3) EXIT\n\n> ")
        if user_input not in '123' or len(user_input)!=1:
            raise ValueError
        clear()

        #BLOOD DONATION MENUPONT
        if user_input=='1':
            while True:
                print("\n\t\t\t--- WELCOME TO THE BLOOD DONATION SYSTEM ---\t\t\t")
                print("\t\t\t\t - Made By the Code Stars -\t\t\t\t\n\n")
                try:
                    user_input=input('(1) Add New Donor\n(2) Remove Donor\n(3) Back\n\n> ')
                    if user_input not in '123' or len(user_input) != 1:
                        raise ValueError
                    clear()

                    if user_input=='1':
                        print("Adding new donor...\n")
                        time.sleep(1)
                        clear()
                        elsodonor = Donor()
                        while True:
                            elsodonor.name = input("Name: ")
                            if Validate.validate_name(elsodonor.name):
                                break
                            else:
                                print("\n ! Nem tartalmazhat speciális karaktert a donor neve és legalább 2 részből kell állnia ! \n")
                                time.sleep(2)
                                clear()
                        clear()

                        while True:
                            print("Name:", elsodonor.name)
                            elsodonor.weight = input("Weight (in KG): ")
                            if Validate.validate_positive_int(elsodonor.weight):
                                break
                            else:
                                print("\n ! Your weight must be a positive number !\n")
                                time.sleep(2)
                                clear()
                        clear()
                        while True:
                            print("Name:", elsodonor.name)
                            print("Weight:", elsodonor.weight)
                            elsodonor.gender = input("Gender (M/F): ")
                            if Validate.validate_gender(elsodonor.gender):
                                break
                            else:
                                print("\n ! Válaszd ki a donor nemét, (M)ale or (F)emale ! \n")
                                time.sleep(2)
                                clear()
                        clear()
                        while True:
                            print("Name:", elsodonor.name)
                            print("Weight:", elsodonor.weight)
                            print("Gender:", elsodonor.gender)
                            elsodonor.dateofbirth = input("Date of Birth: ")
                            if Validate.validate_date(elsodonor.dateofbirth):
                                break
                            else:
                                print("\n ! You can use this format to enter the date: 'YYYY.MM.DD' ! \n")
                                time.sleep(2)
                                clear()
                        clear()
                        while True:
                            print("Name:", elsodonor.name)
                            print("Weight:", elsodonor.weight)
                            print("Gender:", elsodonor.gender)
                            print("Date of Birth:", elsodonor.dateofbirth)
                            elsodonor.lastdonationdate = input("Last Donation: ")
                            if Validate.validate_date(elsodonor.lastdonationdate):
                                break
                            else:
                                print("\n ! A következő formátum alapján tudod megadni a dátumot: 'YYYY.MM.DD' ! \n")
                                time.sleep(2)
                                clear()
                        clear()
                        while True:
                            print("Name:", elsodonor.name)
                            print("Weight:", elsodonor.weight)
                            print("Gender:", elsodonor.gender)
                            print("Date of Birth:", elsodonor.dateofbirth)
                            print("Last Donation:", elsodonor.lastdonationdate)
                            elsodonor.wassick = input("Was he/she sick in the last month? (Y/N) ")
                            if Validate.validate_sickness(elsodonor.wassick):
                                break
                            else:
                                print("\n ! Choose from the given answers: (Y)es or (N)o ! \n")
                                time.sleep(2)
                                clear()
                        clear()
                        while True:
                            print("Name:", elsodonor.name)
                            print("Weight:", elsodonor.weight)
                            print("Gender:", elsodonor.gender)
                            print("Date of Birth:", elsodonor.dateofbirth)
                            print("Last Donation:", elsodonor.lastdonationdate)
                            print("Was he/she sick:", elsodonor.wassick)
                            elsodonor.uniqueid = input("Unique ID: ")
                            if Validate.validate_id(elsodonor.uniqueid):
                                break
                            else:
                                print("\n ! Létező ID-t adj meg ! \n")
                                time.sleep(2)
                                clear()
                        clear()
                        while True:
                            print("Name:", elsodonor.name)
                            print("Weight:", elsodonor.weight)
                            print("Gender:", elsodonor.gender)
                            print("Date of Birth:", elsodonor.dateofbirth)
                            print("Last Donation:", elsodonor.lastdonationdate)
                            print("Was he/she sick:", elsodonor.wassick)
                            print("Unique ID:", elsodonor.uniqueid)
                            elsodonor.bloodtype = input("Blood Type: ")
                            if Validate.validate_blood_type(elsodonor.bloodtype):
                                break
                            else:
                                print("\n ! It should be a real blood type ! \n")
                                time.sleep(2)
                                clear()
                        clear()
                        while True:
                            print("Name:", elsodonor.name)
                            print("Weight:", elsodonor.weight)
                            print("Gender:", elsodonor.gender)
                            print("Date of Birth:", elsodonor.dateofbirth)
                            print("Last Donation:", elsodonor.lastdonationdate)
                            print("Was he/she sick:", elsodonor.wassick)
                            print("Unique ID:", elsodonor.uniqueid)
                            print("Blood Type:", elsodonor.bloodtype)
                            elsodonor.expofid = input("Expiration of ID: ")
                            if Validate.validate_date(elsodonor.expofid):
                                break
                            else:
                                print("\n ! A következő formátum alapján tudod megadni a dátumot: 'YYYY.MM.DD' ! \n")
                                time.sleep(2)
                                clear()
                        clear()
                        while True:
                            print("Name:", elsodonor.name)
                            print("Weight:", elsodonor.weight)
                            print("Gender:", elsodonor.gender)
                            print("Date of Birth:", elsodonor.dateofbirth)
                            print("Last Donation:", elsodonor.lastdonationdate)
                            print("Was he/she sick:", elsodonor.wassick)
                            print("Unique ID:", elsodonor.uniqueid)
                            print("Blood Type:", elsodonor.bloodtype)
                            print("Expiration of ID:", elsodonor.expofid)
                            elsodonor.emailaddress = input("Email address: ")
                            if Validate.validate_email(elsodonor.emailaddress):
                                break
                            else:
                                print("\n ! Email should contain a @ and should end with .com or .hu ! \n")
                                time.sleep(2)
                                clear()
                        clear()
                        while True:
                            print("Name:", elsodonor.name)
                            print("Weight:", elsodonor.weight)
                            print("Gender:", elsodonor.gender)
                            print("Date of Birth:", elsodonor.dateofbirth)
                            print("Last Donation:", elsodonor.lastdonationdate)
                            print("Was he/she sick:", elsodonor.wassick)
                            print("Unique ID:", elsodonor.uniqueid)
                            print("Blood Type:", elsodonor.bloodtype)
                            print("Expiration of ID:", elsodonor.expofid)
                            print("Email:", elsodonor.emailaddress)
                            elsodonor.mobilnumber = input("Mobile Number: ")
                            if Validate.validate_mobilnumber(elsodonor.mobilnumber):
                                break
                            else:
                                print("\n ! Használd a következö formátumot: +36701234567 or 06703216547 ! \n")
                                time.sleep(2)
                                clear()
                        clear()
                        print("Name:", elsodonor.name)
                        print("Weight:", elsodonor.weight)
                        print("Gender:", elsodonor.gender)
                        print("Date of Birth:", elsodonor.dateofbirth)
                        print("Last Donation:", elsodonor.lastdonationdate)
                        print("Was he/she sick:", elsodonor.wassick)
                        print("Unique ID:", elsodonor.uniqueid)
                        print("Blood Type:", elsodonor.bloodtype)
                        print("Expiration of ID:", elsodonor.expofid)
                        print("Email:", elsodonor.emailaddress)
                        print("Mobile Number:", elsodonor.mobilnumber)
                        input("\n -- Please hit Enter to continue -- ")
                        clear()

                        #print(Donor.parse_name(elsodonor.name))
                        #print(Donor.is_suitable(elsodonor.weight,elsodonor.lastdonationdate,elsodonor.dateofbirth))
                        #input()



















                    elif user_input=='2':
                        print("\n\n\n\n\n\n\n\n\n\t - This will be the remove donor option. It's still under construction -")
                        print("\n"*20)
                        input("Press ENTER to go BACK")
                        clear()

                    elif user_input=='3':
                        clear()
                        break

                    else:
                         raise ValueError

                except:
                    print("\n\t\t! ! !  Please choose from the given numbers.  ! ! !\t\t\n ")
                    time.sleep(1)
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
                        print("Adding new event...\n")
                        time.sleep(1)
                        clear()
                        elsoevent = Event()
                        while True:
                            elsoevent.date_of_event = input("Date of Event: ")
                            if Validate.validate_date(elsoevent.date_of_event):
                                break
                            else:
                                print("\n ! You can use this format to enter the date: 'YYYY.MM.DD' ! \n")
                                time.sleep(2)
                                clear()
                        clear()
                        while True:
                            print("Date of Event:", elsoevent.date_of_event)
                            elsoevent.start_time = input("Start Time: ")
                            if Validate.validate_time(elsoevent.start_time):
                                break
                            else:
                                print("\n ! Time format 00:00 !\n")
                                time.sleep(2)
                                clear()
                        clear()
                        while True:
                            print("Date of Event:", elsoevent.date_of_event)
                            print("Start Time:", elsoevent.start_time)
                            elsoevent.end_time = input("End Time: ")
                            if Validate.validate_time(elsoevent.end_time):
                                break
                            else:
                                print("\n ! Time format 00:00 ! \n")
                                time.sleep(2)
                                clear()
                        clear()
                        while True:
                            print("Date of Event:", elsoevent.date_of_event)
                            print("Start Time:", elsoevent.start_time)
                            print("End Time:", elsoevent.end_time)
                            elsoevent.zip_code = input("ZIP code: ")
                            if Validate.validate_zipcode(elsoevent.zip_code):
                                break
                            else:
                                print("\n ! 4 digits, that doesnt start with 0 ! \n")
                                time.sleep(2)
                                clear()
                        clear()
                        while True:
                            print("Date of Event:", elsoevent.date_of_event)
                            print("Start Time:", elsoevent.start_time)
                            print("End Time:", elsoevent.end_time)
                            print("ZIP code:", elsoevent.zip_code)
                            elsoevent.city_address = input("City: ")
                            if Validate.validate_city_name(elsoevent.city_address):
                                break
                            else:
                                print("\n ! Miskolc, Szerencs, Kazincbarckia, Sárospatak ! \n")
                                time.sleep(2)
                                clear()
                        clear()
                        while True:
                            print("Date of Event:", elsoevent.date_of_event)
                            print("Start Time:", elsoevent.start_time)
                            print("End Time:", elsoevent.end_time)
                            print("ZIP code:", elsoevent.zip_code)
                            print("City:", elsoevent.city_address)
                            elsoevent.available_beds = input("Available beds: ")
                            if Validate.validate_positive_int(elsoevent.available_beds):
                                break
                            else:
                                print("\n ! Positive number ! \n")
                                time.sleep(2)
                                clear()
                        clear()
                        while True:
                            print("Date of Event:", elsoevent.date_of_event)
                            print("Start Time:", elsoevent.start_time)
                            print("End Time:", elsoevent.end_time)
                            print("ZIP code:", elsoevent.zip_code)
                            print("City:", elsoevent.city_address)
                            print("Available beds:", elsoevent.available_beds)
                            elsoevent.planned_donor_number = input("Planned donor number: ")
                            if Validate.validate_positive_int(elsoevent.planned_donor_number):
                                break
                            else:
                                print("\n ! Positive number ! \n")
                                time.sleep(2)
                                clear()
                        clear()
                        print("Date of Event:", elsoevent.date_of_event)
                        print("Start Time:", elsoevent.start_time)
                        print("End Time:", elsoevent.end_time)
                        print("ZIP code:", elsoevent.zip_code)
                        print("City:", elsoevent.city_address)
                        print("Available beds:", elsoevent.available_beds)
                        print("Donors:", elsoevent.planned_donor_number)
                        input("\n -- Please hit Enter to continue -- ")
                        clear()




                    elif user_input=='2':
                        print("\n\n\n\n\n\n\n\n\n\t - This will be the remove donor option. It's still under construction -")
                        print("\n"*20)
                        input("Press ENTER to go BACK")
                        clear()
                    elif user_input=='3':
                        clear()
                        break
                    else:
                         raise ValueError
                except:
                    print("\n\t\t! ! !  Please choose from the given numbers.  ! ! !\t\t\n ")
                    time.sleep(1)
                    clear()

        #EXIT
        elif user_input=='3':
            clear()
            print("\n\n\n\n\n\n\t\t\t   - Thank you for using our software -\t\t\t\t")
            print("\t\t\t      - Made By the Code Stars - ")
            print("\n\n\t\t\t\t    --- GOODBYE ---")
            time.sleep(1)
            clear()
            break
        else:
            raise ValueError
    except:
        print("\n\t\t! ! !  Please choose from the given numbers.  ! ! !\t\t\n ")
        time.sleep(2)
        clear()