import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.widgets import Slider

R = 0.1 #Resistance
Xl = 1  #admittace
alpha = 0  # unit in degree
Vm = 200  #Vmax
t = 0 #เวลาใดๆ
f = 50 #frequency
w = 2*math.pi*f #omega

# Create a custom time vector for the simulation (0 to 10 seconds, 1000 points)
time = np.linspace(0, 0.1, 1000)

thetaRad = math.atan(Xl / R)
alphaRad = math.radians(alpha)

Z = math.sqrt(R**2 + Xl**2)
i_ac = (Vm/Z)*np.sin(w*time + alphaRad - thetaRad)

#print("theta = ",thetaDeg)
#print("Z = ",Z)
#print("i = ",i,"A")

L = Xl/w
A = -(Vm/Z)*np.sin(w*t + alphaRad - thetaRad)
#print(A)
DcOff = A*np.exp(-(R/L)*time)
i_total = i_ac + DcOff


fig, ax = plt.subplots(figsize=(11, 6))

plt.subplots_adjust(left=0.1,bottom=0.35)

line_ac, = ax.plot(time,i_ac,label="AC Current")

line_dc, = ax.plot(time,DcOff,"--",label="DC Offset")

line_total, = ax.plot(time,i_total,linewidth=2,label="Total Current")

ax.set_title("RL Circuit")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Current (A)")

ax.grid(True)
ax.legend()

ax_R = plt.axes([
    0.15, 0.25,
    0.7, 0.03
])

slider_R = Slider(
    ax=ax_R,
    label="R (Ω)",
    valmin=0.01,
    valmax=2,
    valinit=R,
    valstep=0.01
)

ax_Xl = plt.axes([
    0.15, 0.19,
    0.7, 0.03
])

slider_Xl = Slider(
    ax=ax_Xl,
    label="Xl (Ω)",
    valmin=0.1,
    valmax=5,
    valinit=Xl,
    valstep=0.1
)

ax_Vm = plt.axes([
    0.15, 0.13,
    0.7, 0.03
])

slider_Vm = Slider(
    ax=ax_Vm,
    label="Vm (V)",
    valmin=10,
    valmax=500,
    valinit=Vm,
    valstep=10
)

ax_alpha = plt.axes([
    0.15, 0.07,
    0.7, 0.03
])

slider_alpha = Slider(
    ax=ax_alpha,
    label="Alpha (°)",
    valmin=0,
    valmax=180,
    valinit=alpha,
    valstep=1
)


def update(val):
    R = slider_R.val
    Xl = slider_Xl.val
    Vm = slider_Vm.val
    alpha = slider_alpha.val

    w = 2 * math.pi * f

    thetaRad = math.atan(Xl / R)
    thetaDeg = math.degrees(thetaRad)

    Z = math.sqrt(R**2 + Xl**2)
    L = Xl / w

    alphaRad = math.radians(alpha)

    i_ac = (Vm / Z) * np.sin(w * time + alphaRad - thetaRad)

    A = -(Vm / Z) * np.sin(alphaRad - thetaRad)
    dcOffset = A * np.exp(-(R / L) * time)
    i_total = i_ac + dcOffset

    # Update graph
    line_ac.set_ydata(i_ac)
    line_dc.set_ydata(dcOffset)
    line_total.set_ydata(i_total)

    # Update title
    ax.set_title(
        f"RL Circuit    "
        f"R={R:.2f} Ω    "
        f"XL={Xl:.2f} Ω    "
        f"Vm={Vm:.0f} V    "
        f"α={alpha:.0f}°    "
        f"θ={thetaDeg:.2f}°"
    )

    # Automatically adjust Y axis
    ax.relim()
    ax.autoscale_view()

    fig.canvas.draw_idle()

slider_R.on_changed(update)
slider_Xl.on_changed(update)
slider_Vm.on_changed(update)
slider_alpha.on_changed(update)

plt.show()