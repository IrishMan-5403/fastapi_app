from repository.vector_db import VectorDB
from service.llm_service import get_chat_response
from service.user_service import User, findUser


class ConversationService:
    def __init__(self):
        self.vdb = None

    async def chat(self, query: str, username:str):
        user=findUser(username)
        if not user:
            return {"message":"You are not logged in"}
        self.vdb=user.vector_db
        prompt = await self.vdb.get_prompt(query)
        context = await self.vdb.get_context(prompt)
        llm_response = await get_chat_response(prompt, context=context)
        return llm_response

