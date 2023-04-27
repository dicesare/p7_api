# Utiliser une image Python officielle comme base
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers requis dans le conteneur
COPY . /app

# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer le port 8000 pour accéder à l'application web
EXPOSE 8000

# Lancer l'application web avec Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
