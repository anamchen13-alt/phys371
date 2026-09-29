import numpy as np 
import matplotlib.pyplot as plt 

path = '/users/anamc/fw2026/phys371/lab2data2.csv' 
data = np.genfromtxt(path, delimiter=',', names=['time', 'adc'])

time = (data['time']-50000)*0.001
adc = data['adc']

Rref = 1000 #ohms
Vout= (adc/1023) * 5 
Rt = Rref*((1023-adc)/adc)
# print(Vout)
## print(Rt)
R25 = 3300 #ohms 

#  B_25/85 =3997
A, B, C, D = 3.354016e-03, 2.569850e-04, 2.620131e-06, 6.383091e-08

def temperature_K(Rt):
    x = np.log(Rt/R25)
    return 1.0 / (A + B*x + C*x**2 + D*x**3)

T = temperature_K(Rt)

plt.figure(figsize=(6,4))
plt.scatter(time, T, s = 4, color='blue')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.title('Temperature vs Time')
plt.grid(True)


plt.show()