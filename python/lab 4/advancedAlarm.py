import time

current_time= time.localtime()

hour= current_time.tm_hour
minute= current_time.tm_min
wday= current_time.tm_wday

if (wday>4) and (hour>=8):
    print('It is time to get up on the weekend')
    
if (wday<5) and (hour>7) or (hour==7 and minute>29):
    print('It is time to get up')

print('The time is ', hour,':',minute)


