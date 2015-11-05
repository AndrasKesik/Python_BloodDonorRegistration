import datetime

today = datetime.datetime.today()
today2 = datetime.datetime.strptime("2015,02,15", "%Y,%m,%d")

starttime = datetime.datetime.strptime('10:00', '%H:%M')
endtime = datetime.datetime.strptime('18:00', '%H:%M')
duration = endtime - starttime
print((today-today2).days)
print(type((today-today2).days))

print(today2.strftime("%Y.%m.%d"))
print(type(today2.strftime("%Y.%m.%d")))