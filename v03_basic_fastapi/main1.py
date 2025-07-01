from fastapi import FastAPI

app = FastAPI()

# 홈 화면 구성
@app.get('/')
def home():
    return "Hi"

# 다른 화면 구성
@app.get('/items/{item_id}')
def read_item(item_id):
    return {"item_id " : item_id}