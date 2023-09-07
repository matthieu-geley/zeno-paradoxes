# Les paradoxes de Zénon d'Élée

Zénon d'Élée est un philosophe grec du Ve siècle av. J.-C. qui a proposé plusieurs paradoxes pour démontrer que le mouvement n'existe pas. Ces paradoxes ont été résolus par l'analyse mathématique.

## Le paradoxe d'Achille et de la tortue

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

Achille ne rattrapera, théoriquement, jamais la tortue.

### Explication algorithmique

J'ai fais un script qui simule la course entre Achille et la tortue.

Le scrip itère 20 fois et à chaque itération, la tortue parcourt la moitié de la distance qui la sépare d'Achille et Achille parcourt la distance qui le sépare de la tortue.

## Le paradoxe de la Dichotomie

Zénon s'imagine devant un arbre imposant avec une pierre.
Il dit que si la pierre parcourt la moitié de la distance qui la sépare de l'arbre, puis la moitié de la distance restante, puis la moitié de la distance restante, etc.
alors la pierre ne pourra jamais atteindre l'arbre.

Distance de la pierre à T0 = 0M
Distance de l'arbre à T0 = 100M

Distance de la pierre à T1 = 0M + 100/2M = 50M

Distance de la pierre à T2 = 50M + 50/2M = 75M

Distance de la pierre à T3 = 75M + 25/2M = 87.5M

Ainsi, la distance entre la pierre et l'arbre tend vers 0 mais ne l'atteindra jamais.

### Explication algorithmique

J'ai fais un script qui simule d'une pierre qui se rapproche d'un arbre.

Le script itère 20 fois et à chaque itération, la pierre parcourt la moitié de la distance qui la sépare de l'arbre.

## Le paradoxe de la flèche

Zénon imagine une flèche qui vole dans les airs. Il dit que si l'on prend une photo de la flèche à un instant T, alors la flèche est immobile sur la photo. Donc la flèche est immobile à l'instant T.

La flèche est immobile à T0.

Elle se "déplace" entre T0 et T1.

La flèche est immobile à T1.

Ainsi, la flèche est immobile à chaque instant T. Donc la flèche est immobile tout le temps.

### Explication algorithmique

J'ai fais un script qui simule une flèche qui vole dans les airs.

Le script itère 20 fois et à chaque itération, la flèche se déplace de 70M.
