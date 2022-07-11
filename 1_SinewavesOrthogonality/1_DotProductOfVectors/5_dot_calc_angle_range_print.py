from lib import rotate_vector
import numpy as np

vector = [0,1]

for angle in range(0,370,10):
   rot_vec = rotate_vector(vector,angle)
   dot = vector[0]*rot_vec[0]+vector[1]*rot_vec[1]
   print(f'{angle:03d}: {dot:+0.3f}')




