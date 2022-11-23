import os
import datetime
import time

c, b, a = input('enter the date = ').split('/')
hr, minn, sec = (input('enter the time:')).split(':')
schedule_date = datetime.date(int(a), int(b), int(c))
n = 1
while n > 0:
    if time.localtime().tm_hour == int(hr) and time.localtime().tm_min == int(minn) and time.localtime().tm_sec == int(sec) and datetime.date.today() == schedule_date:
        print('playing.....')
        os.startfile("C:\\Users\\nishant\\Desktop\\AudioCutter_yt5s.com - Hall of Fame __ Feat script __ N.C.S (128 kbps).mp3")
        break