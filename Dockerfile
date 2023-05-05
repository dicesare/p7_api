# Utilise une image Python officielle en tant qu'image parente
FROM python:3.9-slim-buster

# Définit le répertoire de travail de l'application dans le conteneur
WORKDIR /app

# Créer un environnement virtuel
RUN python -m venv /venv

# Copie les fichiers nécessaires (dépendances et code source)
COPY main.py /app
COPY requirements.txt /app
COPY models/ models/
COPY routes/ routes/

# Activer l'environnement virtuel et installer les dépendances
RUN venv/Scripts/activate
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copie le dossier de tests dans le conteneur
COPY test/ test/

# Exécute les tests
RUN pytest

# Exposer le port 8080 pour accéder à l'application web
EXPOSE 8080

# Lancer l'application web avec Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

# Nommer l'image et spécifier la version
LABEL name="p7_api" version="1.1.0"
