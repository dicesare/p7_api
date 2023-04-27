import uvicorn
from fastapi import FastAPI

from routes.crud import router

app = FastAPI()

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080, log_level='info')
