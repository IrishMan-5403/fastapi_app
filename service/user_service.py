from typing import Dict
from fastapi import HTTPException
from pydantic import BaseModel
from repository.vector_db import VectorDB



user_db: Dict[str, "User"] = {}


class User(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        
    username: str
    password: str
    vector_db: VectorDB = None 

user_db["irish"] = User(username="irish",password="1234",vector_db=VectorDB())

def findUser(username: str):

    if username not in user_db:
        return False
    return user_db[username]

def addUser(username:str,password:str):

    if username in user_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    new_user = User(username=username, password=password, vector_db=VectorDB())
    user_db[username] = new_user  # Assuming VectorDB is initialized here
    return {"message": "Registration successful" , "user" : username }

def editUser(user:User):
    if user.username in user_db:
        user_db[user.username] = user
        return {"message": "User details updated successfully", "user": user}
    else:
        user.vector_db = VectorDB()
        user_db[user.username] = user
        return {"message": "User created successfully", "user": user}
    
def clearChat(username:str):
    if username not in user_db:
        return{"message":"Not Logged in"}
    
    user_db[username]["vector_db"] = VectorDB()
    return {"message": "Chat Cleared" , "user" : username }