import numpy as np
import matplotlib.pyplot as plt

# Définition des paramètres de la droite
a = 5
b = 2.5

# Génération des abscisses : X
X = np.linspace(start=0.5, stop=5, num=20)

# Génération d'un bruit : noise
cte = 3
noise = cte * np.random.rand(20)

# Génération des ordonnées : Y
Y = a * X + b + noise

# Concaténation des valeurs dans une matrice : data
data = np.transpose(np.vstack((X, Y)))

# Affichage
plt.plot(X, Y, 'o')
plt.show()

# Enregistrement de data au format .npy
np.save('data', data)

# Chargement du fichier .npy
Z = np.load('data.npy')

# Affichage en ligne de console 
print(Z)
