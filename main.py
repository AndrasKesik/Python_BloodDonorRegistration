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
                        DonorManager.list_donors()
                        continue

                    elif user_input == '1':
                        EventManager.list_donation_events()
                        continue

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
                        DonorManager.search_in_donors()
                        continue

                    elif user_input == '1':
                        EventManager.search_in_donation_events()
                        continue

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