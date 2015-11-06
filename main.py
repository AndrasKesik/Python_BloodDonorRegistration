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
                            elsodonor.name = input("Name: ").upper()
                            if Validate.validate_name(elsodonor.name):
                                break
                            else:
                                print("\n ! Your name should have at least 2 parts and shouldn't contain special characters ! \n")
                                time.sleep(2.5)
                                clear()
                        clear()

                        while True:
                            print("Name:", elsodonor.name)
                            elsodonor.weight = input("Weight (in KG): ")
                            if Validate.validate_positive_int(elsodonor.weight):
                                break
                            else:
                                print("\n\t\t ! Your weight must be a positive number !\n")
                                time.sleep(2)
                                clear()
                        clear()
                        while True:
                            print("Name:", elsodonor.name)
                            print("Weight:", elsodonor.weight)
                            elsodonor.gender = input("Gender (M/F): ").upper()
                            if Validate.validate_gender(elsodonor.gender):
                                break
                            else:
                                print("\n\t\t ! Choose the donors gender, (M)ale or (F)emale ! \n")
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
                                print("\n\t\t ! Use this format to enter the date: 'YYYY.MM.DD' ! \n")
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
                                print("\n\t\t ! Use this format to enter the date: 'YYYY.MM.DD' ! \n")
                                time.sleep(2)
                                clear()
                        if not elsodonor.is_suitable():
                            print("\n\t - It seems your donor is not suitable for the donation. =( - ")
                            input("\n\n (Press ENTER to go BACK)")
                            clear()
                            continue
                        clear()
                        while True:
                            print("Name:", elsodonor.name)
                            print("Weight:", elsodonor.weight)
                            print("Gender:", elsodonor.gender)
                            print("Date of Birth:", elsodonor.dateofbirth)
                            print("Last Donation:", elsodonor.lastdonationdate)
                            elsodonor.wassick = input("Was he/she sick in the last month? (Y/N) ").upper()
                            if Validate.validate_sickness(elsodonor.wassick):
                                break
                            else:
                                print("\n\t\t ! Choose from the given answers: (Y)es or (N)o ! \n")
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
                            elsodonor.uniqueid = input("Unique ID: ").upper()
                            if Validate.validate_id(elsodonor.uniqueid):
                                break
                            else:
                                print("\n ! Please enter an existing ID or Passport.  6 letter/number + 2 letter/number ! \n")
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
                            elsodonor.bloodtype = input("Blood Type: ").upper()
                            if Validate.validate_blood_type(elsodonor.bloodtype):
                                break
                            else:
                                print("\n   ! It should be a real blood type. ( A+, A-, B+, B-, AB+, AB-, 0+, 0- ) ! \n")
                                time.sleep(2.5)
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
                                print("\n\t\t ! Use this format to enter the date: 'YYYY.MM.DD' ! \n")
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
                            elsodonor.emailaddress = input("Email address: ").lower()
                            if Validate.validate_email(elsodonor.emailaddress):
                                break
                            else:
                                print("\n\t ! Email should contain a @ and should end with .com or .hu ! \n")
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
                                print("\n\t\t ! Use this format: +36701234567 or 06703216547 ! \n")
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
                        print("\n\t\t - Your donor is added to the database -\n")
                        input("\n\t (Press ENTER to view the required functions)")
                        clear()
                        print("\nThe required functions: \n")
                        namelist = elsodonor.parse_name()
                        print("Parsed name in seperate objects:", namelist)

                        elsodonor.age = elsodonor.donor_age()
                        print("Age of the donor:", elsodonor.age)
                        print("Id not expired:", elsodonor.id_not_expired())
                        print("Documentum type: ", elsodonor.type_of_doc())
                        print("Hemoglobin:", elsodonor.generate_hemoglobin_level())
                        print("\n----------\n{}\n----------\n".format(elsodonor.data_out()))


                        input()
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

                except: #Exception as e:
                    #print(e)
                    print("\n\t\t! ! !  Please choose from the given numbers.  ! ! !\t\t\n ")
                    time.sleep(1.5)
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
                            if Validate.validate_date(elsoevent.date_of_event) and elsoevent.registration_in_tendays():
                                break
                            else:
                                print("\n\t ! The registration should be at least 10 days from now. ! ")
                                print("\t   ! Use this format to enter date: 'YYYY.MM.DD' ! \n")
                                time.sleep(2)
                                clear()
                        clear()
                        while True:
                            print("Date of Event:", elsoevent.date_of_event)
                            elsoevent.start_time = input("Start Time: ")
                            if Validate.validate_time(elsoevent.start_time):
                                break
                            else:
                                print("\n\t\t ! Use this time format 00:00 !\n")
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
                                print("\n\t\t ! Use this time format 00:00 ! \n")
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
                                print("\n\t ! Should be 4 digits, that doesn't start with 0 ! \n")
                                time.sleep(2)
                                clear()
                        clear()
                        while True:
                            print("Date of Event:", elsoevent.date_of_event)
                            print("Start Time:", elsoevent.start_time)
                            print("End Time:", elsoevent.end_time)
                            print("ZIP code:", elsoevent.zip_code)
                            elsoevent.city_address = input("City: ").capitalize()
                            if Validate.validate_city_name(elsoevent.city_address):
                                break
                            else:
                                print("\n\t ! Miskolc, Szerencs, Kazincbarcika, Sárospatak ! \n")
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
                                print("\n\t\t ! It should be a positive number ! \n")
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
                                print("\n\t\t ! It should be a positive number ! \n")
                                time.sleep(2)
                                clear()
                        clear()
                        print("Date of Event:", elsoevent.date_of_event)
                        print("Start Time:", elsoevent.start_time)
                        print("End Time:", elsoevent.end_time)
                        print("ZIP code:", elsoevent.zip_code)
                        print("City:", elsoevent.city_address)
                        print("Available beds:", elsoevent.available_beds)
                        print("Planned donor number:", elsoevent.planned_donor_number)

                        while True:
                            elsoevent.successfull = input("\n How many successfull donation was on the event?\n > ")
                            if Validate.validate_positive_int(elsoevent.successfull):
                                break
                            else:
                                print("\n\t\t ! It should be a positive number ! \n")
                                time.sleep(2)
                                clear()


                        print("\nThe required functions: \n")

                        print("Weekday :", elsoevent.is_weekday())
                        elsoevent.duration = elsoevent.calculate_duration()
                        print("Duration: {} min  --  {} hours ".format(elsoevent.duration,round(elsoevent.duration/60,1)))
                        print("Maximum donor number:", elsoevent.max_donor_number())
                        print("Success rate: {}".format(elsoevent.success_rate()))
                        input("\n\n (Press ENTER to go BACK)")
                        clear()


















                    elif user_input=='2':
                        print("\n\n\n\n\n\n\n\n\n\t - This will be the remove donor option. It's still under construction -")
                        print("\n"*20)
                        input("(Press ENTER to go BACK)")
                        clear()
                    elif user_input=='3':
                        clear()
                        break
                    else:
                         raise ValueError
                except Exception as e:
                    print(e)
                    print("\n\t\t! ! !  Please choose from the given numbers.  ! ! !\t\t\n ")
                    input()
                    time.sleep(1.5)
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
        time.sleep(1.5)
        clear()