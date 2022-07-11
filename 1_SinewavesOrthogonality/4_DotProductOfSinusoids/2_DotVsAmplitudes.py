import numpy as np
pi = np.pi

# PARAMS
TIME_VECTOR_SIZE = 30

AMP_A = 1
AMP_B = 2

# CALCULATIONS
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

Sin_A = AMP_A * np.sin(t)
Sin_B = AMP_B * np.sin(t)
dot = np.dot(Sin_A,Sin_B)


# PRESENTATION
print(f'AMP_A = {AMP_A}')
print(f'AMP_B = {AMP_B}')
print(f'dot = {dot:0.2f}')



