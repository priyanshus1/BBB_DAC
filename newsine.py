from math import pi,sin
import Adafruit_BBIO.PWM as PWM
#freq = 367
freq=400
omega = 2*pi*freq
sampleRate = 133333.333333
samples = int(sampleRate/freq)
pwms = [0 for _ in range(2000)]
for i in range(2000):
        pwms[i]=0
#pwms[0] = (samples+1)*4
#print pwms[0]
PWM.start("P9_14",50)
for i in range(1,samples+1):
        if i < 2000:
                pwms[i] = 50+int(50*sin(omega*(i-1)/sampleRate))

print "Frequency="+str(freq)+"\n" 
freq=float(raw_input())
PWM.set_frequency("P9_14",freq)
if freq < 67: 
        print "Frequency: "+str(freq)+" is too low. Enter a number higher than 67\n"
        freq = 67
print "Frequency="+str(freq)+"\n"
      
while True:
        if freq >=67:
                omega = 2*pi*freq;
                samples = int(sampleRate/freq);
                #pwms[0] = (samples+1)*4;
                for i in range (1,samples+1):
                        if(i < 2000):
                                pwms[i] = 50+int(50*sin(omega*(i-1)/sampleRate));
                                print pwms[i]
                                PWM.set_duty_cycle("P9_14",pwms[i])
        if freq < 67:
"newsine.py" [readonly] 42L, 1020C                                                                                                  1,1           Top

