# House Price Predictor

Je me situe dans le top [**7%**](https://www.kaggle.com/aryamaankunwar/competitions) pour ce concours \
[notebook](https://github.com/aryamaan3/Kaggle-Data-Science/blob/master/House%20Price%20Estimation/house-price-predictor.ipynb)

## Data Cleaning
On ne garde que les colonnes ayant une faible cardinalité (nombre de données unique).
Le modèle verra sa tâche facilité.

### Les caractéristiques catégorielles
Définition : Donnée non-numérique, où établir un "rang" est impossible.
En règle générale, la meilleure méthode est "one hot encode". Celle-ci consiste à créer une colonne pour chaque "possibilité" d'une caractéristique catégorielle.
Exemple : couleurs possibles pour un objet = rouge, bleu, vert. En appliquant "one hot encode", chaque rangée aura trois nouvelles colonnes : rouge, bleue et verte. Pour une rangée où l'objet est bleu, la colonne bleue sera "true" et le reste "false". Le modèle sera mieux orientée.

## Choix du modèle

### Arbre de décision
Trop élémentaire, **MAE** > 20.000

### Forêt d'Arbre decisionelles
Fait la moyenne de n arbres de décision, **MAE** < 20.000

### XGBoost
XGBoost est un algorithme de boosting de gradient, celui-ci regroupe les résultats d'un **ensemble** de modèles plus faibles. 
J'ai également réglé quelques hyperparamètres afin d'obtenir un **MAE** < 17.000.
XGBoost a donc été le modèle le plus efficace.
