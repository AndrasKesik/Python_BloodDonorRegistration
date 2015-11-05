# -*- coding: UTF-8 -*-
import os
import time
from validation import Validate
clear = lambda: os.system('cls')





#MAIN MENU
clear()
while True:
    print("\n\t\t\t--- WELCOME TO THE BLOOD DONATION SYSTEM ---\t\t\t")
    print("\t\t\t\t - Made By the Code Stars -\t\t\t\t\n\n")
    try:
        user_input = input("(1) Blood Donor Registration\n(2) Event Registration\n(3) EXIT\n\n> ")
        if user_input not in '123' or len(user_input)>1:
            raise ValueError
        clear()

        #BLOOD DONATION MENUPONT
        if user_input=='1':
            while True:
                print("\n\t\t\t--- WELCOME TO THE BLOOD DONATION SYSTEM ---\t\t\t")
                print("\t\t\t\t - Made By the Code Stars -\t\t\t\t\n\n")
                try:
                    user_input=input(' (1) Add New Donor\n(2) Remove Donor\n(3) Back\n\n> ')
                    if user_input not in '123' or len(user_input)>1:
                        raise ValueError
                    clear()

                    if user_input=='1':
                        print("----Adding new donor----\n")
                        elsodonor = Donor()
                        while not Validate.validate_name(elsodonor.name):
                            elsodonor.name = input("Add meg a nevet:")
                        print(elsodonor.name)
                        input()
                        clear()

                    elif user_input=='2':
                        print("----Removing donor-----\n")
                        input()
                        clear()

                    elif user_input=='3':
                        clear()
                        break

                    else:
                         raise ValueError

                except:
                    print("\n\t\t! ! !  Please choose from the given numbers.  ! ! !\t\t\n ")
                    time.sleep(2)
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
                        print("----Adding new event----\n")
                        input()
                        clear()
                    elif user_input=='2':
                        print("----Removing event-----\n")
                        input()
                        clear()
                    elif user_input=='3':
                        clear()
                        break
                    else:
                         raise ValueError
                except:
                    print("\n\t\t! ! !  Please choose from the given numbers.  ! ! !\t\t\n ")
                    time.sleep(2)
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
        time.sleep(2)
        clear()