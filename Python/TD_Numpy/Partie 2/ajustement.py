import matplotlib.pyplot as plt
import numpy as np

cons_list = [1.03, 1.01, 1.03, 1.05, 1.03, 1.21, 1.25, 1.22, 1.24, 1.24, 1.68, 1.66, 1.69, 1.69, 1.62, 2.19, 2.3, 2.2, 2.36, 2.12, 3.14, 3.13, 2.94, 3.25, 3.19, 3.86, 3.95, 4.09, 4.11, 4.28, 5.01, 5.01, 4.95, 5.01, 5.17, 6.91, 6.99, 6.31, 6.14, 6.17, 8.71, 8.5, 8.96, 7.75, 8.18, 10.79, 9.68, 9.93, 10.39, 10.44, 11.04, 11.49, 11.38, 11.44, 12.0, 13.41, 15.08, 13.69, 14.04, 15.07, 15.51, 15.43, 15.58, 15.54, 17.46]
cons_array = np.array(cons_list).reshape((13, 5))
speed = np.arange(5, 130, 10)
cons_mean = np.mean(cons_array, axis=1)
a, b, c = np.polyfit(speed, cons_mean, 2)
print(a, b, c)
cons_fit = a * speed**2 + b * speed + c
plt.plot(speed, cons_mean, "r+", label="Moyenne des consommations")
plt.plot(speed, cons_fit, label="Polynôme d'ordre 2 ajusté")
plt.xlabel("Vitesse (km/h)")
plt.ylabel("Consommation (L/100km)")
plt.show()