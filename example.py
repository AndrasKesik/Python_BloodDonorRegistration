import datetime

today = datetime.datetime.today()
today2 = datetime.datetime.strptime("2015,02,15", "%Y,%m,%d")

starttime = datetime.datetime.strptime('10:00', '%H:%M')
endtime = datetime.datetime.strptime('18:00', '%H:%M')
duration = endtime - starttime
print(duration)
print(type(duration))
