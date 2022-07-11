import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 30
CARRIER_TX_AMP = 1.0
INTERFER_SHIFT = pi/2+pi/8
INTERFER_AMP = 1.0

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

Carrier  = CARRIER_TX_AMP * np.sin(t) 
Interfer = INTERFER_AMP * np.sin(t+INTERFER_SHIFT)

Rx       = Carrier + Interfer
Rx_mul_Sin = Carrier * Interfer
Rx_dot_Sin  = np.dot(Carrier,Interfer)
CarrierRxAmpl = (2*Rx_dot_Sin)/(TIME_VECTOR_SIZE*INTERFER_AMP)

# PRESENTATION
plt.plot(t,Carrier,  '-' , label='Carrier',     color='blue')
plt.plot(t,Interfer, '--', label='Interfer',color='green')
plt.plot(t,Rx,       '-' , label='Rx',      color='gray', linewidth=6)
plt.ylim(-3.1, 3.1)
plt.legend()
plt.grid()
plt.axhline(y=0,color='black')
plt.show()

plt.fill_between(t,0,Rx_mul_Sin, label='Rx_mul_Sin', color='orange')
plt.ylim(-3.1, 3.1)
plt.legend()
plt.grid()
plt.axhline(y=0,color='black')
plt.show()

print(f'CARRIER_TX_AMP={CARRIER_TX_AMP}')
print(f'INTERFER_AMP={INTERFER_AMP}')
print(f'INTERFER_SHIFT={INTERFER_SHIFT:0.2f}')
print(f'Rx_dot_Sin={Rx_dot_Sin:0.1f}')
print(f'CarrierRxAmpl={CarrierRxAmpl:0.1f}')




#=========================================
#figure(figsize=(12, 6), dpi=80)

# plt.plot(modulated_signal,color='blue')
# plt.plot(carier_x_modulated,color='red')

# plt.show()

# periods = np.reshape(,[30,-1]) 


# dots.append(np.dot(sin,sin_shift))