import time
import os

def start_beeb(sec):
    for i in range(int(sec)):
      duration=(i+1)
      freq=500
      os.system('play -nq -t alsa synth {} sine'.format(duration,freq))
def counter(t):  
    while t>0:
        mins , sec = divmod(t,60)
        timer = str(mins)+':'+str(sec)
        print(timer, end='\r')
        time.sleep(t)
        t=t-1

t=int(input("please inter the time in second:"))
counter(t)
start_beeb(3)
print("wakeup")


