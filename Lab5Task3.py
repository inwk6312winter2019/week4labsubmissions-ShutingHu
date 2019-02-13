class Time():
      def _init_(self,hour,minutes,seconds):
          self.hour = 0
          self.minutes = 0
          self.seconds = 0

def print_time(time):
    if (time.hour > 24) or (time.minutes > 60) or (time.seconds > 60):
       raise ValueError('invalid Time object')
    if (time.hour < 0) or (time.minutes < 0) or (time.seconds < 0):
       raise ValueError('negative Time object') 
    print('Time is %.2d:%.2d:%.2d' %(time.hour,time.minutes,time.seconds))

time = Time()
time.hour = 9
time.minutes = 30
time.seconds = 45

print_time(time)
