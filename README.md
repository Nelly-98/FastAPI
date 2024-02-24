# Projet FastAPI

Ce projet est une API FastAPI pour gérer des questionnaires. Il permet aux utilisateurs de se connecter, de récupérer des questions basées sur certains critères et aux administrateurs d'ajouter de nouvelles questions.

## Installation et Configuration

### Prérequis

- Python 3.6+
- pip (Gestionnaire de paquets Python)

### Configuration de l'Environnement Virtuel

#### Création de l'Environnement Virtuel

Ouvrez un terminal et naviguez jusqu'au dossier exam
_GUEPNANG. Exécutez la commande suivante pour créer un environnement virtuel :

- python -m venv venv

#### Activation de l'Environnement Virtuel

##### Sur Windows, exécutez :

- .\venv\Scripts\activate

##### Sur Unix ou MacOS, exécutez :

- source venv/bin/activate

### Installation des Dépendances

Avec l'environnement virtuel activé, installez les dépendances requises en exécutant :

- pip install -r requirements.txt

## Lancement de l'API

Pour démarrer le serveur FastAPI, exécutez la commande suivante :

- uvicorn main:api --reload


## Utilisation
Une fois l'API en cours d'exécution, vous pouvez accéder à la documentation interactive de l'API à l'adresse suivante : http://localhost:8000/docs.


