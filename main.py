# -*- coding: UTF-8 -*-
import os
import time
from validation import Validate
from functions import Donor
from functions import Event
import csv
from collections import deque
import pydoc
import datetime
from msvcrt import getch
from colorama import Fore, Back, Style, init
from operator import attrgetter
from constant_variables import *
from csv_check import CsvChecker
clear = lambda: os.system('cls')


def data_in(donor, validate, input_mess, error_mess):
    valid_input = ""
    while not valid_input:
        clear()
        if donor.name != "":
            print(donor)
        valid_input = input(input_mess)
        if validate(valid_input):
            return valid_input.upper()
        else:
            print(error_mess)
            valid_input = ""
            time.sleep(2)

def data_in_e(event, validate, input_mess, error_mess):
    valid_input = ""
    while not valid_input:
        clear()
        if event.date_of_event != "":
            print(event)
        valid_input = input(input_mess)
        if validate(valid_input):
            return valid_input.upper()
        else:
            print(error_mess)
            valid_input = ""
            time.sleep(2)


def put_string_in_quotes_if_has_comma(text):
    if ',' in text:
        return '"' + text + '"'
    else:
        return text


def event_id_generator(donations_csv):
    with open(donations_csv, 'r') as f:
        last_line_list = deque(csv.reader(f), 1)[0]
        if last_line_list[0] == "id":
            return 1
        if last_line_list and last_line_list[0].isdigit():
            return int(last_line_list[0]) + 1
        else:
            return -100


def store_donation_data():
    id_int = event_id_generator("Data/donations.csv")
    donation_sample = ""
    donation_sample += str(id_int) + "," + str(e1.date_of_event) + "," + str(e1.start_time) + "," + str(e1.end_time) + "," + \
                str(e1.zip_code) + "," + str(e1.city) + "," + put_string_in_quotes_if_has_comma(e1.address) + "," + str(e1.available_beds) + "," + \
                       str(e1.planned_donor_number) + "," + str(e1.successfull) + "\n"
    with open("Data/donations.csv", "a") as donations:
        donations.writelines(donation_sample)




def mainmenu(hol):
    clear()
    print(Style.RESET_ALL, end="")
    print(WELCOME_MESSAGE)
    menu = ['Add new donor',
            'Add new donation event',
            'Delete a donor',
            'Delete donation event',
            'List donors and donation events',
            'Search',
            'Exit']
    i = 0
    while i < hol:
        print(menu[i])
        i += 1
    print(Back.WHITE + Fore.BLACK + menu[hol])
    print(Style.RESET_ALL, end="")
    i += 1
    while i < 7:
        print(menu[i])
        i += 1
    return None


def list_submenu(hol):
    clear()
    print(Style.RESET_ALL, end="")
    print(WELCOME_MESSAGE)
    menu = ['List donors',
            'List donation events',
            'Cancel']
    i = 0
    while i < hol:
        print(menu[i])
        i += 1
    print(Back.WHITE + Fore.BLACK + menu[hol])
    print(Style.RESET_ALL, end="")
    i += 1
    while i < 3:
        print(menu[i])
        i += 1
    return None

def search_submenu(hol):
    clear()
    print(Style.RESET_ALL, end="")
    print(WELCOME_MESSAGE)
    menu = ['Search Donors',
            'Search Donations',
            'Cancel']
    i = 0
    while i < hol:
        print(menu[i])
        i += 1
    print(Back.WHITE + Fore.BLACK + menu[hol])
    print(Style.RESET_ALL, end="")
    i += 1
    while i < 3:
        print(menu[i])
        i += 1
    return None


def print_sorted_donor_list(donor_objects, input_string):
    if input_string not in ("2", "13"):
        input_donor_data_pairs = {"1": "name", "3": "gender", "4": "dateofbirth", "5": "lastdonationdate",
                                  "6": "wassick", "7": "uniqueid", "8": "expofid", "9": "bloodtype", "10": "hemoglobin",
                                  "11": "emailaddress", "12": "mobilnumber"}
        list_to_print = sorted(donor_objects, key=attrgetter(input_donor_data_pairs[input_string]))
    elif input_string == "2":
        list_to_print = sorted(donor_objects, key=lambda x: int(x.weight))
    elif input_string == "13":
        list_to_print = sorted(donor_objects, key=lambda x: int(x.age))
    text = ""
    for don in list_to_print:
        text += "------------------------------\n"
        text += don.data_out()+"\n"
    text += "------------------------------\n"
    pydoc.pager(text)
    input("\n Press (ENTER) to go back")
    clear()


def print_sorted_donation_list(event_objects, input_string):
    if input_string not in ("4", "7", "8", "9"):
        input_donation_data_pairs = {"1": "date_of_event", "2": "start_time", "3": "end_time", "5": "city", "6": "address"}
        list_to_print = sorted(event_objects, key=attrgetter(input_donation_data_pairs[input_string]))
    elif input_string == "4":
        list_to_print = sorted(event_objects, key=lambda x: int(x.zip_code))
    elif input_string == "7":
        list_to_print = sorted(event_objects, key=lambda x: int(x.available_beds))
    elif input_string == "8":
        list_to_print = sorted(event_objects, key=lambda x: int(x.planned_donor_number))
    elif input_string == "9":
        list_to_print = sorted(event_objects, key=lambda x: int(x.successfull))
    szoveg = ""
    for eve in list_to_print:
        szoveg += "------------------------------\n"
        szoveg += "ID: " + eve.id + "\n"
        szoveg += str(eve)+"\n"
    szoveg += "------------------------------\n"
    pydoc.pager(szoveg)
    input("\n Press (ENTER) to go back")
    clear()

#
# MENU POINTS
#


def add_new_donor():
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
        input("\n\n (Press ENTER to go BACK)")
        clear()
        return None

    donor_sample.wassick = data_in(donor_sample, Validate.validate_sickness, "Was he/she sick in the last month? (Y/N) ", SICK_ERR)
    donor_sample.uniqueid = data_in(donor_sample, Validate.validate_id, "Unique ID: ", ID_ERR)
    donor_sample.bloodtype = data_in(donor_sample, Validate.validate_blood_type, "Blood Type: ", BTYPE_ERR)
    donor_sample.expofid = data_in(donor_sample, Validate.validate_date, "Expiration of ID: ", DATE_ERR)
    donor_sample.emailaddress = data_in(donor_sample, Validate.validate_email, "Email address: ", EMAIL_ERR)
    donor_sample.mobilnumber = data_in(donor_sample, Validate.validate_mobilnumber, "Mobile Number: ", MOBILE_ERR )

    with open("Data/donors.csv", "a") as f:
        f.write(donor_sample.name+",")
        f.write(donor_sample.weight+",")
        f.write(donor_sample.gender+",")
        f.write(donor_sample.dateofbirth+",")
        f.write(donor_sample.lastdonationdate+",")
        f.write(donor_sample.wassick+",")
        f.write(donor_sample.uniqueid+",")
        f.write(donor_sample.expofid+",")
        f.write(donor_sample.bloodtype+",")
        f.write(donor_sample.generate_hemoglobin_level()+",")
        f.write(donor_sample.emailaddress+",")
        f.write(donor_sample.mobilnumber+"\n")

    print("\n - Your donor is added to the csv -\n\n Going back to main menu...")
    time.sleep(2.5)
    clear()

#
# DONORS.CSV CHECK
#
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

CsvChecker.donor_file_check()
CsvChecker.donations_file_check()


#MAIN MENU
clear()
holjar = 0
init()

#
# KEYPRESS MENU
#
while True:
    mainmenu(holjar)

    key = ord(getch())
    if key == ESC:
        print("\n Exiting...")
        time.sleep(1)
        user_input = 6

    elif key == ENTER:
        user_input = holjar
        clear()
    elif key == SPECIALKEYSELECTOR:
        key = ord(getch())
        if key == DOWNARROW:
            if holjar < 6:
                holjar += 1
            continue
        elif key == UPARROW:
            if holjar > 0:
                holjar -= 1
            continue
    else:
        print("\n! Wrong key !")
        time.sleep(1)
        continue

    try:
        #
        # ADD NEW DONOR
        #
        if user_input == MENU_ITEM_1:
            add_new_donor()
            continue

        #
        # ADD NEW DONATION EVENT
        #
        elif user_input == MENU_ITEM_2:
            print("Adding new event...\n")
            time.sleep(1)
            clear()
            e1 = Event()
            while True:
                e1.date_of_event = input("Date of Event: ")
                if Validate.validate_date(e1.date_of_event) and e1.registration_in_tendays():
                    pass
                else:
                    print("\n\t ! The registration should be at least 10 days from now. ! ")
                    print("\t   ! Use this format to enter date: 'YYYY.MM.DD' ! \n")
                    time.sleep(2)
                    clear()
                    continue

                e1.start_time = data_in_e(e1, Validate.validate_time, "Start Time: ", TIME_ERR)
                e1.end_time = data_in_e(e1, Validate.validate_time, "End Time: ", TIME_ERR)
                while not e1.is_starttime_before_endtime():
                    print("\n\t ! The starting time should be before the ending time. ! ")
                    time.sleep(2)
                    clear()
                    e1.end_time = ""
                    e1.end_time = data_in_e(e1, Validate.validate_time, "End Time: ", TIME_ERR)

                e1.zip_code = data_in_e(e1, Validate.validate_zipcode, "ZIP code: ", ZIP_ERR)
                e1.city = data_in_e(e1, Validate.validate_city_name, "City: ", CITY_ERR)
                e1.address = data_in_e(e1, Validate.validate_address, "Address of event: ", ADDRESS_ERR)
                e1.available_beds = data_in_e(e1, Validate.validate_positive_int, "Available beds: ", POSINT_ERR)
                e1.planned_donor_number = data_in_e(e1, Validate.validate_positive_int, "Planned donor number: ", POSINT_ERR)

                e1.successfull = data_in_e(e1, Validate.validate_positive_int, "\n How many successfull donation was on the event?\n > ",POSINT_ERR)

                print("\nThe required functions: \n")

                print("Weekday :", e1.is_weekday())
                e1.duration = e1.calculate_duration()
                print("Duration: {} min  --  {} hours ".format(e1.duration, round(e1.duration/60, 1)))
                print("Maximum donor number:", e1.max_donor_number())
                print("Success rate: {}".format(e1.success_rate()))
                input("\n\n (Press ENTER to go BACK)")
                store_donation_data()
                clear()
                break
        #
        # DElETE A DONOR
        #
        elif user_input == MENU_ITEM_3:
            while True:
                try:
                    with open("Data/donors.csv", "r") as f:
                        content=[]
                        for line in f:
                            content.append(line.strip())
                    ids = [content[i].split(',')[6] for i in range(len(content)) if i != 0]
                    print(ids, "(0) Cancel")
                    user_input = input("Enter donor's ID or passport number: ").upper()
                    if user_input=='0':
                        clear()
                        break
                    elif not Validate.validate_id(user_input):
                        print("\n\tWrong ID or Passport number, enter a real value")
                        time.sleep(2)
                        clear()
                        continue
                    elif user_input not in ids:
                        print("\n\tID is valid, but there is no entry with this ID yet.")
                        time.sleep(2)
                        clear()
                        continue
                    else:
                        print("Deleting entry...")
                        with open("Data/donors.csv", "w") as f:
                            for line in content:
                                if user_input != line.split(",")[6]:
                                    f.write(line+"\n")
                        time.sleep(1)
                    print("Done!")
                    input()
                    clear()
                    break
                except Exception as e:
                    print(e)
                    print("\n\t! ! !  Belso Error ! ! ! ")
                    input()
                    clear()
        #
        # DELETE DONATION EVENT
        #
        elif user_input == MENU_ITEM_4:
            while True:
                try:
                    with open("Data/donations.csv", "r") as f:
                        content = []
                        for line in f:
                            content.append(line.strip())
                    ids = [content[i].split(',')[0] for i in range(len(content)) if i != 0]
                    print(ids, "(0) Cancel")
                    user_input = input("Enter donation event's ID number: ")
                    if not user_input.isdigit():
                        print("\n\tWrong ID, enter a real value")
                        time.sleep(2)
                        clear()
                        continue
                    elif user_input == '0':
                        clear()
                        break
                    elif user_input not in ids:
                        print("\n\tID is valid, but there is no entry with this ID yet.")
                        time.sleep(2)
                        clear()
                        continue
                    else:
                        print("Deleting entry...")
                        with open("Data/donations.csv", "w") as f:
                            for line in content:
                                if user_input != line.split(",")[0]:
                                    f.write(line + "\n")
                        time.sleep(1)
                    print("Done!")
                    input()
                    clear()
                    break
                except Exception as e:
                    print(e)
                    print("\n\t! ! !  Belso Error ! ! ! ")
                    input()
                    clear()
        #
        # LIST DONORS AND DONATION EVENTS
        #
        elif user_input == MENU_ITEM_5:
            holjar = 0
            while True:
                list_submenu(holjar)

                key = ord(getch())
                if key == 27: #ESC
                    user_input = "3"
                    clear()
                elif key == 13: #Enter
                    user_input = str(holjar)
                    clear()
                elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
                    key = ord(getch())
                    if key == 80: #Down arrow
                        if holjar < 2:
                            holjar += 1
                        continue
                    elif key == 72: #Up arrow
                        if holjar > 0:
                            holjar -= 1
                        continue
                else:
                    print("\n! Wrong key !")
                    time.sleep(1)
                    continue


                try:
                    clear()
                    if user_input == '0':
                        with open("Data/donors.csv", "r") as f:
                            donor_list = list(csv.reader(f))
                        del(donor_list[0])
                        if len(donor_list) < 1:
                            print("\n No entry found\n")
                            input("\n Press (ENTER) to go back")
                            clear()
                            continue
                        else:
                            donor_object_list = []
                            for l in donor_list:
                                next_donor = Donor()
                                next_donor.name = l[0]
                                next_donor.weight = l[1]
                                next_donor.gender = l[2]
                                next_donor.dateofbirth = l[3]
                                next_donor.lastdonationdate = l[4]
                                next_donor.wassick = l[5]
                                next_donor.uniqueid = l[6]
                                next_donor.expofid = l[7]
                                next_donor.bloodtype = l[8]
                                next_donor.hemoglobin = l[9]
                                next_donor.emailaddress = l[-2]
                                next_donor.mobilnumber = l[-1]
                                next_donor.age = next_donor.donor_age()
                                donor_object_list.append(next_donor)

                            sort_by_input = input("Please choose the criteria by which you would like to sort the list: "
                                            "\n\n(ENTER) or (1) by name\n(2) by weight\n(3) by gender\n(4) by birth date"
                                            "\n(5) by date of last donation\n(6) by health status in last month"
                                            "\n(7) by ID or Passport number\n(8) by expiration date of ID"
                                            "\n(9) by blood type\n(10) by hemoglobin\n(11) by e-mail address"
                                            "\n(12) by mobile number\n(13) by age\n(0) Cancel\n\n> ")
                            clear()

                            if sort_by_input == "":
                                sort_by_input = "1"
                            if sort_by_input.isdigit() and int(sort_by_input) in range(1, 14):
                                print_sorted_donor_list(donor_object_list, sort_by_input)
                                continue
                            elif sort_by_input == "0":
                               clear()
                               break

                            else:
                                print("\n\t\t! ! !  Please choose from the given numbers.  ! ! !\t\t\n ")
                                time.sleep(1.5)
                                clear()

                    elif user_input == '1':
                        with open("Data/donations.csv", "r") as f:
                            event_list = list(csv.reader(f))
                        del(event_list[0])
                        if len(event_list) < 1:
                            print("\n No entry found\n")
                            input("\n Press (ENTER) to go back")
                            clear()
                            continue
                        else:
                            donation_object_list = []
                            for i in event_list:
                                next_event = Event()
                                next_event.id = i[0]
                                next_event.date_of_event = i[1]
                                next_event.start_time = i[2]
                                next_event.end_time = i[3]
                                next_event.zip_code = i[4]
                                next_event.city = i[5]
                                next_event.address = i[6]
                                next_event.available_beds = i[7]
                                next_event.planned_donor_number = i[8]
                                next_event.successfull = i[9]
                                donation_object_list.append(next_event)
                            #
                            # EVENT SORT BY MENU
                            #
                            print("Please type the criteria by which you would like to sort the list")
                            print("\n(1) Date of Event\n(2) Start Time\n(3) End Time\n(4) Zip code\n"
                                  "(5) City\n(6) Address\n(7) Available beds\n(8) Planned donor number\n"
                                  "(9) Final donor number\n(0) Cancel")
                            user_input = input("\n> ")
                            clear()

                            if user_input == "":
                                user_input = "1"
                            if user_input.isdigit() and int(user_input) in range(1, 10):
                                print_sorted_donation_list(donation_object_list, user_input)
                                continue
                            elif user_input == "0":
                                clear()
                                break
                            else:
                                print("Please choose from the given numbers")
                                time.sleep(1)
                                clear()

                    elif user_input=='2':
                        holjar=1
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
        #
        # SEARCH
        #
        elif user_input == MENU_ITEM_6:
            holjar = 0
            while True:
                search_submenu(holjar)
                key = ord(getch())
                if key == 27: #ESC
                    user_input = "3"
                    clear()
                elif key == 13: #Enter
                    user_input = str(holjar)
                    clear()
                elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
                    key = ord(getch())
                    if key == 80: #Down arrow
                        if holjar < 2:
                            holjar += 1
                        continue

                    elif key == 72: #Up arrow
                        if holjar > 0:
                            holjar -= 1
                        continue
                else:
                    print("\n! Wrong key !")
                    time.sleep(1)
                    continue

                try:

                    if user_input == '0':
                        with open("Data/donors.csv", "r") as f:
                            content = []
                            for line in f:
                                content.append(line.strip())
                        del(content[0])
                        if len(content) < 1:
                            print("\n No entry found\n")
                            input("\n Press (ENTER) to go back")
                            clear()
                            continue
                        else:
                            string_to_search = input("Search for donor: ")
                            found_items = []
                            for donor in content:
                                if string_to_search in donor:
                                    found_items.append(donor)
                            donor_object_list = []
                            for i in found_items:
                                l = i.split(",")
                                donor_object_list.append(Donor())
                                donor_object_list[-1].name = l[0]
                                donor_object_list[-1].weight = l[1]
                                donor_object_list[-1].dateofbirth = l[3]
                                donor_object_list[-1].emailaddress = l[-2]
                                donor_object_list[-1].age = donor_object_list[-1].donor_age()
                            szoveg = ""
                            for i in donor_object_list:
                                szoveg += "------------------------------\n"
                                szoveg += i.data_out()+"\n"
                            szoveg += "------------------------------\n"
                            pydoc.pager(szoveg)

                            input("\n Press (ENTER) to go back")
                            clear()

                    elif user_input == '1':
                        with open("Data/donations.csv", "r") as f:
                            content = []
                            for line in f:
                                content.append(line.strip())
                        del(content[0])
                        if len(content) < 1:
                            print("\n No entry found\n")
                            input("\n Press (ENTER) to go back")
                            clear()
                            continue
                        else:
                            string_to_search = input("Search for donations: ")
                            found_items = []
                            for donation in content:
                                if string_to_search.capitalize() in donation:
                                    found_items.append(donation)
                            eventlista = []
                            for i in found_items:
                                l = i.split(",")
                                eventlista.append(Event())
                                eventlista[-1].id = l[0]
                                eventlista[-1].date_of_event = l[1]
                                eventlista[-1].start_time = l[2]
                                eventlista[-1].end_time = l[3]
                                eventlista[-1].zip_code = l[4]
                                eventlista[-1].city = l[5]
                                eventlista[-1].address = l[6]
                                eventlista[-1].available_beds = l[7]
                                eventlista[-1].planned_donor_number = l[8]
                                eventlista[-1].successfull = l[9]

                            szoveg = ""
                            for i in eventlista:
                                szoveg += "------------------------------\n"
                                szoveg += "ID: " + i.id + "\n"
                                szoveg += str(i)+"\n"
                            szoveg += "------------------------------\n"
                            pydoc.pager(szoveg)
                            input("\n Press (ENTER) to go back")
                            clear()

                    elif user_input == '2':
                        clear()
                        holjar=1
                        break
                    else:
                         raise ValueError

                except Exception as e:
                    print(e)
                    print("\n\t\t! ! !  Please choose from the given numbers.  ! ! !\t\t\n ")
                    input()
                    time.sleep(1.5)
                    clear()
        #
        # EXIT
        #
        elif user_input == MENU_ITEM_7:
            clear()
            print("\n\n\n\n\n\n\n\n\n\n\t\t\t\t    - Thank you for using our software -\t\t\t\t")
            print("\t\t\t\t       - Made By the Code Stars - ")
            print("\n\n\t\t\t\t\t     --- GOODBYE ---")
            time.sleep(2)
            clear()
            break

        else:
            raise ValueError
    except Exception as e:
        print(e)
        print("\n\t\t! ! !  main Please choose from the given numbers.  ! ! !\t\t\n ")
        time.sleep(1.5)
        clear()