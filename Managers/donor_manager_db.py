# -*- coding: UTF-8 -*-
import os
import time
from validation import Validate
from functions import Donor
import csv
import pydoc
from operator import attrgetter
from constant_variables import *
import datetime
from msvcrt import getch
from Managers.interactive_menu_manager import MenuManager
clear = lambda: os.system('cls')
ADD_DONOR="""INSERT INTO `blooddonationstorage`.`donor`
                        (`UniqueId`,
                        `Name`,
                        `Weight`,
                        `Gender`,
                        `DateOfBirth`,
                        `LastDonationDate`,
                        `Wassick`,
                        `BloodType`,
                        `ExpofId`,
                        `Emailaddress`,
                        `Mobilnumber`,
                        `HemoglobinLevel`)
                        VALUES
                        ('{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}',
                        '{}');
                       """

class DonorManagerDB():
    @staticmethod
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

    @staticmethod
    def print_sorted_donor_list(donor_objects, input_string):
        if input_string not in ("2", "13"):
            input_donor_data_pairs = {"1": "name", "3": "gender", "4": "dateofbirth", "5": "lastdonationdate",
                                      "6": "wassick", "7": "uniqueid", "8": "expofid", "9": "bloodtype",
                                      "10": "hemoglobin", "11": "emailaddress", "12": "mobilnumber"}
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

    @staticmethod
    def add_new_donor(cursor):
        print("Adding new donor...\n")
        time.sleep(1)
        clear()

        donor_sample = Donor()
        donor_sample.name = DonorManagerDB.data_in(donor_sample, Validate.validate_name, "Name: ", NAME_ERR)
        donor_sample.weight = DonorManagerDB.data_in(donor_sample, Validate.validate_positive_int, "Weight (in KG): ", POSINT_ERR)
        donor_sample.gender = DonorManagerDB.data_in(donor_sample, Validate.validate_gender, "Gender (M/F): ", GEND_ERR)
        donor_sample.dateofbirth = DonorManagerDB.data_in(donor_sample, Validate.validate_date, "Date of Birth: ", DATE_ERR)
        donor_sample.lastdonationdate = DonorManagerDB.data_in(donor_sample, Validate.validate_date, "Last Donation: ", DATE_ERR)

        if not donor_sample.is_suitable():
            print("\n\t - It seems your donor is not suitable for the donation. =( - ")
            input("\n\n (Press ENTER to go BACK)")
            clear()
            return None

        donor_sample.wassick = DonorManagerDB.data_in(donor_sample, Validate.validate_sickness, "Was he/she sick in the last month? (Y/N) ", SICK_ERR)
        donor_sample.uniqueid = DonorManagerDB.data_in(donor_sample, Validate.validate_id, "Unique ID: ", ID_ERR)
        donor_sample.bloodtype = DonorManagerDB.data_in(donor_sample, Validate.validate_blood_type, "Blood Type: ", BTYPE_ERR)
        donor_sample.expofid = DonorManagerDB.data_in(donor_sample, Validate.validate_date, "Expiration of ID: ", DATE_ERR)
        donor_sample.emailaddress = DonorManagerDB.data_in(donor_sample, Validate.validate_email, "Email address: ", EMAIL_ERR)
        donor_sample.mobilnumber = DonorManagerDB.data_in(donor_sample, Validate.validate_mobilnumber, "Mobile Number: ", MOBILE_ERR)

        cursor.execute(ADD_DONOR.format(donor_sample.uniqueid,
                                        donor_sample.name,
                                        donor_sample.weight,
                                        donor_sample.gender,
                                        donor_sample.dateofbirth,
                                        donor_sample.lastdonationdate,
                                        donor_sample.wassick,
                                        donor_sample.bloodtype,
                                        donor_sample.expofid,
                                        donor_sample.emailaddress,
                                        donor_sample.mobilnumber,
                                        donor_sample.generate_hemoglobin_level()))



        print("\n - Your donor is added to the csv -\n\n Going back to main menu...")
        time.sleep(2.5)
        clear()

    @staticmethod
    def delete_donor(cursor):
        while True:
            try:
                cursor.execute("SELECT UniqueId FROM Donor;")
                data = cursor.fetchall()
                ids = [i[0] for i in data]
                print(ids, "(0) Cancel")
                user_input = input("Enter donor's ID or passport number: ").upper()
                if user_input == '0':
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
                    cursor.execute("DELETE FROM Donor WHERE UniqueId = '{}';".format(user_input))
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
    def list_donors(cursor):
        cursor.execute("SELECT * FROM Donor;")
        donor_list = cursor.fetchall()
        if len(donor_list) < 1:
            print("\n No entry found\n")
            input("\n Press (ENTER) to go back")
            clear()
            return None
        else:
            donor_object_list = []
            for l in donor_list:

                next_donor = Donor()
                next_donor.uniqueid = l[0]
                next_donor.name = l[1]
                next_donor.weight = str(l[2])
                next_donor.gender = l[3]
                next_donor.dateofbirth = datetime.date.strftime(l[4], "%Y.%m.%d")
                next_donor.lastdonationdate = datetime.date.strftime(l[5], "%Y.%m.%d")
                next_donor.wassick = l[6]
                next_donor.bloodtype = l[7]
                next_donor.expofid = datetime.date.strftime(l[8], "%Y.%m.%d")
                next_donor.hemoglobin = l[9]
                next_donor.emailaddress = l[-2]
                next_donor.mobilnumber = str(l[-1])
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
                DonorManagerDB.print_sorted_donor_list(donor_object_list, sort_by_input)
                return None
            elif sort_by_input == "0":
                clear()
                return None

            else:
                print("\n\t\t! ! !  Please choose from the given numbers.  ! ! !\t\t\n ")
                time.sleep(1.5)
                clear()

    @staticmethod
    def search_in_donors(cursor):
        cursor.execute("SELECT * FROM Donor;")
        data = cursor.fetchall()
        sor=""
        content=[]
        for i in data:
            sor += i[1]+","
            sor += str(i[2])+","
            sor += i[3]+","
            sor += datetime.date.strftime(i[4], "%Y.%m.%d")+","
            sor += datetime.date.strftime(i[5], "%Y.%m.%d")+","
            sor += i[6] +","
            sor += i[0] + ","
            sor += datetime.date.strftime(i[8], "%Y.%m.%d")+","
            sor += i[7]+","
            sor += str(i[11])+","
            sor += i[9] +","
            sor += i[10]
            content.append(sor)

        if len(content) < 1:
            print("\n No entry found\n")
            input("\n Press (ENTER) to go back")
            clear()
            return None
        else:
            string_to_search = input("Search for donor: ")
            found_items = []
            for donor in content:
                if string_to_search.upper() in donor:
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
            
    @staticmethod
    def change_donor_data(data_input):
        with open('Data/donors.csv', 'r') as f:
            donor_list = list(csv.reader(f))
        del(donor_list[0])

        if data_input in [i[6] for i in donor_list]:
            for i, l in enumerate(donor_list):
                if data_input == l[6]:
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
                    line_number = i

        else:
            print("Data entry doesn't exist with that ID.")
            time.sleep(1)
            return None

        input_donor_data_pairs = {0: "Name", 1: "Weight", 2: "Gender", 3: "Date of birth", 4: "Last donation date",
                                  5: "Health status in last month", 6: "ID number", 7: "Expiration of ID", 8: "Blood Type",
                                  9: "Hemoglobin", 10: "e-mail address", 11: "Mobil number"}
        which_donor_data_validation = {0: Validate.validate_name, 1: Validate.validate_positive_int, 2: Validate.validate_gender, 3: Validate.validate_date, 4: Validate.validate_date,
                                  5: Validate.validate_sickness, 6: Validate.validate_id, 7: Validate.validate_date, 8: Validate.validate_blood_type,
                                  9: Validate.validate_positive_int, 10: Validate.validate_email, 11: Validate.validate_mobilnumber}

        actv_selection = 0
        while True:
            MenuManager.change_donor_submenu(actv_selection, next_donor)

            key = ord(getch())
            if key == ESC:
                user_input = 12
                clear()
            elif key == ENTER:
                user_input = actv_selection
                clear()
            elif key == SPECIALKEYSELECTOR:
                key = ord(getch())
                if key == DOWNARROW:
                    if actv_selection < 12:
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

            if user_input in range(12):
                new = ""
                while new == "":
                    clear()
                    print(next_donor)
                    print("------------------------------\n")
                    new = input("\n(0) Cancel\nChanging {} to: ".format(input_donor_data_pairs[user_input]))
                    if new == "0":
                        return None
                    if new.upper() in [donor[6] for donor in donor_list]:
                        print("This ID number already exists! Try again.")
                        time.sleep(2)
                        break
                    if which_donor_data_validation[user_input](new):
                        with open("Data/donors.csv", "w") as f:
                            donor_list[line_number][user_input] = new.upper()
                            f.write(DONORS_ELSOSOR)
                            for line in donor_list:
                                for i in range(len(line)):
                                    f.write(line[i])
                                    if i < len(line)-1:
                                        f.write(',')
                                f.write('\n')
                        print('\n...Done!')
                        time.sleep(1)
                        break
                    else:
                        print("Wrong input")
                        new = ""
                        time.sleep(1)
            elif user_input == 12:
                clear()
                actv_selection = 0
                return None
