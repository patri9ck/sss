from statistics import linear_regression

import numpy as np
import matplotlib.pyplot as plt

def get_files():
    file_list = []
    for i in range(10, 73, 3):
        file_list.append('Messungen/Versuch1-' + str(i) + 'cm.csv')
    return file_list

def comma_into_dot(x):
    return float(x.replace(',', '.'))

measured_voltage_list = np.array([1.38, 1.20, 1.07, 0.952, 0.880, 0.813, 0.757, 0.699, 0.659, 0.619, 0.617, 0.585, 0.564, 0.520, 0.506, 0.480, 0.467, 0.525, 0.466, 0.446, 0.449])
distance_list = np.arange(10, 73, 3)
voltage_list = []
std_list = []

for file in get_files():
    voltages = np.genfromtxt(file, delimiter=';', skip_header=1000, max_rows=100, dtype=float, converters={0: comma_into_dot, 1: comma_into_dot})[:, 1]

    voltage_list.append(np.mean(voltages))
    std_list.append(np.std(voltages))

plt.plot(voltage_list, distance_list, color="green")
plt.xlabel("Spannung [mV]")
plt.ylabel("Distanz [cm]")
plt.title("Mittelwerte")
plt.show()

plt.plot(measured_voltage_list, distance_list, color="blue")
plt.xlabel("Spannung [mV]")
plt.ylabel("Distanz [cm]")
plt.title("Gemessene Werte")
plt.show()

log_voltage_list = np.log(voltage_list)
log_distance_list = np.log(distance_list)

voltage_mean = np.mean(log_voltage_list)
distance_mean = np.mean(log_distance_list)

def get_gradient():
    v = log_voltage_list - voltage_mean
    d = log_distance_list - distance_mean

    return np.sum(d * v) / np.sum(np.power(v, 2))

# a
gradient = get_gradient()
# b
offset = distance_mean - (voltage_mean * gradient)

linear_regression_distance = gradient * log_voltage_list + offset

plt.plot(log_voltage_list, linear_regression_distance, color="red")
plt.xlabel("log(Spannung) [log(mV)]")
plt.ylabel("log(Distanz) [log(cm)]")
plt.title("Lineare Regression")
plt.show()

non_linear_regression_distance = np.exp(offset) * np.power(voltage_list, gradient)

plt.plot(voltage_list, non_linear_regression_distance)
plt.xlabel("Spannung [mV]")
plt.ylabel("Distanz [cm]")
plt.title("Nicht-lineare Regression")
plt.show()

width_voltage_list = np.genfromtxt("Messungen/Versuch2-Breite.csv", delimiter=';', skip_header=1000, max_rows=100, dtype=float, converters={0: comma_into_dot, 1: comma_into_dot})[:, 1]
length_voltage_list =  np.genfromtxt("Messungen/Versuch2-Laenge.csv", delimiter=';', skip_header=1000, max_rows=100, dtype=float, converters={0: comma_into_dot, 1: comma_into_dot})[:, 1]

width_voltage_std = np.std(width_voltage_list)
length_voltage_std = np.std(length_voltage_list)

print(f"s(Spannung Breite) = {width_voltage_std}")
print(f"s(Spannung Länge) = {length_voltage_std}")

width_mean = np.mean(width_voltage_list)
length_mean = np.mean(length_voltage_list)

correction_68 = 1.0
correction_95 = 1.96

width_voltage_mean_std = width_voltage_std / np.sqrt(len(width_voltage_list))
length_voltage_mean_std = length_voltage_std / np.sqrt(len(length_voltage_list))

print(f"U(Breite) = {width_mean} +/- {correction_95} * {width_voltage_mean_std} V")
print(f"(Länge) = {length_mean} +/- {correction_95} * {length_voltage_mean_std} V")

print(f"Vetrauensbereich 68% Breite: {correction_68} * {width_voltage_mean_std} = {correction_68 * width_voltage_mean_std}")
print(f"Vetrauensbereich 95% Breite: {correction_95} * {width_voltage_mean_std} = {correction_95 * width_voltage_mean_std}")
print(f"Vetrauensbereich 68% Länge: {correction_68} * {length_voltage_mean_std} = {correction_68 * length_voltage_mean_std}")
print(f"Vetrauensbereich 95% Länge: {correction_95} * {length_voltage_mean_std} = {correction_95 * length_voltage_mean_std}")

# f(x) = e^b * x^a
# f'(x) = e^b * a * x^(a-1)
width = np.exp(offset) * np.power(width_mean, gradient)
length = np.exp(offset) * np.power(length_mean, gradient)

width_error = np.exp(offset) * gradient * np.power(width_mean, gradient - 1) * width_voltage_mean_std
length_error = np.exp(offset) * gradient * np.power(length_mean, gradient - 1) * length_voltage_mean_std

print(f"w = {width} +/- {correction_95} * {width_error} cm")
print(f"l = {length} +/- {correction_95} * {length_error} cm")

# wv: width voltage
# lv: length voltage
# f(wv, lv) = e^b * wv^a * e^b * lv^a = e^(2b) * wv^a * lv^a
# df/dwv = e^(2b) * a * wv^(a-1) * lv^a
# df/dlv = e^(2b) * wv^a * a * lv^(a-1)

area = width * length

dwv = np.exp(2 * offset) * gradient * np.pow(width_mean, gradient - 1) * np.pow(length_mean, gradient)
dlv = np.exp(2 * offset) * np.pow(width_mean, gradient) * gradient * np.pow(length_mean, gradient - 1)

area_error = np.sqrt(np.pow(dwv * width_voltage_mean_std, 2) + np.pow(dlv * length_voltage_mean_std, 2))

print(f"a = {area} +/- {correction_95} * {area_error} cm^2")

