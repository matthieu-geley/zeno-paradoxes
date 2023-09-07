"""
Le paradoxe de la Dichotomie:

Zénon s'imagine devant un arbre imposant avec une pierre.
Il dit que si la pierre parcourt la moitié de la distance qui la sépare de l'arbre, puis la moitié de la distance restante, puis la moitié de la distance restante, etc. 
alors la pierre ne pourra jamais atteindre l'arbre.

Distance de la pierre à T0 = 0M
Distance de l'arbre à T0 = 100M

Distance de la pierre à T1 = 0M + 100/2M = 50M

Distance de la pierre à T2 = 50M + 50/2M = 75M

Distance de la pierre à T3 = 75M + 25/2M = 87.5M

On itère 20 fois et on affiche la distance de la pierre par rapport à l'arbre à chaque itération en sachant que l'arbres ne se déplace pas.

"""

# Importation des modules
import os
import time

# Déclaration des variables
distancePierre = 0
distanceArbre = 100
iteration = 0

# Programme principal
os.system("cls")
print(f"Distance de la pierre à T{iteration} = {distancePierre}M")
print(f"Distance de l'arbre à T{iteration} = {distanceArbre}M")
print()
time.sleep(1)

while iteration < 20:
    iteration += 1
    distancePierre += (distanceArbre - distancePierre) / 2
    print(f"Distance de la pierre à T{iteration} = {distancePierre}M")
    print(f"Distance de l'arbre à T{iteration} = {distanceArbre}M")
    print()
    time.sleep(1)

# Fin du programme