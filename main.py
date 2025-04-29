from fastapi import FastAPI
import uvicorn
from app import rout

app = FastAPI()
app.include_router(rout)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0')