import numpy as np
import matplotlib.pyplot as plt

frequencies_gross = np.array([100, 200, 300, 400, 500, 700, 850, 1000, 1200, 1500, 1700, 2000, 3000, 4000, 5000, 6000, 10000]) # Hz
a_peak_gross = np.array([1.501, 1.484, 1.484, 1.506, 1.506, 1.506, 1.506, 1.506, 1.506, 1.506, 1.501, 1.501, 1.519, 1.519, 1.501, 1.519, 1.484]) # V
b_peak_gross = np.array([31.99, 109, 84.74, 59.67, 48.43, 34.58, 31.99, 33.72, 30.71, 28.98, 29.42, 28.55, 26.39, 42.39, 25.95, 25.96, 18.51]) * 1000 # V
phase_shift_gross = np.array([4550, 4138, 99.68, 239.6, 302.1, 254.3, 210.1, 188, 180.7, 199.1, 169, 161.7, 132.2, 132.4, 147.4, 127.1, 42.17]) # micro s

frequencies_klein = np.array([100, 200, 300, 400, 500, 700, 850, 1000, 1200, 1500, 1700, 2000, 3000, 4000, 5000, 6000, 10000])
a_peak_klein = np.array([1.5, 1.5, 1.5, 1.517, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.517, 1.5, 1.5, 1.5, 1.517])
b_peak_klein = np.array([12.12, 18.18, 28.57, 54.98, 82.69, 43.29, 38.1, 29.87, 25.11, 27.27, 25.98, 26.41, 32.04, 21.21, 22.08, 14.29, 16.88]) * 1000
phase_shift_klein = np.array([6888, 2147, 1166, 639.2, 31.85, 1276, 963.1, 785.4, 625.4, 482.7, 417.4, 333.7, 181.8, 98.01, 52.09, 26.32, 50.25])

plt.figure(figsize=(10, 6))
plt.plot(frequencies_gross, phase_shift_gross)
plt.title("Phasengang großer Lautsprecher")
plt.xlabel("Frequenz (Hz)")
plt.ylabel("Phase (deg)")
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(frequencies_klein, phase_shift_klein)
plt.title("Phasengang kleiner Lautsprecher")
plt.xlabel("Frequenz (Hz)")
plt.ylabel("Phase (deg)")
plt.grid()
plt.show()

phase_response_gross = phase_shift_gross * -1  * frequencies_gross * 360
phase_response_klein = phase_shift_klein * -1 * frequencies_klein * 360

amplitude_response_gross = b_peak_gross / a_peak_gross
amplitude_response_klein = b_peak_klein / a_peak_klein

plt.subplot(2, 1, 1)
plt.title("Amplitudengang")
plt.semilogx(frequencies_gross, amplitude_response_gross, label="Großer Lautsprecher")
plt.semilogx(frequencies_klein, amplitude_response_klein, label="Kleiner Lautsprecher")
plt.xlabel("Frequenz (Hz)")
plt.ylabel("dB")
plt.legend()

# Zweiter Subplot
plt.subplot(2, 1, 2)
plt.title("Phasengang")
plt.semilogx(frequencies_gross, phase_response_gross, label="Großer Lautsprecher")
plt.semilogx(frequencies_klein, phase_response_klein, label="Kleiner Lautsprecher")
plt.xlabel("Frequenz (Hz)")
plt.ylabel("Phase (deg)")

plt.tight_layout()
plt.show()

