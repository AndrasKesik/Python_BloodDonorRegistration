# -*- coding: UTF-8 -*-
import os
from colorama import Fore, Back, Style
from constant_variables import *
clear = lambda: os.system('cls')


class InteractiveMenuManager:

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
