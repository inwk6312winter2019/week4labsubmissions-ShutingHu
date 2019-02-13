
import time
import datetime

class Time:
      def __init__(self,year,month,day,hour,min,sec):
          self.year = year
          self.month = month
          self.day = month
          self.hour = hour
          self.min = min
          self.sec = sec
          self.date = datetime.datetime(year,month,day,hour,min,sec)

time1 = Time(2013,1,1,8,30,20)
time2 = Time(2013,1,3,7,30,21)

def is_after(time1,time2):
    print(time1.date)
    print(time2.date)
    return time1.date > time2.date

print is_after(time1,time2)
    
