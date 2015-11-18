import datetime
import os
from collections import deque
import csv

today = datetime.datetime.today()
today2 = datetime.datetime.strptime("2015,02,15", "%Y,%m,%d")

starttime = datetime.datetime.strptime('10:00', '%H:%M')
endtime = datetime.datetime.strptime('18:00', '%H:%M')
duration = endtime - starttime
#print((today-today2).days)
#print(type((today-today2).days))

#print(today2.strftime("%Y.%m.%d"))
#print(type(today2.strftime("%Y.%m.%d")))

#print("123456ab".upper())
def event_id_generator(donations_csv):
    if not os.path.isfile(donations_csv):
        return 1
    with open(donations_csv, 'r') as f:
        last_line_list = deque(csv.reader(f), 1)[0]
        if last_line_list and last_line_list[0].isdigit():
            return int(last_line_list[0]) + 1
        else:
            return -100
        print(last_line_list)

event_id_generator("Data/donations.csv")
print(event_id_generator("Data/donations.csv"))