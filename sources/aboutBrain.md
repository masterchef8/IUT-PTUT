# Multilayer perceptron 

Ce fichier est destiné à définir les différentes variables du MLP et comment on va introduire les données à l'interieur. 

Pour rappel, nous utilisons Hyperopt pour trouver les meilleurs méta-paramètres possibles pour notre réseau. cf (wiki de git.rabian.fr)

## Bref récapitulatif de ce qu'est un réseau de neurone MLP
Le Perceptron multicouche est un Classifieur linéaire de type réseau neuronal formel organisé en plusieurs couches au sein desquelles une information circule de la couche d'entrée vers la couche de sortie uniquement ; il s'agit donc d'un réseau de type feedforward (en). Chaque couche est constituée d'un nombre variable de neurones, les neurones de la couche de sortie correspondant toujours aux sorties du système.

## Algorithme de backpropagation du gradient de l'erreur 

- Présentation d'un motif d'entraînement au réseau.
- Comparaison de la sortie du réseau avec la sortie ciblée.
- Calcul de l'erreur en sortie de chacun des neurones du réseau.
- Calcul, pour chacun des neurones, de la valeur de sortie qui aurait été correcte.
- Définition de l'augmentation ou de la diminution nécessaire pour obtenir cette valeur (erreur locale).
- Ajustement du poids de chaque connexion vers l'erreur locale la plus faible.
- Attribution d'un blâme à tous les neurones précédents.
- Recommencer à partir de l'étape 4, sur les neurones précédent en utilisant le blâme comme erreur.

## Les variables de notre réseau 

```python 
# Number of neuron in Input, Hidden and output layer.

LI = 20
LH = 20
LO = 5
ITERATIONS = 2000 # Number of iterations during training step.
PAS = 0.3 
MOMENTUM = 0.1
```

Le nombre de neurones en entrée sera fixé à 24 (cf section d'après).
Le nombre de neurones en couche cachée reste à déterminer.
Le nombre de neurones en couche de sortie reste à déterminer. Il dépendra de 

la sortie que nous souhaitons avoir. Un seul neurone en sortie me semble correct car nous voulons un indice en sortie. Nous pouvons aussi coder cette indice sur 8 bit, donc 8 neurones et ainsi de suite. 

Le nombre d'itérations correspond au nombre de fois que nous exécuter un passage dans le réseau de neurone avec application de la backpropagation.
Cette valeur sera fixé par HyperOpt. 

Le PAS correspond à la valeur qui sera appliquer par addition ou soustraction aux poids des connexions dans le réseau de neurones. Si une connexion entre deux neurones correspond à la sortie attendu, le poids de cette connexion sera augmentée (0.1 dans l'exemple) et inversement si elle cause une erreur. C'est l'algorithme de backpropagation qui se charge de décider il faut augmenter ou diminuer le poids de la connexion entre deux neurones. 

Pour éviter les problèmes liés à une stabilisation dans un minimum local, on ajoute un terme d'inertie (momentum). Celui-ci permet de sortir des minimums locaux dans la mesure du possible et de poursuivre la descente de la fonction d'erreur. À chaque itération, le changement de poids conserve les informations des changements précédents. Cet effet de mémoire permet d'éviter les oscillations et accélère l'optimisation du réseau. Par rapport à la formule de modification des poids présentée auparavant, le changement des poids avec inertie au temps t se traduit par une formule que je ne peux pas affichier en md gfm.

Les variables PAS et MOMENTUM peuvent être changées selon vos besoins, elles doivent cependant en général rester inférieures à 1.0.

### Comment allons nous fiter les données ?

les écologues veulent une précision la plus fine possible pour la reconnaissance des lacs. Le problème, les lacs ont des tailles différentes. Dans un premier temps, on implémente une entrée avec 8 neurones par composantes du RVB (R,V,B) = (8,8,8) = 24 neurones qui prennent des entrées du binaire
Exemple d'une couleur : RVB(235, 1, 4). 
Nous aurons donc 24 neurones qui prendrons chacun un bit de la ligne suivante :
```

11101011 00000100 00000001

```


## Allez plus loin 

http://lcn.epfl.ch/tutorial/french/mlp/html/index.html Applet java d'un MLP