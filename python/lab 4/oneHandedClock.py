import time
current_time = time.localtime()
year= current_time.tm_year
day= current_time.tm_mday
minutes= current_time.tm_min
month= current_time.tm_mon
hour = current_time.tm_hour
print('The hour is', hour,':', minutes,'.','The date is',month,'/',day,'/',year)
