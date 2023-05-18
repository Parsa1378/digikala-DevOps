from fastapi import FastAPI,status,Response
from pydantic import BaseModel
import hashlib

app = FastAPI()

class User(BaseModel):
    username:str
    password:str

users:dict

def generate_token(username):
    secret_key = 'secret'
    token = hashlib.sha256((username + secret_key).encode()).hexdigest()
    return token

@app.get("/")
def check_service(response:Response):
    response.status_code = status.HTTP_200_OK
    return {"ok":True}

@app.post("/signup")
def signup(user:User,response:Response):

    if not user.username or not user.password:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "ok":False,
            "error" : "no username or password provided"
        }
    if user.username in users.keys():
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {    
                "ok":False,
                "error":"user already exists"
            }
    users[user.username] = user.password
    token = generate_token(user.username)
    response.status_code = status.HTTP_201_CREATED
    return {
        "ok":True,
        "token":token
    } , {"Authorization": f"{token}"}

@app.post("/login")
def login(user:User,response:Response):
    if not user.username or not user.password:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "ok":False,
            "error" : "no username or password provided"
        }
    
    if user.username in users.keys():
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {    
                "ok":False,
                "error":"invalid username or password"
            }
    token = generate_token(user.username)
    response.status_code = status.HTTP_200_OK
    return {
        "ok":True,
        "token":token
    } , {"Authorization": f"{token}"}

