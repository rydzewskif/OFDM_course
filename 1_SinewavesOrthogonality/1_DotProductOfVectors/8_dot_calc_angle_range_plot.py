from lib import rotate_vector
import matplotlib.pyplot as plt

v = [0, 1]
angle_list = []
dot_list = []

for angle in range(0,370,10):
    angle_list.append(angle)
    v_rot = rotate_vector(v,angle)
    dot = v[0]*v_rot[0]+v[1]*v_rot[1]
    dot_list.append(dot)

plt.plot(angle_list,dot_list)

plt.xlabel("angle")
plt.ylabel("dot")

plt.grid()



