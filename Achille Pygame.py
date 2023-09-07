"""
Le paradoxe d'Achille et de la tortue:

Achille et une tortue font une course.
Achille est plus rapide que la tortue et lui laisse donc un handicap de 100M.

Distance de la tortue à T0 = 100M
Distance d'Achille à T0 = 0M

Pendant qu'Achille parcourt la distance qui le sépare de la tortue, la tortue parcourt une distance égale à la moitié de la distance parcouru par Achille et ainsi de suite.

Distance de la tortue à T1 = 100M + 50M = 150M
Distance d'Achille à T1 = 0M + 100M = 100M

Distance de la tortue à T2 = 150M + 25M = 175M
Distance d'Achille à T2 = 100M + 50M = 150M

Distance de la tortue à T3 = 175M + 12.5M = 187.5M
Distance d'Achille à T3 = 150M + 25M = 175M

Achille ne rattrapera jamais la tortue. Du moins, c'est ce que Zénon pense.

On itère 20 fois et on affiche la distance de la tortue par rapport à Achille à chaque itération en sachant que la tortue se déplace de la moitié de la distance parcouru par Achille.

"""

# Importation des modules
import os
import time
import pygame
from pygame.locals import *

# Déclaration des variables
handicap = 100
distanceTortue = handicap
distanceAchille = 0
iteration = 0

pygame.init()
pygame.display.set_caption("Paradoxe d'Achille et de la tortue")
X = 640
Y = 400
screen = pygame.display.set_mode((X, Y))
font = pygame.font.SysFont("Arial", 20)

texteAchille = font.render("Achille", True, (255, 0, 0))
texteTortue = font.render("Tortue", True, (0, 255, 0))

texteAchilleRect = texteAchille.get_rect()
texteTortueRect = texteTortue.get_rect()

texteAchilleRect.center = (X // 2 -180, Y // 2 - 70)
texteTortueRect.center = (X // 2 -180, Y // 2 - 30)

# Initialisation de la fenêtre

pygame.draw.line(pygame.display.get_surface(), (255, 0, 0), (X/2 - distanceAchille, 50), (X/2 + distanceAchille, 50), 15)
pygame.draw.line(pygame.display.get_surface(), (0, 255, 0), (X/2 - distanceTortue, 65), (X/2 + distanceTortue, 65), 10)

texteTortueDistance = font.render(str(distanceTortue) + "M", True, (0, 255, 0))
texteAchilleDistance = font.render(str(distanceAchille) + "M", True, (255,0 , 0))

texteAchilleDistanceRect = texteAchilleDistance.get_rect()
texteTortueDistanceRect = texteTortueDistance.get_rect()

texteTortueDistance = font.render(str(distanceTortue) + "M", True, (0, 255, 0))
texteAchilleDistance = font.render(str(distanceAchille) + "M", True, (255,0 , 0))

texteAchilleDistanceRect.center = (X // 2, Y // 2 - 70)
texteTortueDistanceRect.center = (X // 2, Y // 2 - 30)

pygame.display.get_surface().blit(texteTortueDistance, texteTortueDistanceRect)
pygame.display.get_surface().blit(texteAchilleDistance, texteAchilleDistanceRect)
pygame.display.get_surface().blit(texteAchille, texteAchilleRect)
pygame.display.get_surface().blit(texteTortue, texteTortueRect)

pygame.display.update()

# Programme principal
os.system("cls")
print("Distance d'Achille à T0 = 0M")
print(f"Distance de la tortue à T0 = {handicap}M")
print()
# time.sleep(0.5)
             
while iteration < 20:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()

    screen.fill((0, 0, 0))

    pygame.time.wait(830)

    iteration += 1
    distanceAchille = distanceTortue
    distanceTortue = handicap + distanceAchille / 2
    print("Distance d'Achille à T" + str(iteration) + " = " + str(distanceAchille) + "M")
    print("Distance de la tortue à T" + str(iteration) + " = " + str(distanceTortue) + "M")
    print()
    # time.sleep(1)
    
    pygame.draw.line(pygame.display.get_surface(), (255, 0, 0), (X/2 - distanceAchille, 50), (X/2 + distanceAchille, 50), 15)
    pygame.draw.line(pygame.display.get_surface(), (0, 255, 0), (X/2 - distanceTortue, 65), (X/2 + distanceTortue, 65), 10)
    
    
    texteTortueDistance = font.render(str(distanceTortue) + "M", True, (0, 255, 0))
    texteAchilleDistance = font.render(str(distanceAchille) + "M", True, (255,0 , 0))
    
    texteAchilleDistanceRect = texteAchilleDistance.get_rect()
    texteTortueDistanceRect = texteTortueDistance.get_rect()
    
    texteTortueDistance = font.render(str(distanceTortue) + "M", True, (0, 255, 0))
    texteAchilleDistance = font.render(str(distanceAchille) + "M", True, (255,0 , 0))
    
    texteAchilleDistanceRect.center = (X // 2, Y // 2 - 70)
    texteTortueDistanceRect.center = (X // 2, Y // 2 - 30)

    pygame.display.get_surface().blit(texteTortueDistance, texteTortueDistanceRect)
    pygame.display.get_surface().blit(texteAchilleDistance, texteAchilleDistanceRect)
    pygame.display.get_surface().blit(texteAchille, texteAchilleRect)
    pygame.display.get_surface().blit(texteTortue, texteTortueRect)



os.system("pause")

pygame.quit()

# Fin du programme