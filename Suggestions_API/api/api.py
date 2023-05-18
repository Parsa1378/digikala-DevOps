from fastapi import FastAPI,status,Response,Header
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username:str
    password:str

users:dict
class Suggestion(BaseModel):
    text:str
    user:str

suggestions:list[Suggestion]

def generate_token(username):
    token = "hjndwa"+username+"djsnv"
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

@app.post("/suggestions")
def post_suggestion(text:str,response:Response,token:str = Header(...)):
    username = token[6:-5]
    # user:User
    # if username in users.keys():
    #     user.username = username
    #     user.password =
    if not text:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "ok":False,
            "error":"no text provided"
        }
    suggestion = Suggestion(text=text,user=username)
    suggestions.append(suggestion)
    response.status_code = status.HTTP_201_CREATED
    return {
        "ok":True,
    }

@app.get("/suggestions")
def get_suggestions():
    return suggestions

        