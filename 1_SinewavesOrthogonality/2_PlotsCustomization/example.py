import numpy as np
import matplotlib.pyplot as plt
from scipy import signal #required for triangle signal generation

# DATA CREATION

# definition of pi constant by using numpy library
pi = np.pi 

# time vector.
# from zero to 2pi in 30 steps
t = np.linspace(0, 3*2*pi,60, endpoint=False) #

# “simple” sinusoid
sin_a = np.sin(t)

# sinusoid with amplitude equal to 2 and time shift qual to pi/4
sin_b = 2*np.sin(t+pi/4)

# triangular waveforms
#"0.5" denotes proportion between positive and negative slope
trian_a = signal.sawtooth(t,0.5)
trian_b = 2*signal.sawtooth(t+pi/2, 0.5)
trian_c = trian_a+trian_b

# SIMPLE PLOTTING

# adding waveforms to figure
plt.plot(t,sin_a)
plt.plot(t,sin_b)

# drawing figure
plt.show()

# PLOTS CUSTOMIZATION

# adding waveforms to figure
plt.plot(t,trian_a, 'p', label='ampl=1, phase=0', color='blue')
plt.plot(t,trian_b,'-p', label='ampl=2, phase=pi/2', color='green')
plt.plot(t,trian_c,'--', label='sum', color='brown')

# customizing figure
plt.title('Trianle waveform')
plt.xlabel('time[s]')
plt.ylabel('amplitude[a.u.]')
plt.xlim(10,20)
plt.ylim(-2,4)
plt.axhline(y=0,color='red')
plt.grid()
plt.legend()

# drawing figure
plt.show()

