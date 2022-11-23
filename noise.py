import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy import signal

noise_file = 'Noise.xlsx'
data = pd.read_excel(noise_file)

time = data["Time"].values.tolist()
voltage = data["Voltage"].values.tolist()
noise = data["Noise"].values.tolist()
noise_percentage = data["Noise Percentage"].values.tolist()


Fs = 1e7
f, Pxx_spec = signal.periodogram(noise, Fs, 'flattop', scaling='spectrum')
plt.figure()
plt.semilogy(f, np.sqrt(Pxx_spec))
plt.show()
plt.ylim([1e-5, 2e-1])
plt.xlabel('frequency [Hz]')
plt.ylabel('Linear spectrum [V RMS]')