import numpy as np
from matplotlib import pyplot as plt

MAXVOLT = 3.3

with open ("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]

with open ("settings.txt", "r") as settings:
    dT = float(settings.readline())

data_array = np.loadtxt("data.txt", dtype=int)

volt_array = data_array * MAXVOLT / 256

time_array = np.arange(0, len(volt_array) * dT, dT)
#print(data_array)
fig, ax = plt.subplots(figsize=(16, 10), dpi=400)
ax.plot(time_array, volt_array, color='purple', linewidth=3, linestyle='--')

ax.set_xlabel('TIME')  # Add an x-label to the axes.
ax.set_ylabel('VOLTAGE') 

plt.axis([min(time_array), max(time_array), min(volt_array), max(volt_array)])

plt.title("Simple Plot", fontsize = 17, wrap=True)

ax.grid(which='major', color = 'k', linewidth = 0.5)
ax.grid(which='minor', color = 'k', linestyle = '--')

str1 = "Charging time =" + str(max(time_array)) + "s" 
str2 = "Discharge time =" + (str((len(volt_array)-max(time_array)))) + "s"

plt.text(0.3, 2, str1)
plt.text(0.3, 1.5, str2)

fig.savefig("test.png")
fig.savefig("graph.svg")
