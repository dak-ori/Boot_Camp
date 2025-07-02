from fastapi import FastAPI
from controller import admins, items, users, event

app = FastAPI()
app.include_router(admins.router)
app.include_router(items.router)
app.include_router(event.router)
app.include_router(users.router)

@app.get('/')
def home():
    return 'Home'