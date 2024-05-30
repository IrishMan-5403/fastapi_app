from fastapi import APIRouter, Body

from repository.vector_db import VectorDB
from service.conversation_service import ConversationService
from service.llm_service import get_chat_response
from service.user_service import clearChat

conversation_router = APIRouter()
conversation_service = ConversationService()


@conversation_router.post("/chat")
async def chat(query: str , username:str):
    """
    Chat endpoint to get a response from the model
    Args:
        query:

    Returns:

    """
    # TODO: Read the method signature and implement the method
    return await conversation_service.chat(query,username)


@conversation_router.post("/new-chat")
async def new_chat(username:str):
    """
    This will invalidate the context (currently uploaded documents and chunks) and start a new conversation
    Args:
        query:

    Returns:

    """
    # TODO: Read the method signature and implement the method

    return clearChat(username=username)
    
