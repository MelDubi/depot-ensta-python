import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def facteur_amplification(beta, epsilon):
    return 1 / np.sqrt((1 - beta**2)**2 + 4 * epsilon**2 * beta**2)

Beta = np.linspace(0, 2*np.sqrt(2), 1000)
for epsilon in (0, 0.1, 0.2):
    plt.plot(Beta, facteur_amplification(Beta, epsilon), label=str(epsilon))

plt.plot([0, 2], [1, 1], color="black")
plt.plot([np.sqrt(2), np.sqrt(2)], [0, 8], color="black")
plt.plot([1, 1], [1, 8], color="black")

plt.legend(title=r"Valeurs de $\epsilon$")
plt.ylim(0, 8)
plt.xlim(0, np.max(Beta))
plt.xlabel(r"$\frac{\omega}{\omega_0}$")
plt.ylabel("Facteur d'amplification dynamique")

plt.text(0.2, 6, "Amplification\ndynamique")
ax = plt.gca()
p1 = patches.FancyArrowPatch((0, 5.8), (np.sqrt(2), 5.8),
                             arrowstyle='<->', mutation_scale=20)
ax.add_patch(p1)
plt.text(1.7, 6, "Atténuation\nvibratoire")
p1 = patches.FancyArrowPatch((np.sqrt(2), 5.8), (2.5, 5.8),
                             arrowstyle='<-', mutation_scale=20)
ax.add_patch(p1)

plt.annotate("Réponse statique\n"+r"sous l'effort $F_0$", xy=(0, 1),
             xytext=(0.05, 2), arrowprops=dict(arrowstyle='->'))

plt.annotate(r"$\frac{w}{w_0} = \sqrt{2}$", xy=(np.sqrt(2), 2),
             xytext=(1.6, 2.1), arrowprops=dict(arrowstyle='->'))

plt.title("Atténuation vibratoire par suspensions élastiques")
plt.show()