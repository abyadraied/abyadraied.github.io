import pandas as pd
import matplotlib.pyplot as plt

walking_data = pd.read_csv("D:\\Trovasys\\CowTrac\\Data\\8_walking__on_head.csv", delimiter=",", names=['x_accel', 'y_accel', 'z_accel', 'x_gyro', 'y_gyro', 'z_gyro', '','',''])
still_data = pd.read_csv("D:\\Trovasys\\CowTrac\\Data\\1_still__x.csv", delimiter=",", names=['x_accel', 'y_accel', 'z_accel', 'x_gyro', 'y_gyro', 'z_gyro', '','',''])


print(walking_data['x_accel'])  
walk_xa_data = walking_data['x_accel']
walk_ya_data = walking_data['y_accel']

print(still_data['x_accel'])  
still_xa_data = still_data['x_accel']
still_ya_data = still_data['y_accel']

plt.subplot(211)
plt.plot(walk_xa_data)  
plt.plot(still_xa_data)  

plt.subplot(212)
plt.plot(walk_ya_data)  
plt.plot(still_ya_data)  
plt.show()