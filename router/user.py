from fastapi import APIRouter, Body , HTTPException
from pydantic import BaseModel
from typing import Dict
from repository.vector_db import VectorDB
from service.llm_service import get_chat_response
from service.user_service import User, editUser,findUser,addUser

user_router = APIRouter()


@user_router.post("/login")
async def login(username:str ,password:str):
    """
    User login endpoint
    Returns:

    """
    # TODO: Read the method signature and implement the method
    user=findUser(username=username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username")
    if password == user.password:
        return {"message": "Login successful", "user":user.username}
    else:
        raise HTTPException(status_code=401, detail="Invalid  password")


@user_router.post("/register")
async def register(username:str,password:str):
    """
    User registration endpoint
    Returns:

    """
    # TODO: Read the method signature and implement the method
    return addUser(username=username,password=password)



@user_router.post("/logout")
async def logout():
    """
    User logout endpoint
    Returns:

    """
    # TODO: Read the method signature and implement the method
    return {"message": "Logout successful"}
    


@user_router.get("/user")
async def get_user_details(username: str):
    """
    User get endpoint
    Returns:

    """
    # TODO: Read the method signature and implement the method
    
    return findUser(username)


@user_router.post("/user")
async def set_user_details(user: User = Body(...)):
    """
    User create/update endpoint
    Returns:

    """
    # TODO: Read the method signature and implement the method
    return editUser(user)
    
