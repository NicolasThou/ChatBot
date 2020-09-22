# ChatBot Project

## Table of contents

- [Dossier PFA](#Dossier PFA)
- [Dossier data](#Dossier data)
- [Dossier model](#Dossier model)
- [Dossier src](#Dossier src)
- [Dossier test](#Dossier test)
- [Utilisation](#Utilisation)

---
###Dossier PFA
 - Le dossier PFA contient 4 sous dossiers :
    - Le dossier data
    - Le dossier model
    - Le dossier src
    - Le dossier test
---

##Dossier data

Ce dossier contient toutes les données .xlsx pour pouvoir modifier les données avec Excel.
Une fois les données modifiées, les enregistrer dans le format .csv. Data_base.xlsx contient les données
de chaque cockpit avec pour caractéristiques modifiables/optionnelles surligné en orange. Ce code
couleur permet de spécifier le fait que la caractéristiques est ajustable.

Les fichier excel pour les cockpit IFR, VFR et MH sont uniquement les transposées des colonnes
de la matrice du fichier Data_Base.xlsx

Le fichier excel Data_Base_Basic.xlsx est la matrice sans les caractéristiques modifiables.

---

##Dossier src

Le dossier src contient le fichier make_data.py et Question.py. Le fichier make_data.py
génère toutes les configurations de cockpit possible. 
Il y a plus de 204 800 possibilitées pour les combinaisaons de caractéristiques.
Il faut bien utiliser des séparateur de virgule "," et non pas des séparateurs de point virgule
" ; " pour les fichier CSV.

Les features adjustable sont les caractéristiques qui peuvent avoir des valeurs différentes. Les indices de ces caractéristiques sont obtenues
par rapport au fichier xlsx ou csv. Il faut compter manuellement quelles sont les colonnes dont les caractéristiques
sont modifiables (de couleur orange). Attention aux indices avec la librairie pandas.

Pour les dependant variable, nous avons besoin de traiter les categorical variable. Pour cela, il suffit de les encoder.
Nous avons donc générer autant de dependant variable que d'individus possibles, c'est à dire plus de 204 800 variables.
Pour chaque catégorie de cockpit nous avons 2 à la puissance le nombre de caractéristiques modifiables. Donc 2 à la puissance la
longueur d'une liste features_adjustable.

- Question.py
  - Ce fichier permet de faire parler le ChatBot avec plusieurs questions successives (Cf Arbres de Questions)
  - Deux cas sont possibles et intéressant à traiter pour le machine learning. Le cas où nous devons
  prédire le meilleur cockpit selon les caractéristiques entrées.
  - Le deuxième cas (qui doit être traité) est le cas de la description d'une pièce de cockpit dans une catégorie précise.
  
  

##Dossier model

Ce dossier contient le modèle prédictif qui utilise la méthode de Random Forest à 10 arbres. 
Nous avons testé notre modèle avec une matrice de confusion. Il n'y aucun faux positifs et faux négatifs :
```bash
print(matrix)
```
Nous avons aussi utilisé une méthode de k-fold cross validation et la précision est en moyenne de 1.00 donc
de 100% : 
```bash
print(accuracies.mean())
print(accuracies.std())
```
Ce résultat s'explique que les données sont très simples car les caractéristiques des cockpits
ne peuvent prendre que la valeur de 1 ou de 0. Mise à part les IDU qui peuvent prendre les valeurs de 1, 2, 3 ou 4.


##Dossier test

Ce dossier est vide pour l'instant car tous les tests se sont fait dans le main de chaque fichier .py
Les tests pouvant être généré avec pytest.

##Utilisation

Dans les questions, la réponse attendue n'est pas une chaîne de caractère mais un 0 ou un 1. 
De plus, lorsque le chatBot demande une catégorie de cockpit ou de pièce, la réponse attendue est un entier
avec pour première réponse 0. Attention aux indices. Exemple : réponse 0 = Light VFR, réponse 1 = Light IFR, 
réponse 3 = MH etc...



