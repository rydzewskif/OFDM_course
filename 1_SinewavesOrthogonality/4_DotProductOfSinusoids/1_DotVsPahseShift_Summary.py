
import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

t = np.linspace(0, 2*pi,30, endpoint=False)
SinRef = np.sin(t)

dot = 0
dot_list = []
phase_shift = np.linspace(0,pi,9)
for index in range(len(phase_shift)):
    SinShift = np.sin(t+phase_shift[index])
    for index in range(len(SinRef)):
        dot += SinRef[index]*SinShift[index]
    dot_list.append(dot)
    dot = 0
    
plt.figure(1)
plt.title('Dot product vs phase shift')    
plt.plot(phase_shift, dot_list,'-o',color = 'blue')
plt.axhline(y=0,color='black')
plt.xlabel('shift')
plt.ylabel('dot')
plt.grid()
plt.show()