# -*- coding: UTF-8 -*-
import os
import time
from msvcrt import getch
from colorama import init
from constant_variables import *
from csv_check import CsvChecker
from validation import Validate
from Managers.donor_manager import DonorManager
from Managers.event_manager import EventManager
from Managers.interactive_menu_manager import MenuManager
clear = lambda: os.system('cls')

#
# CSV CHECKERS
#
CsvChecker.donor_file_check()
CsvChecker.donations_file_check()

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
        DonorManager.add_new_donor()
        continue
    #
    # ADD NEW DONATION EVENT
    #
    elif user_input == MENU_ITEM_2:
        EventManager.add_new_donation_event()
        continue
    #
    # DElETE A DONOR
    #
    elif user_input == MENU_ITEM_3:
        DonorManager.delete_donor()
        continue
    #
    # DELETE DONATION EVENT
    #
    elif user_input == MENU_ITEM_4:
        EventManager.delete_donation_event()
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
                DonorManager.list_donors()
                continue
            elif user_input == 1:
                EventManager.list_donation_events()
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
                DonorManager.search_in_donors()
                continue
            elif user_input == 1:
                EventManager.search_in_donation_events()
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
                continue
            elif user_input.isdigit():
                EventManager.change_event(user_input)
                continue
            elif Validate.validate_id(user_input):
                DonorManager.change_donor_data(user_input)
                actv_selection = 0
            else:
                print(ID_ERR + "\n\t\t\t\tor\n" + POSINT_ERR)
                time.sleep(3)
                clear()
                continue
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
