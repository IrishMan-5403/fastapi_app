import os
import fitz
import faiss
from typing import List
import numpy as np
from starlette.datastructures import UploadFile
from langchain.schema.document import Document
from langchain_community.vectorstores import FAISS
from service.llm_service import embeddings, encode_vectors
from .query_refiner import QueryRefiner


class VectorDB:
    def __init__(self):
        self.embeddings = embeddings
        self.db = None

    async def generate_text_chunks(self, file: UploadFile):
        """
        Reads text chunks from an uploaded file (pdf only) and returns a list of chunks.

        Args:
            file (UploadFile): The uploaded file object.

        Returns:
            list: A list of text chunks (strings).
        """
        # TODO: Implement a method to read text chunks from a PDF file
        upload_folder = "path/"
        os.makedirs(upload_folder, exist_ok=True)
        file_path = os.path.join(upload_folder, file.filename)
        file.file.seek(0)
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())

# Open the saved file with PyMuPDF
        pdf_document = fitz.open(file_path)
        chunks=[]
        
        # Extract text from each page
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text = page.get_text()
            chunks.extend(self.split_text_into_chunks(text))
        
        return chunks
    def split_text_into_chunks(self, text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
        """
        Splits the given text into chunks of a specified size with overlap.

        Args:
            text (str): The text to be split.
            chunk_size (int): The size of each chunk.
            overlap (int): The number of overlapping characters between chunks.

        Returns:
            List[str]: A list of text chunks.
        """
        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunks.append(text[start:end])
            start += chunk_size - overlap
        return chunks
    

    async def encode_and_store(self, chunks):
        """Encodes data points and stores their vectors in memory."""
        # TODO: Implement a method to get vector embeddings for chunks and store data in a database
        embeddings = [self.embeddings(chunk) for chunk in chunks]
        for chunk, embedding in zip(chunks, embeddings):
            self.db.add([embedding], [Document(page_content=chunk)])

    async def get_context(self, query: str):
        """Searches for matching vectors based on a query vector."""
        # TODO: Find matching chunks based on vector distance
        if self.db == None:
            return {"message":"Please load a pdf first"}
        query_refiner = QueryRefiner()
        refined_query = query_refiner.get_refined_query(query)
        query_embedding =await encode_vectors([refined_query])
        matched_docs = self.db.search(refined_query,search_type="similarity", k=5)

        return '\n\n'.join([doc.page_content for doc in matched_docs])

    async def get_prompt(self, query):
        # TODO: Implement a method to get a prompt for processing query correctly
        query_refiner = QueryRefiner()
        refined_query = query_refiner.get_refined_query(query)
        
        return f"Question: {refined_query}\nPlease provide an answer:"


    async def save_chunks_to_db(self, chunks_with_embeddings):
        # TODO: Implement a method to save chunks to a vector database, with embeddings (vectors) for each chunk
        documents = []
    
        # Iterate over chunks and embeddings to create documents
        for chunk, embedding in chunks_with_embeddings:
            # Ensure chunk is a string
            if not isinstance(chunk, str):
                raise ValueError("Chunk should be a string.")
            document = Document(page_content=chunk)
            documents.append(document)

        self.db = FAISS.from_documents(documents,self.embeddings)
