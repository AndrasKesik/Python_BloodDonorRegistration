# -*- coding: UTF-8 -*-
import os
from colorama import Fore, Back, Style
from constant_variables import *
clear = lambda: os.system('cls')


class MenuManager:

    @staticmethod
    def main_menu(selector):
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
        while i < selector:
            print(menu[i])
            i += 1
        print(Back.WHITE + Fore.BLACK + menu[selector])
        print(Style.RESET_ALL, end="")
        i += 1
        while i < 8:
            print(menu[i])
            i += 1
        return None

    @staticmethod
    def list_submenu(selector):
        clear()
        print(Style.RESET_ALL, end="")
        print(WELCOME_MESSAGE)
        menu = ['List donors',
                'List donation events',
                'Cancel']
        i = 0
        while i < selector:
            print(menu[i])
            i += 1
        print(Back.WHITE + Fore.BLACK + menu[selector])
        print(Style.RESET_ALL, end="")
        i += 1
        while i < 3:
            print(menu[i])
            i += 1
        return None

    @staticmethod
    def search_submenu(selector):
        clear()
        print(Style.RESET_ALL, end="")
        print(WELCOME_MESSAGE)
        menu = ['Search Donors',
                'Search Donations',
                'Cancel']
        i = 0
        while i < selector:
            print(menu[i])
            i += 1
        print(Back.WHITE + Fore.BLACK + menu[selector])
        print(Style.RESET_ALL, end="")
        i += 1
        while i < 3:
            print(menu[i])
            i += 1
        return None

    @staticmethod
    def change_event_submenu(selector, event_object):
        clear()
        print(Style.RESET_ALL, end="")
        print(event_object)
        print("------------------------------\n")
        menu = ['Date of Event',
                'Start Time',
                'End Time',
                'Zip Code',
                'City',
                'Address',
                'Available Beds',
                'Planned Donor Number',
                'Number of Successful Donations',
                'Cancel']
        i = 0
        while i < selector:
            print(menu[i])
            i += 1
        print(Back.WHITE + Fore.BLACK + menu[selector])
        print(Style.RESET_ALL, end="")
        i += 1
        while i < 10:
            print(menu[i])
            i += 1
        return None

    @staticmethod
    def change_donor_submenu(selector, donor_object):
        clear()
        print(Style.RESET_ALL, end="")
        print(donor_object)
        print("------------------------------\n")
        menu = ['Name',
                'Weight',
                'Gender',
                'Date of birth',
                'Date of last donation',
                'Health status in last month',
                'ID or Passport number',
                'Expiration of ID',
                'Blood Type',
                'Hemoglobin',
                'E-mail address',
                'Mobile number',
                'Cancel']
        i = 0
        while i < selector:
            print(menu[i])
            i += 1
        print(Back.WHITE + Fore.BLACK + menu[selector])
        print(Style.RESET_ALL, end="")
        i += 1
        while i < 13:
            print(menu[i])
            i += 1
        return None
