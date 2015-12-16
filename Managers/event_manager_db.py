# -*- coding: UTF-8 -*-
import os
import time
from datetime import datetime
from datetime import date
from validation import Validate
from functions import Event
import csv
from collections import deque
import pydoc
from operator import attrgetter
from constant_variables import *
from msvcrt import getch
from Managers.interactive_menu_manager import MenuManager
clear = lambda: os.system('cls')

STORE_EVENT_IN_SQLDB = """INSERT INTO `blooddonationstorage`.`event` (`DateOfEvent`, `StartTime`, `EndTime`,
`ZipCode`, `City`, `Address`, `AvailableBeds`, `PlannedDonorNumber`, `Successfull`)
VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');"""
QUERY_EVENT_IDS_FROM_SQLDB = """SELECT `Id` FROM `blooddonationstorage`.`event`;"""
QUERY_EVENTS_FROM_SQLDB = """SELECT * FROM `blooddonationstorage`.`event`;"""
DELETE_ROW_IN_SQLDB = """DELETE FROM `blooddonationstorage`.`event` WHERE Id='{}';"""


class EventManagerDB:
    @staticmethod
    def data_into_event_object(event_obj, validate, input_msg, error_msg):
        valid_input = ""
        while not valid_input:
            clear()
            if event_obj.date_of_event != "":
                print(event_obj)
            valid_input = input(input_msg)
            if validate(valid_input):
                return valid_input.upper()
            else:
                print(error_msg)
                valid_input = ""
                time.sleep(2)

    @staticmethod
    def store_donation_data(donation_object, cursor_obj):
        cursor_obj.execute(STORE_EVENT_IN_SQLDB.format(datetime.strptime(donation_object.date_of_event, '%Y.%m.%d'),
                                                       datetime.strptime(donation_object.start_time, '%H:%M'),
                                                       datetime.strptime(donation_object.end_time, '%H:%M'),
                                                       donation_object.zip_code, donation_object.city,
                                                       donation_object.address, donation_object.available_beds,
                                                       donation_object.planned_donor_number, donation_object.successfull))

    @staticmethod
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

    @staticmethod
    def add_new_donation_event(cursor_object):
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

            e1.start_time = EventManagerDB.data_into_event_object(e1, Validate.validate_time, "Start Time: ", TIME_ERR)
            e1.end_time = EventManagerDB.data_into_event_object(e1, Validate.validate_time, "End Time: ", TIME_ERR)
            while not e1.is_starttime_before_endtime():
                print("\n\t ! The starting time should be before the ending time. ! ")
                time.sleep(2)
                clear()
                e1.end_time = ""
                e1.end_time = EventManagerDB.data_into_event_object(e1, Validate.validate_time, "End Time: ", TIME_ERR)

            e1.zip_code = EventManagerDB.data_into_event_object(e1, Validate.validate_zipcode, "ZIP code: ", ZIP_ERR)
            e1.city = EventManagerDB.data_into_event_object(e1, Validate.validate_city_name, "City: ", CITY_ERR)
            e1.address = EventManagerDB.data_into_event_object(e1, Validate.validate_address, "Address of event: ", ADDRESS_ERR)
            e1.available_beds = EventManagerDB.data_into_event_object(e1, Validate.validate_positive_int, "Available beds: ", POSINT_ERR)
            e1.planned_donor_number = EventManagerDB.data_into_event_object(e1, Validate.validate_positive_int, "Planned donor number: ", POSINT_ERR)

            e1.successfull = EventManagerDB.data_into_event_object(e1, Validate.validate_positive_int, "\n How many successfull donation was on the event?\n > ", POSINT_ERR)

            print("\nThe required functions: \n")

            print("Weekday :", e1.is_weekday())
            e1.duration = e1.calculate_duration()
            print("Duration: {} min  --  {} hours ".format(e1.duration, round(e1.duration/60, 1)))
            print("Maximum donor number:", e1.max_donor_number())
            print("Success rate: {}".format(e1.success_rate()))
            input("\n\n (Press ENTER to go BACK)")
            EventManagerDB.store_donation_data(e1, cursor_object)
            clear()
            break

    @staticmethod
    def delete_donation_event(cursor_object):
        while True:
            try:
                cursor_object.execute(QUERY_EVENT_IDS_FROM_SQLDB)
                ids = [tupl[0] for tupl in cursor_object.fetchall()]
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
                elif int(user_input) not in ids:
                    print("\n\tID is valid, but there is no entry with this ID yet.")
                    time.sleep(2)
                    clear()
                    continue
                else:
                    print("Deleting entry...")
                    cursor_object.execute(DELETE_ROW_IN_SQLDB.format(int(user_input)))
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

    @staticmethod
    def list_donation_events(cursor_object):
        cursor_object.execute(QUERY_EVENTS_FROM_SQLDB)
        event_list = cursor_object.fetchall()
        if len(event_list) < 1:
            print("\n No entry found\n")
            input("\n Press (ENTER) to go back")
            clear()
            return None
        else:
            donation_object_list = []
            for entry in event_list:
                next_event = Event()
                next_event.id = str(entry[0])
                next_event.date_of_event = entry[1].strftime('%Y.%m.%d')
                delta_to_time_obj = (datetime.min + entry[2]).time()
                next_event.start_time = delta_to_time_obj.strftime('%H:%M')
                delta_to_time_obj2 = (datetime.min + entry[3]).time()
                next_event.end_time = delta_to_time_obj2.strftime('%H:%M')
                next_event.zip_code = str(entry[4])
                next_event.city = entry[5]
                next_event.address = entry[6]
                next_event.available_beds = str(entry[7])
                next_event.planned_donor_number = str(entry[8])
                next_event.successfull = str(entry[9])
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
                EventManagerDB.print_sorted_donation_list(donation_object_list, user_input)
                return None
            elif user_input == "0":
                clear()
                return None
            else:
                print("Please choose from the given numbers")
                time.sleep(1)
                clear()

    @staticmethod
    def search_in_donation_events(cursor_object):
        cursor_object.execute(QUERY_EVENTS_FROM_SQLDB)
        content = cursor_object.fetchall()
        if len(content) < 1:
            print("\n No entry found\n")
            input("\n Press (ENTER) to go back")
            clear()
            return None
        else:
            string_to_search = input("Search for donations: ")
            found_items = []
            for donation in content:
                for data in donation:
                    if string_to_search.capitalize() in str(data) or string_to_search.upper() in str(data):
                        found_items.append(donation)
                        break
            eventlista = []
            for found_donation in found_items:
                eventlista.append(Event())
                eventlista[-1].id = str(found_donation[0])
                eventlista[-1].date_of_event = found_donation[1].strftime('%Y.%m.%d')
                delta_to_time_obj = (datetime.min + found_donation[2]).time()
                eventlista[-1].start_time = delta_to_time_obj.strftime('%H:%M')
                delta_to_time_obj2 = (datetime.min + found_donation[3]).time()
                eventlista[-1].end_time = delta_to_time_obj2.strftime('%H:%M')
                eventlista[-1].zip_code = str(found_donation[4])
                eventlista[-1].city = found_donation[5]
                eventlista[-1].address = found_donation[6]
                eventlista[-1].available_beds = str(found_donation[7])
                eventlista[-1].planned_donor_number = str(found_donation[8])
                eventlista[-1].successfull = str(found_donation[9])

            szoveg = ""
            for i in eventlista:
                szoveg += "------------------------------\n"
                szoveg += "ID: " + i.id + "\n"
                szoveg += str(i)+"\n"
            szoveg += "------------------------------\n"
            pydoc.pager(szoveg)
            input("\n Press (ENTER) to go back")
            clear()

    @staticmethod
    def change_event(input_id_string, cursor_object):
        event_to_change = []
        cursor_object.execute(QUERY_EVENTS_FROM_SQLDB)
        event_list = cursor_object.fetchall()
        for event in event_list:
            if int(input_id_string) == event[0]:
                event_to_change = list(event)
        if not event_to_change:
            print("\n No entry found with this ID.\n")
            time.sleep(1)
            clear()
            return None

        input_object_data_pairs = {
            0: "DateOfEvent", 1: "StartTime", 2: "EndTime", 3: "ZipCode", 4: "City", 5: "Address",
            6: "AvailableBeds", 7: "PlannedDonorNumber", 8: "Successfull"
        }
        validators_for_data_to_change = {
            0: Validate.validate_date, 1: Validate.validate_time, 2: Validate.validate_time,
            3: Validate.validate_zipcode, 4: Validate.validate_city_name, 5: Validate.validate_address,
            6: Validate.validate_positive_int, 7: Validate.validate_positive_int,
            8: Validate.validate_positive_int
        }
        event_object_for_printing = Event()
        event_object_for_printing.id = str(event_to_change[0])
        event_object_for_printing.date_of_event = event_to_change[1].strftime('%Y.%m.%d')
        delta_to_time_obj = (datetime.min + event_to_change[2]).time()
        event_object_for_printing.start_time = delta_to_time_obj.strftime('%H:%M')
        delta_to_time_obj2 = (datetime.min + event_to_change[3]).time()
        event_object_for_printing.end_time = delta_to_time_obj2.strftime('%H:%M')
        event_object_for_printing.zip_code = str(event_to_change[4])
        event_object_for_printing.city = event_to_change[5]
        event_object_for_printing.address = event_to_change[6]
        event_object_for_printing.available_beds = str(event_to_change[7])
        event_object_for_printing.planned_donor_number = str(event_to_change[8])
        event_object_for_printing.successfull = str(event_to_change[9])

        actv_selection = 0
        while True:
            MenuManager.change_event_submenu(actv_selection, event_object_for_printing)

            key = ord(getch())
            if key == ESC:
                user_input = 9
                clear()
            elif key == ENTER:
                user_input = actv_selection
                clear()
            elif key == SPECIALKEYSELECTOR:
                key = ord(getch())
                if key == DOWNARROW:
                    if actv_selection < 9:
                        actv_selection += 1
                    continue
                elif key == UPARROW:
                    if actv_selection > 0:
                        actv_selection -= 1
                    continue
                else:
                    print("\n! Wrong key !")
                    time.sleep(1)
                    continue
            else:
                print("\n! Wrong key !")
                time.sleep(1)
                continue

            if user_input in range(9):
                data_to_change = ""
                while data_to_change == "":
                    print(event_object_for_printing)
                    print("------------------------------\n")
                    print("\n(0) Cancel\nChanging {} to: ".format(input_object_data_pairs[user_input]))
                    data_to_change = input("\n> ")
                    data_to_change = data_to_change.upper()
                    if data_to_change == "0":
                        return None
                    elif validators_for_data_to_change[user_input](data_to_change):
                        CHANGE_DATA = "UPDATE event SET {} = '{}' WHERE Id = {}".format(input_object_data_pairs[user_input], data_to_change, event_object_for_printing.id)
                        cursor_object.execute(CHANGE_DATA)
                        clear()
                        print("...Done!")
                        time.sleep(1)
                        return None
                    else:
                        print("Wrong {}.".format(input_object_data_pairs[user_input]))
                        data_to_change = ""
                        time.sleep(1)
                        clear()
            elif user_input == 9:
                clear()
                actv_selection = 0
                return None
