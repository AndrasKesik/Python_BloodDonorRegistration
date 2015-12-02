# -*- coding: UTF-8 -*-
import os
import time
from msvcrt import getch
from colorama import Fore, Back, Style, init
from constant_variables import *
from csv_check import CsvChecker
from Managers.donor_manager import DonorManager
from Managers.event_manager import EventManager
clear = lambda: os.system('cls')


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
            'Change data',
            'Exit']
    i = 0
    while i < hol:
        print(menu[i])
        i += 1
    print(Back.WHITE + Fore.BLACK + menu[hol])
    print(Style.RESET_ALL, end="")
    i += 1
    while i < 8:
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

#
# CSV CHECKERS
#
CsvChecker.donor_file_check()
CsvChecker.donations_file_check()



clear()
holjar = 0
init()

#
# MAIN MENU
#
while True:

    mainmenu(holjar)

    key = ord(getch())
    if key == ESC:
        print("\n Exiting...")
        time.sleep(1)
        user_input = 7

    elif key == ENTER:
        user_input = holjar
        clear()
    elif key == SPECIALKEYSELECTOR:
        key = ord(getch())
        if key == DOWNARROW:
            if holjar < 7:
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
        holjar = 0
        while True:
            list_submenu(holjar)

            key = ord(getch())
            if key == ESC:
                user_input = 2
                clear()
            elif key == ENTER:
                user_input = holjar
                clear()
            elif key == SPECIALKEYSELECTOR:
                key = ord(getch())
                if key == DOWNARROW:
                    if holjar < 2:
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
                holjar=0
                clear()
                break
    #
    # SEARCH
    #
    elif user_input == MENU_ITEM_6:
        holjar = 0
        while True:
            search_submenu(holjar)

            key = ord(getch())
            if key == ESC:
                user_input = 2
                clear()
            elif key == ENTER:
                user_input = holjar
                clear()
            elif key == SPECIALKEYSELECTOR:
                key = ord(getch())
                if key == DOWNARROW:
                    if holjar < 2:
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
                holjar = 0
                break

    elif user_input == MENU_ITEM_7:
        user_input = input("Type ID number: ")
        if user_input.isdigit():
            EventManager.change_event(user_input)
            continue
        else:
	        DonorManager.change_donor_data('852476HG')  # A string helyére jön majd a bekért ID
	        holjar = 0
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

