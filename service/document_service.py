from fastapi import HTTPException, UploadFile
import tempfile
import os

from fastapi.responses import FileResponse
from service.llm_service import encode_vectors
from service.user_service import editUser, findUser

file_names=[]
if os.path.exists('path/'):
    for file_name in os.listdir('path/'):
        if os.path.isfile(os.path.join('path/', file_name)):
            file_names.append(file_name)

def upload_document(file: UploadFile):
    # TODO: Implement this method to upload a document
    file_names.append(file.filename)


async def process_document_for_rag(file: UploadFile ,username:str):
    # TODO: Implement this method to process a document for RAG
    user = findUser(username)
    if not user:
        return {"message":"You are not looged in"}
    chunks = await user.vector_db.generate_text_chunks(file)
    chunks_with_embeddings = await encode_vectors(chunks)
    await user.vector_db.save_chunks_to_db(chunks_with_embeddings)
    user= editUser(user)
    return  {"message":"document has been processed" , "user":user["user"].username}

def getAllFiles():

    return file_names


def getfile(file_name:str) :

    file_path=f"path/{file_name}"
    

    if file_name not in file_names:
        raise HTTPException(status_code=404, detail="File not found")
    
    # Return the file as a response
    return FileResponse(file_path)
