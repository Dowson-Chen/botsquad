from fastapi import FastAPI
from botsquad.api.routes import router  # make sure this file exists

app = FastAPI()  # ✅ This is what Uvicorn needs to find

app.include_router(router)

@app.get("/")
def root():
    return {"message": "BotSquad backend is running!"}