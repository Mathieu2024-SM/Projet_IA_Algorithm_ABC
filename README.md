# Projet_IA_Algorithme_ABC
Projet d'IA sur l'étude de l'algorithme Artifical Bee Colonies (ABC)

# Objectif du projet :

1. Étudier et comprendre le fonctionnement de l'algorithme ABC.

2. Comparer ses performances à travers deux implémentations : en Python et en C++.

# Contexte

L'étude s'inscrit dans le cadre d'un cours d'Intelligence Artificielle et explore les métaheuristiques, des algorithmes d'optimisation inspirés de comportements naturels. L'algorithme ABC, inspiré des colonies d'abeilles, est utilisé pour résoudre des problèmes complexes d'optimisation.

# Méthodologie

Phase d'analyse :

1. Étude théorique des articles scientifiques sur ABC.

2. Analyse d'un code Python implémentant ABC.

Phase de développement :

1. Implémentation en Python et en C++ de l'algorithme.

2. Test des deux versions sur des fonctions objectifs (Rastrigin, Ackley, Schwefel, et Rosenbrock).

Phase d'évaluation :

1. Comparaison des performances (temps d'exécution, précision).

2. Analyse des résultats via des graphiques.

# Installation et utilisation du projet en Python
-> Conseil : installez PyCharm Community pour accéder directement au terminal intégré dans PyCharm (View > Tool Windows > Terminal)

-> Téléchargez la bibliothèque mealpy-master depuis le lien gitHub suivant : https://github.com/thieu1995/mealpy/tree/master -> onglet "code" -> "Download zip"

-> Mettez le repertoire dans votre disque dur principal -> créez un dossier "Python" -> copier-coller le fichier

-> Pour utiliser la bibliothèque "meaply" : ouvrer un nouveau projet Python avec PyCharm ou autre et copiez le contenu du fichier main.py

-> Allez dans le terminal et tappez la commande : pip install mealpy

-> Vérifier l'installation de "meaply" : Allez dans votre projet -> dossier .venv -> Lib -> site-packages et vérifiez que vous y trouver "meaply"

-> Utilisation de "meaply" : from mealpy import * (pour avoir accès à tout le contenu de la bibliothèque)

ATTENTION : petite correction à faire dans le fichier optimizer.py de la bibliothèque "mealpy" : changer la ligne 625 : #if list_fitness.ptp() == 0: par if np.ptp(list_fitness) == 0: (si vous utilisez NumPy 2.0 ou une version plus récente)

ATTENTION : pour éviter l'affichage de "2025/01/04 02:18:14 PM, INFO, mealpy.swarm_based.ABC.OriginalABC: >>>Problem: P, Epoch: 528, Current best: 288.1531068963579, Global best: 242.9776921578927, Runtime: 0.00556 seconds" dans la console
--> ligne 270 et 271 du fichier optimizer.py -> mettre en #

# Accès direct aux fichier
--> allez dans l'onglet "main" --> selctionnez Projet_IA_ABC_acces_code
