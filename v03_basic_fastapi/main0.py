from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

# 1. 홈 화면 구성
@app.get('/')
def home():
    return "Welcome!!!"

# 2. 다른 화면 구성
@app.get('/data')
def data():
    return "Lost Data... :("

# 3. HTML 화면 구성
@app.get('/my_html')
def get_html():
    return FileResponse('index.html')

class Model(BaseModel):
    name : str
    age : int

@app.post("/send")
def post_data(data : Model):
    print(data)
    return "SUCCESS"
