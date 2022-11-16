import time
import os
t=int(input("please inter the time in second:"))
print(t)
time.sleep(t)
for i in range(3):
    duration=(i+1)
    freq=2500
    os.system('play -nq -t alsa synth {} sine'.format(duration,freq))
#duration = 1  # seconds
#freq = 440  # Hz

#os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))