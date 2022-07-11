import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETER
PHASE_SHIFT = pi

# VECTORS
t = np.linspace(0, 2*pi,30, endpoint=False)
Sin_dot = []

SinRef = np.sin(t)
SinShift = np.sin(t+PHASE_SHIFT)
SinRef_mult_SinShift = SinShift * SinRef
for index in range(len(SinRef)):
    Sin_dot.append(SinRef[index]*SinShift[index])

# PLOTS

# components
plt.figure(1)
plt.title('Components')    
plt.plot(t, SinRef,'-o', label = 'SinRef')
plt.plot(t, SinShift,'-o', label = 'SinShift')
plt.axhline(y=0,color='black')
plt.grid()
plt.legend()
plt.show()
# multiplication
plt.figure(2)
plt.title('Multiplication')    
plt.stem(t, Sin_dot,markerfmt=" ")
plt.plot(t, SinRef_mult_SinShift,'o', label = 'SinRef_mult_SinShift')
plt.axhline(y=0,color='red')
plt.ylim(-1,1)
plt.grid()
plt.legend()
plt.show()
# print phase shift and dot product value
dot_sum = round(sum(Sin_dot),2)
print(f'phase_shift = pi/2 + pi')
print(f'dot_product = {dot_sum}')


    