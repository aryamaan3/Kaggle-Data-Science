# House Price Predictor

Je me situe dans le top [**7%**](https://www.kaggle.com/aryamaankunwar/competitions) pour ce concours \
[notebook](https://github.com/aryamaan3/Kaggle-Data-Science/blob/master/House%20Price%20Estimation/house-price-predictor.ipynb)

## Data Cleaning
On ne va garder que les colonnes ayant une faible cardinalité (nb de donée unique) 
cela va rendre la tache plus facile pour le modèle

### Les caractéristiquex catégorielles
En régle général la meilleure methode est "one hot encode", cette méthode consiste à creer une colonne pour chaque "état" d'une caractéristique catégorielle.
ex : couleur possibles = rouge, bleu, vert. en appliquant one hot encode chaque rangée aura trois nouvelles colonnes : rouge, bleu et vert. pour une rangée ou l'objet est bleu, la colonne blue sera true et le reste false. Cela permet de mieux orienter le modèle  

## Choix du modèle

### Arbre de décision
trop basique, **MAE** > 20.000

### Forêt d'Arbre decisionelles
fait la moyenne de n arbres de décision, **MAE** < 20.000

### XGBoost
XGBoost est un algorithme de boosting de gradient, ceci consiste à regrouper les resultats d'un **ensemble** de modèle plus faible 
J'ai egalement reglé quelques hyperparamètres afin d'obtenir un **MAE** < 17.000.
XGBoost a donc été le modèle le plus efficace
