import numpy as np
import matplotlib.pyplot as plt
from scipy import signal #required for triangle signal generation

# DATA CREATION

# definition of pi constant by using numpy library
pi = np.pi 

# time vector.
# from zero to 2pi in 30 steps
t = np.linspace(0, 3*2*pi,60, endpoint=False) #

# sinusoid
sin_a = -1.5*np.sin(t)

# triangular waveforms
trian_a = 2.5*signal.sawtooth(t,0.5)

#sum
sum_a = trian_a + sin_a

# adding waveforms to figure
plt.plot(t,sum_a,'--', label='sum', color='red')
plt.plot(t,trian_a,'-p', label='triangle', color='green')
plt.plot(t,sin_a,'p',color='blue',label = 'sinusoid')

plt.show()

# customizing figure
plt.title('Trianle + sinus')
plt.xlabel('tempus[s]')
plt.ylabel('amplitude[a.u.]')
plt.xlim(0,10)
plt.ylim(-4,6)
plt.axhline(y=0,color='orange')
plt.grid()
plt.legend()

# drawing figure
plt.show()

