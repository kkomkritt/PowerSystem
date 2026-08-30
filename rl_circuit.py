import numpy as np
import matplotlib.pyplot as plt
import math

R = 0.1 #Resistance
Xl = 1  #admittace
alpha = 0  # unit in degree
Vm = 200  #Vmax
t = 0 #เวลาใดๆ
w = 2*math.pi*50 #omega

# Create a custom time vector for the simulation (0 to 10 seconds, 1000 points)
time = np.linspace(0, 0.1, 1000)

thetaRad = math.atan(Xl / R)
thetaDeg = math.degrees(thetaRad)

alphaRad = math.radians(alpha)

Z = math.sqrt(R**2 + Xl**2)
i = (Vm/Z)*np.sin(w*time + alphaRad - thetaRad)

#print("theta = ",thetaDeg)
#print("Z = ",Z)
#print("i = ",i,"A")

L = Xl/w
A = -(Vm/Z)*np.sin(w*t + alphaRad - thetaRad)
#print(A)
DcOff = A*np.exp(-(R/L)*time)
i_DcOffset = i + DcOff

plt.figure(figsize=(10,5))
plt.plot(time, DcOff,"--" ,label='Dc Offset')
plt.plot(time, i_DcOffset, label='Total current')
plt.plot(time, i,label='AC current')
plt.title('RL Circuit + DC offset')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.grid(True)
plt.legend()
plt.show()

