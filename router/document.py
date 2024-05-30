from typing import List
import faiss
from fastapi import APIRouter, File, UploadFile
from repository.vector_db import VectorDB
from service.document_service import getAllFiles, getfile, upload_document, process_document_for_rag

document_router = APIRouter()


@document_router.post("/process-document")
async def process_document(file: UploadFile , username:str):
    """
    Process the uploaded document and store it in the local storage
    Args:
        file:

    Returns:

    """
    # TODO: Read the method signature and implement the method
    upload_document(file)
    return await process_document_for_rag(file ,username)


@document_router.get("/get-documents")
async def get_documents():
    """
    Get all pdf documents (not their chunks) for this chat-session from the local storage.
    Optionally add offset & limit to paginate the results
    Returns:

    """
    # TODO: Read the method signature and implement the method
    return getAllFiles()


@document_router.get("/get-document/{doc_id}")
async def get_document(doc_id: str):
    """
    Get a specific document by its id
    Args:
        doc_id:

    Returns:

    """
    # TODO: Read the method signature and implement the method
    return getfile(file_name=doc_id)
