import numpy as np
import matplotlib.pyplot as plt

Vin = 5.0        # volts
Rref = 1000      # ohms

R_unknown = np.linspace(0, 1500, 500)   
Vout = Vin * Rref / (R_unknown + Rref)

plt.figure(figsize=(6,4))
plt.plot(R_unknown, Vout)
plt.xlabel(r'$R_?$ (Ω)')
plt.ylabel(r'$V_{out}$ (V)')
plt.title(r'Voltage Divider: $V_{out}$ vs $R_?$')
plt.grid(True)

plt.scatter(351, 3.7, color='red', label='result')
plt.legend()

plt.show()