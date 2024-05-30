from dotenv import load_dotenv
from openai import OpenAI
import os
from pathlib import Path
from langchain_openai import OpenAIEmbeddings

env_path = Path(__file__).parent / '../.env'
if env_path.is_file():
    load_dotenv(dotenv_path=env_path)
openai_api_key = os.getenv("openai_api_key")
temperature = 1.0
client = OpenAI(api_key=openai_api_key)
embeddings = OpenAIEmbeddings(api_key=openai_api_key)


async def encode_vectors(data):
    """Encodes a list of data points into vectors using the OpenAI API.

    Args:
        data (list): A list of data points (strings) to be encoded.

    Returns:
        list: A list of encoded vectors (embeddings).
    """

    encoded_vectors = []

    # Batch data for efficiency (adjust batch_size as needed)
    batch_size = 1
    for i in range(0, len(data), batch_size):
        batch = data[i]
        response = client.embeddings.create(
            input=batch,
            model="text-embedding-3-small"
        )
        embeddings = [embedding.embedding for embedding in response.data] # Extract embeddings from response
        encoded_vectors.append([ data[i],embeddings])
    return encoded_vectors


async def get_chat_response(prompt, context):
    try:
        chat_template = """
        You are a helpful assistant. Here is some context to help answer the following question.
        
        Context:
        {context}
        
        Question:
        {question}
        """

        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant"
            },
            {
                "role": "user",
                "content": chat_template.format(question=prompt, context=context)
            }
        ]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=temperature
        )

        # answer = response['choices'][0]['message']['content']
        answer = response.choices[0].message.content
        return answer
    except Exception as e:
        raise e
