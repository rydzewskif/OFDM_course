import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 30
TX_AMP = 1.5
REF_RX_DEV = 0 # deviation od receiver refertence frequency

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

Carrier = np.sin(t)
Tx = TX_AMP * Carrier

Rx = Tx # Ideal channel

Ref = np.sin(t+REF_RX_DEV)
Rx_dot_Ref  = np.dot(Rx, Ref)
RxAmpl = 2*(Rx_dot_Ref/TIME_VECTOR_SIZE) # normalisation

Error = 100 * (TX_AMP - RxAmpl)/TX_AMP

# PRESENTATION
plt.plot(t, Rx,    '-' , label='Rx  (Carrier)',     color='blue')
plt.plot(t, Ref, '--', label='RefRx',color='green')
plt.ylim(-3.1, 3.1)
plt.legend()
plt.grid()
plt.axhline(y=0,color='black')
plt.show()

print(f'TX_AMP={TX_AMP}')
print(f'REF_RX_DEV={REF_RX_DEV:0.2f}')
print(f'RxAmpl={RxAmpl:0.1f}')
print(f'Error={Error:0.1f}%')

