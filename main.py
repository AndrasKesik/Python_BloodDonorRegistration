# -*- coding: UTF-8 -*-
import os
import time
import mysql.connector
from msvcrt import getch
from colorama import init
from constant_variables import *
from csv_check import CsvChecker
from validation import Validate
from Managers.donor_manager_csv import DonorManager
from Managers.donor_manager_db import DonorManagerDB
from Managers.event_manager_csv import EventManagerCSV
from Managers.event_manager_db import EventManagerDB
from Managers.interactive_menu_manager import MenuManager
clear = lambda: os.system('cls')


appconfig = r"app.config"
create_db = r"create.sql"

def config_manager(config_file):
    with open(config_file, 'r') as f:
        dict = eval(f.read())
        if dict["mode"] == "db":
            connect_dict = {}
            for i in dict["connection_string"].split(";"):
                connect_dict[i.split("=")[0]] = i.split("=")[1]
            return connect_dict
        elif dict["mode"] == "csv":
            return None

def run_sql_script(sql_file):
    with open(sql_file, 'r') as f:
        sql_data = f.read()
    actual = ""
    for i in sql_data.split('\n'):
        if not i.startswith("--"):
            actual += i
            if i.endswith(";"):
                cursor.execute(actual)
                actual = ""
    connection.commit()

connect_decider = config_manager(appconfig)
if connect_decider:
    connection = mysql.connector.connect(user=connect_decider["Uid"], host=connect_decider["Server"], password= connect_decider["Pwd"])
    cursor = connection.cursor()
    cursor.execute("SHOW DATABASES;")
    data = cursor.fetchall()
    print(data)
    input()
else:
    CsvChecker.donor_file_check()
    CsvChecker.donations_file_check()

run_sql_script(create_db)





clear()
actv_selection = 0
init()
#
# MAIN MENU
#
while True:

    MenuManager.main_menu(actv_selection)

    key = ord(getch())
    if key == ESC:
        print("\n Exiting...")
        time.sleep(1)
        user_input = 7

    elif key == ENTER:
        user_input = actv_selection
        clear()
    elif key == SPECIALKEYSELECTOR:
        key = ord(getch())
        if key == DOWNARROW:
            if actv_selection < 7:
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
    #
    # ADD NEW DONOR
    #
    if user_input == MENU_ITEM_1:
        if connect_decider:
            DonorManagerDB.add_new_donor(cursor)
            connection.commit()
        else:
            DonorManager.add_new_donor()
        continue
    #
    # ADD NEW DONATION EVENT
    #
    elif user_input == MENU_ITEM_2:
        if connect_decider:
            EventManagerDB.add_new_donation_event(cursor)
            connection.commit()
        else:
            EventManagerCSV.add_new_donation_event()
        continue
    #
    # DElETE A DONOR
    #
    elif user_input == MENU_ITEM_3:
        if connect_decider:
            DonorManagerDB.delete_donor(cursor)
            connection.commit()
        else:
            DonorManager.delete_donor()
        continue
    #
    # DELETE DONATION EVENT
    #
    elif user_input == MENU_ITEM_4:
        if connect_decider:
            EventManagerDB.delete_donation_event(cursor)
            connection.commit()
        else:
            EventManagerCSV.delete_donation_event()
    #
    # LIST DONORS AND DONATION EVENTS
    #
    elif user_input == MENU_ITEM_5:
        actv_selection = 0
        while True:
            MenuManager.list_submenu(actv_selection)

            key = ord(getch())
            if key == ESC:
                user_input = 2
                clear()
            elif key == ENTER:
                user_input = actv_selection
                clear()
            elif key == SPECIALKEYSELECTOR:
                key = ord(getch())
                if key == DOWNARROW:
                    if actv_selection < 2:
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

            clear()
            if user_input == 0:
                if connect_decider:
                    DonorManagerDB.list_donors(cursor)
                else:
                    DonorManager.list_donors()
                continue
            elif user_input == 1:
                if connect_decider:
                    EventManagerDB.list_donation_events(cursor)
                else:
                    EventManagerCSV.list_donation_events()
                continue
            elif user_input == 2:
                actv_selection = 0
                clear()
                break
    #
    # SEARCH
    #
    elif user_input == MENU_ITEM_6:
        actv_selection = 0
        while True:
            MenuManager.search_submenu(actv_selection)

            key = ord(getch())
            if key == ESC:
                user_input = 2
                clear()
            elif key == ENTER:
                user_input = actv_selection
                clear()
            elif key == SPECIALKEYSELECTOR:
                key = ord(getch())
                if key == DOWNARROW:
                    if actv_selection < 2:
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

            if user_input == 0:
                if connect_decider:
                    DonorManagerDB.search_in_donors(cursor)
                else:
                    DonorManager.search_in_donors()
                continue
            elif user_input == 1:
                if connect_decider:
                    EventManagerDB.search_in_donation_events(cursor)
                else:
                    EventManagerCSV.search_in_donation_events()
                continue
            elif user_input == 2:
                clear()
                actv_selection = 0
                break
    #
    # CHANGE DATA
    #
    elif user_input == MENU_ITEM_7:
        user_input = ""
        while user_input == "":
            user_input = input("(0) Cancel\nType ID number: ")
            user_input = user_input.upper()
            clear()
            if user_input == '0':
                break
            elif user_input.isdigit():
                if connect_decider:
                    EventManagerDB.change_event(user_input, cursor)
                    connection.commit()
                else:
                    EventManagerCSV.change_event(user_input)
                actv_selection = 0
            elif Validate.validate_id(user_input):
                if connect_decider:
                    DonorManagerDB.change_donor_data(user_input,cursor)
                    connection.commit()
                else:
                    DonorManager.change_donor_data(user_input)
                actv_selection = 0
            else:
                print(ID_ERR + "\n\t\t\t\tor\n" + POSINT_ERR)
                time.sleep(3)
                clear()
                user_input = ""
    #
    # EXIT
    #
    elif user_input == MENU_ITEM_8:
        clear()
        print("\n\n\n\n\n\n\n\n\n\n\t\t\t\t    - Thank you for using our software -\t\t\t\t")
        print("\t\t\t\t       - Made By the Code Stars - ")
        print("\n\n\t\t\t\t\t     --- GOODBYE ---")
        time.sleep(2)
        clear()
        break
