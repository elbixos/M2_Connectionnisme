## Deep Mim

Essayons de créer une intelligence artificielle, basée sur des réseaux
de neurones, pour jouer au jeu des allumettes.

On commence par créer une IA sur le principe du MIN MAX.
A chaque étape, l'IA doit évaluer chacun de ses coups possibles
et choisir le meilleur.

### Accéleration par stockage des évaluations.

La procédure d'évaluation peut être grandement accélerée si l'on
conserve en mémoire les situations déja évaluées.
Dans notre cas, nous ne stockerons que les situations vues du point de vue
de l'IA qui doit jouer.

Ainsi, le plateau [0,0,0,1] est gagnant si l'IA doit jouer, et perdant si c'est l'autre joueur qui joue. Nous stockerons simplement que [0,0,0,1] est un plateau
gagnant.

En feintant un peu, on transforme ce plateau en un unique nombre.
[0,0,0,1]-> 1000
[1,2,0,7]-> 7210

Nous pouvons ainsi construire une table des évaluations avec comme clef,
ce nombre, représentant le tableau et comme valeur, l'évaluation du plateau(-1 ou 1).

#### Taille de la table d'évaluations.

Au vu de la construction des nombres,
il y a en fait très peu d'évaluations.
Vite fait :
- le plus gros chiffre vaut au maximum 7 (et est en premier).
Il y a donc 8 possibilités.
- le second plus gros vaut au maximum 5 (et est en second)
il y a donc au max 6 possibilités.
-...

Une premiere évaluation serait donc :
N= 8x6x4x2 = 384

En fait, il y en a moins car par exemple 7131 n'est pas possible.
On trouvera 7311 qui représente un plateau équivalent.

Quelques tests semblent montrer (pas eu le temps de le prouver)
qu'il n'y a en fait que 143 valeurs possibles...

### Du Réseau de Neurone la dedans.

Le réseau de neurone n'a qu'une chose à faire :
On lui donne un tableau (bien trié) : [3,1,1,0]
et il doit évaluer ceci (idéalement -1 ou 1)

C'est clairement un problème de Régression,
et il n'y a dans notre cas que 143 valeurs a apprendre à évaluer !

Commencons par créer une base de ces valeurs.

Le fichier [../Sources/saveEvaluations.py](../Sources/saveEvaluations.py) sauve
cette table en un fichier csv : [../Sources/evalMim.csv](../Sources/evalMim.csv)
