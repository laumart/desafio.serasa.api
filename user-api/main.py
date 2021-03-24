import uvicorn
from fastapi import FastAPI
from routes import api_router
from dotenv import load_dotenv
from pathlib import Path
import os

app = FastAPI()

app.include_router(api_router)
HOST_MAIN = os.getenv("HOST_MAIN")
HOST_PORT = os.getenv("HOST_PORT")

@app.on_event("startup")
async def startup_event():
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)



@app.on_event("shutdown")
def shutdown_event():
    with open("log.txt", mode="a") as log:
        log.write("Application shutdown")


if __name__ == "__main__":
   uvicorn.run(app, host=HOST_MAIN, port=int(HOST_PORT))


