# -*- coding: UTF-8 -*-
import os
import time
from validation import Validate
from functions import Donor
from functions import Event
clear = lambda: os.system('cls')
NAME_ERR = "\n ! Your name should have at least 2 parts and shouldn't contain special characters ! \n"
POSINT_ERR = "\n\t\t ! Your weight must be a positive number !\n"
GEND_ERR = "\n\t\t ! Choose the donors gender, (M)ale or (F)emale ! \n"
DATE_ERR = "\n\t\t ! Use this format to enter the date: 'YYYY.MM.DD' ! \n"
SICK_ERR = "\n\t\t ! Choose from the given answers: (Y)es or (N)o ! \n"
ID_ERR = "\n ! Please enter an existing ID or Passport.  6 letter/number + 2 letter/number ! \n"
BTYPE_ERR = "\n   ! It should be a real blood type. ( A+, A-, B+, B-, AB+, AB-, 0+, 0- ) ! \n"
EMAIL_ERR = "\n\t ! Email should contain a @ and should end with .com or .hu ! \n"
MOBILE_ERR = "\n\t\t ! Use this format: +36701234567 or 06703216547 ! \n"

TIME_ERR = "\n\t\t ! Use this time format 00:00 !\n"
ZIP_ERR =  "\n\t ! Should be 4 digits, that doesn't start with 0 ! \n"
CITY_ERR = "\n\t ! Miskolc, Szerencs, Kazincbarcika, Sárospatak ! \n"

WELCOME_MESSAGE =  "\n\t\t\t--- WELCOME TO THE BLOOD DONATION SYSTEM ---\t\t\t" \
                     "\n\t\t\t\t - Made By the Code Stars -\t\t\t\t\n\n"


def data_in(d, validate, input_mess, error_mess):
    valid_input = ""
    while not valid_input:
        clear()
        if d.name != "":
            print(d)
        valid_input = input(input_mess)
        if validate(valid_input):
            return valid_input.upper()
        else:
            print(error_mess)
            valid_input = ""
            time.sleep(2)

def data_in_e(e, validate, input_mess, error_mess):
    valid_input = ""
    while not valid_input:
        clear()
        if e.date_of_event != "":
            print(e)
        valid_input = input(input_mess)
        if validate(valid_input):
            return valid_input.upper()
        else:
            print(error_mess)
            valid_input = ""
            time.sleep(2)

donors = []
if not os.path.isfile("Data/donors.csv"):
    with open("Data/donors.csv","w") as f:
        f.write("name,weight,gender,date_of_birth,last_donation,last_month_sickness,unique_identifier,expiration_of_id,blood_type,hemoblogin,email,mobil")
if not os.path.isfile("Data/donations.csv"):
    with open("Data/donations.csv") as f:
        f.write("id,date_of_event,start_time,end_time,zip_code,city,address,number_of_available_beds,planned_donor_number,final_donor_number")




#MAIN MENU
clear()

while True:
    print(WELCOME_MESSAGE)
    try:
        user_input = input("(1) Blood Donor Registration\n(2) Event Registration\n(3) EXIT\n\n> ")
        if user_input not in '123' or len(user_input)!=1:
            raise ValueError
        clear()

        #BLOOD DONATION MENUPONT
        if user_input=='1':
            while True:
                print(WELCOME_MESSAGE)
                try:
                    user_input=input('(1) Add New Donor\n(2) List Donors\n(3) Back\n\n> ')
                    if user_input not in '123' or len(user_input) != 1:
                        raise ValueError
                    clear()

                    if user_input=='1':
                        print("Adding new donor...\n")
                        time.sleep(1)
                        clear()

                        donor_sample = Donor()



                        donor_sample.name = data_in(donor_sample, Validate.validate_name, "Name: ", NAME_ERR)
                        donor_sample.weight = data_in(donor_sample, Validate.validate_positive_int, "Weight (in KG): ", POSINT_ERR)
                        donor_sample.gender = data_in(donor_sample, Validate.validate_gender, "Gender (M/F): ", GEND_ERR)
                        donor_sample.dateofbirth = data_in(donor_sample, Validate.validate_date, "Date of Birth: ", DATE_ERR)
                        donor_sample.lastdonationdate = data_in(donor_sample, Validate.validate_date, "Last Donation: ", DATE_ERR)

                        if not donor_sample.is_suitable():
                            print("\n\t - It seems your donor is not suitable for the donation. =( - ")
                            donors.pop()
                            input("\n\n (Press ENTER to go BACK)")
                            clear()
                            continue

                        donor_sample.wassick = data_in(donor_sample, Validate.validate_sickness, "Was he/she sick in the last month? (Y/N) ", SICK_ERR)
                        donor_sample.uniqueid = data_in(donor_sample, Validate.validate_id, "Unique ID: ", ID_ERR)
                        donor_sample.bloodtype = data_in(donor_sample, Validate.validate_blood_type, "Blood Type: ", BTYPE_ERR)
                        donor_sample.expofid = data_in(donor_sample, Validate.validate_date, "Expiration of ID: ", DATE_ERR)
                        donor_sample.emailaddress = data_in(donor_sample, Validate.validate_email, "Email address: ", EMAIL_ERR)
                        donor_sample.mobilnumber = data_in(donor_sample, Validate.validate_mobilnumber, "Mobile Number: ", MOBILE_ERR )

                        with open("Data/donors.csv", "a") as f:
                            f.write("\n"+donor_sample.name+",")
                            f.write(donor_sample.name+",")
                            f.write(donor_sample.weight+",")
                            f.write(donor_sample.gender+",")
                            f.write(donor_sample.dateofbirth+",")
                            f.write(donor_sample.lastdonationdate+",")
                            f.write(donor_sample.wassick+",")
                            f.write(donor_sample.uniqueid+",")
                            f.write(donor_sample.expofid+",")
                            f.write(donor_sample.bloodtype+",")
                            f.write("127,")    # átirni hemoglobinra
                            f.write(donor_sample.emailaddress+",")
                            f.write(donor_sample.mobilnumber+",")

                        print("\n\t\t - Your donor is added to the database -\n")
                        input("\n\t (Press ENTER to go BACK)")
                        clear()

                    elif user_input=='2':
                        if len(donors)>0:
                            for i in range(len(donors)):
                                print(donors[i])
                                print("\n\nThe required functions: \n")
                                namelist = donors[i].parse_name()
                                print("Parsed name in seperate objects:", namelist)

                                donors[i].age = donors[i].donor_age()
                                print("Age of the donor:", donors[i].age)
                                print("Id not expired:", donors[i].id_not_expired())
                                print("Documentum type: ", donors[i].type_of_doc())
                                print("Hemoglobin:", donors[i].generate_hemoglobin_level())
                                print("\n----------\n{}\n----------\n".format(donors[i].data_out()))
                                input("\n\n\n >>> Press ENTER to see the next entry <<< ")
                                clear()
                        else:
                            print("\n\n\n\t - NO DONORS ADDED YET -")
                            time.sleep(2)

                        clear()

                    elif user_input=='3':
                        clear()
                        break

                    else:
                         raise ValueError

                except Exception as e:
                    print(e)
                    print("\n\t\t! ! !  Please choose from the given numbers.  ! ! !\t\t\n ")
                    time.sleep(1.5)
                    clear()

        #EVENT REGISTER MENUPONT
        elif user_input=='2':
            while True:
                print(WELCOME_MESSAGE)
                try:
                    user_input=input('(1) Add New Event\n(2) Remove Event\n(3) Back\n\n> ')
                    clear()
                    if user_input=='1':
                        print("Adding new event...\n")
                        time.sleep(1)
                        clear()
                        e1 = Event()
                        while True:
                            e1.date_of_event = input("Date of Event: ")
                            if Validate.validate_date(e1.date_of_event) and e1.registration_in_tendays():
                                break
                            else:
                                print("\n\t ! The registration should be at least 10 days from now. ! ")
                                print("\t   ! Use this format to enter date: 'YYYY.MM.DD' ! \n")
                                time.sleep(2)
                                clear()

                        e1.start_time = data_in_e(e1, Validate.validate_time, "Start Time: ", TIME_ERR)
                        e1.end_time = data_in_e(e1, Validate.validate_time, "End Time: ", TIME_ERR)
                        e1.zip_code = data_in_e(e1, Validate.validate_zipcode, "ZIP code: ", ZIP_ERR)
                        e1.city_address = data_in_e(e1, Validate.validate_city_name, "City: ", CITY_ERR)
                        e1.available_beds = data_in_e(e1, Validate.validate_positive_int, "Available beds: ", POSINT_ERR)
                        e1.planned_donor_number = data_in_e(e1, Validate.validate_positive_int, "Planned donor number: ", POSINT_ERR)

                        e1.successfull = data_in_e(e1, Validate.validate_positive_int, "\n How many successfull donation was on the event?\n > ",POSINT_ERR)

                        print("\nThe required functions: \n")

                        print("Weekday :", e1.is_weekday())
                        e1.duration = e1.calculate_duration()
                        print("Duration: {} min  --  {} hours ".format(e1.duration,round(e1.duration/60,1)))
                        print("Maximum donor number:", e1.max_donor_number())
                        print("Success rate: {}".format(e1.success_rate()))
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