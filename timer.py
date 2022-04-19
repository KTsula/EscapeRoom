#timer.py
import time


#sets start to the current time
start = time.time()

#The time that has passed since start
timePassed= time.time()-start


while timePassed < 60:
    timer_text.clear()
    timer_text.write(int(timePassed), font("Courier", 30))

#use to paus the time while widget is active
time.sleep()