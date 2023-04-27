# Projet 7: Déployez un modèle dans le cloud

## Description du projet

Le projet consiste à mettre en place une API permettant de prédire le sentiment d'un tweet grâce à un modèle de classification entraîné sur la base de données Sentiment140. L'API sera déployée sur Google Cloud Platform et permettra aux utilisateurs d'envoyer des requêtes HTTP pour obtenir une prédiction.

## Arborescence du projet

Le projet est organisé en plusieurs dossiers :

- `models/` contient le modèle de classification et les scripts pour le prétraitement des données.
- `routes/` contient les fichiers pour les endpoints de l'API.
- `test/` contient les tests unitaires.
- `model_saved/` contient les modèles entraînés.

## Prérequis

Les dépendances nécessaires pour le projet sont listées dans le fichier `requirements.txt`. Vous pouvez les installer en utilisant la commande suivante :

`pip install -r requirements.txt`


## Utilisation

Pour lancer l'API, exécutez la commande suivante :

`python main.py`


Une fois l'API lancée, vous pouvez envoyer une requête HTTP pour obtenir une prédiction. Voici un exemple avec cURL :

`curl -X POST
http://localhost:8000/predict
-H 'Content-Type: application/json'
-d '{
"text": "I love this product!"
}'
`

## Tests

Les tests unitaires sont implémentés à l'aide de pytest. Vous pouvez les lancer avec la commande suivante :

`python -m pytest test/test_class.py`


`python -m pytest test/test_client.py`



## Auteurs

- COCO Roc-Antony