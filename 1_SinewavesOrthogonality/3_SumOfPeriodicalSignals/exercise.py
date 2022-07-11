import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
pi = np.pi

t = np.linspace(0, 3*(2*pi),100, endpoint=False)

y_sum = np.zeros(len(t)) # summaric vector filled with zeros
for i in range(3): # "3' - nr of componenets
    
    # generating random values of phase shift and amplitudes
    # rand function generates single random nr in range from 0 to 1
    phase = np.random.rand()*(2*pi) 
    ampl  = np.random.rand()
    
    # generating different waveforms 
    # select single waveform by comenting the remaining ones
    
    #y = ampl * signal.sawtooth(t+phase,0.5) #triangle
    #y = ampl * np.sign(np.sin(t+phase))     # rectangle
    y = ampl * np.sin(t+phase)

    
    plt.plot(t,y,'-')
    y_sum = y_sum + y

plt.figure(1)
plt.title('Componenets')    
plt.show()

plt.figure(2)
plt.title('Sum')    
plt.plot(t,y_sum,'-')
plt.show()

