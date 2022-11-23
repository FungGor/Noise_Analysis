import matplotlib.pyplot as plt
from matplotlib.widgets import MultiCursor
import numpy as np
import scipy
import math


time = np.arange(-10*np.pi, 10*np.pi, 0.01)
amplitude = np.sin(time)
amplitude = 16*amplitude

R1 = 20000
R2 = 1000
R4 = 10000
R5 = 95000

Rshunt = 0.01

Input_Voltage = amplitude*Rshunt

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, figsize=(50, 8))

ax1.plot(time,amplitude)
ax1.set_title('Current Amplitude')
ax1.set_xlabel('Time')
ax1.set_ylabel('Amperes (A)')

ax2.plot(time, Input_Voltage)
ax2.set_title('Voltage Drop')
ax2.set_xlabel('Time')
ax2.set_ylabel('\u0394V')

Gain = (R1/R2)*(R2/(R2+R1))*(1+(R5/R4))
OFFSET_Attenuation = (R2/(R1+R2))*(1+(R5/R4)) 
print("Gain : ", Gain)
print("OFFSET Attenuation : ",OFFSET_Attenuation)
OUTPUT_VOLTAGE = Gain*Input_Voltage + 3.3*OFFSET_Attenuation
ax3.plot(time, OUTPUT_VOLTAGE)
ax3.set_title('Output Voltage')
ax3.set_xlabel('Time')
ax3.set_ylabel('Vout')

cursor = MultiCursor(fig.canvas, (ax1, ax2, ax3), color='r',
                     lw=2, horizOn=True, vertOn=True)
                     
#plt.subplot_tool()
plt.subplots_adjust(hspace=0.6)
plt.show()