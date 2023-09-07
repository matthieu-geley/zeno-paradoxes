"""
Le paradoxe de la Flèche:

Zénon s'imagine une flèche en mouvement.
Il dit que si le moment présent est un point, alors la flèche ne peut pas être en mouvement à ce moment précis.

On itère 20 fois et on affiche la position de la flèche à chaque itération en sachant que la flèche se déplace de 1M à chaque itération.
On remarque que la flèche n'a pas de vitesse à un moment précis T malgré qu'elle se déplace entre deux moments T différent.

"""

# Importation des modules
import os
import time

# Déclaration des variables
vitesse = 70
positionFleche = 0
iteration = 0

# Programme principal
os.system("cls")
print(f"Position de la flèche à T{iteration} = {positionFleche}M")
print()
time.sleep(1)

while iteration < 20:
    iteration += 1
    positionFleche += vitesse
    print(f"Position de la flèche à T{iteration} = {positionFleche}M")
    print()
    time.sleep(1)

# Fin du programme