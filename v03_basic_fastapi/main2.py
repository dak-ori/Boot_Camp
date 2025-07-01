from fastapi import FastAPI
from controller import users, items, event

app = FastAPI()
app.include_router(users.router)
app.include_router(items.router)
app.include_router(event.router)

@app.get("/")
def home():
    return "HOME"