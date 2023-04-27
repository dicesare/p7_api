import webbrowser
import uvicorn
from fastapi import FastAPI

from routes.crud import router

app = FastAPI()

app.include_router(router)

# chemin d'accès à l'exécutable de Firefox
firefox_path = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'

# définir Firefox comme navigateur par défaut
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))

# ouvrir la page web
url = 'http://localhost:8000/docs'

if __name__ == "__main__":
    # Lancer votre application Uvicorn sur le port 8000
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
    # Ouvrir le navigateur après le lancement de l'application
    webbrowser.get('firefox').open_new_tab(url)
