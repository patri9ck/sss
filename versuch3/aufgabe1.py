import numpy as np
import matplotlib.pyplot as plt

filename = 'Versuch3-Oeffnung5.csv'

def comma_into_dot(x):
    return float(x.replace(',', '.'))

data = np.genfromtxt(
    filename,
    delimiter=';',
    skip_header=3,
    converters={0: comma_into_dot, 1: comma_into_dot}
)

zeit = data[:, 0]
kanal_a = data[:, 1]
zoomedZeit = zeit[100:1100]
zoomedKanalA = kanal_a[100:1100]

# Roten Balken hinzufügen
start_zeit = -22.7  # Startzeit des Balkens
end_zeit = -21   # Endzeit des Balkens

periodendauer = end_zeit - start_zeit
signal_laenge_time = zeit[-1] - zeit[0] # in (ms)
signal_laenge_samples = len(zeit)
frequenz = 1 / periodendauer
abtast_frequenz = 1 / (zeit[500] - zeit[499])

print("Signallänge M: ",signal_laenge_time, "(ms) bzw. ", signal_laenge_samples, " Samples")
print("Periodendauer P: ", periodendauer, "(ms)")
print("Frequenz f: ", frequenz, "(kHz)") # Frequenz einer Periode
print("Abtastfrequenz: ", abtast_frequenz, "(kHz)")

# Plotten der Daten
plt.figure(figsize=(10,6))
plt.plot(zoomedZeit, zoomedKanalA, label="Kanal A", color="blue")
plt.axvspan(start_zeit, end_zeit, color='red', alpha=0.2, label="Periodendauer")
plt.title("Plot von Zeit vs. Kanal A")
plt.xlabel("Zeit (ms)")
plt.ylabel("Kanal A (mV)")
plt.grid()
plt.legend()
plt.show()

# Fourier-Transformation
fft_values = np.fft.fft(kanal_a)  # Fourier-Transformation des Signals, für jede Frequenz wird ein komplexer Wert zurückgegeben
fft_magnitude = np.abs(fft_values)  # berechnet die Amplitude bzw. den Betrag des komplexen Signals
freq_axis = np.arange(0, signal_laenge_samples) / (signal_laenge_samples * ((zeit[2]-zeit[1]) / 1000))

plt.figure(figsize=(10,6))
plt.plot(freq_axis, fft_magnitude, label="Amplitudenspektrum", color="orange")
plt.title("Amplitudenspektrum")
plt.xlabel("Frequenz (Hz)")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()
plt.show()

#zoom for better visualization
freq_axis_zoom = freq_axis[0:200]
fft_magnitude_zoom = fft_magnitude[0:200]

# Find the maximum frequency and amplitude
find_max = np.argmax(fft_magnitude)
max_freq = freq_axis[find_max]
print("Grund Frequenz: ", max_freq, "Hz")
print("Maximale Amplitude: ", fft_magnitude[find_max])

plt.figure(figsize=(10,6))
plt.plot(freq_axis_zoom , fft_magnitude_zoom, label="Amplitudenspektrum", color="orange")
plt.title("Amplitudenspektrum Zoom")
plt.xlabel("Frequenz (Hz)")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()
plt.show()

#****************Aufgabe 2****************

