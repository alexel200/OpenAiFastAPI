from fastapi import FastAPI
from src.api import openai_uploads, openai_vector_store_file

description = """
The endpoints implemented here are indeed to interact with OpenAI Platform. So,
the implementation follows the recommendations and descriptions disposed 
<a href='https://platform.openai.com/docs/api-reference/' target='_blank'>OpenAI Platform</a>
"""
tags_metadata = [
    {
        "name": "openai_uploads",
        "description": """This operations are related to upload files by parts, according to the documentation.
            The maximum chunk of file is <strong>64Mb</strong>. The operation must follow this sequence:
            <ol>
                <li>The creation of the upload</li>
                <li>Upload parts</li>
                <li>Complete upload</li>
                <li>The Cancellation can be performed at any time before completing the upload.</li>
            </ol>
            <br/>
            For more details consult <a href='https://platform.openai.com/docs/api-reference/uploads' target='_blank'>here</a>.""",
    },
{
        "name": "openai_vector_store_files",
        "description": """Vector store files represent files inside a vector store.
            <br/>
            For more details consult <a href='https://platform.openai.com/docs/api-reference/vector-stores-files/createFile' target='_blank'>Vecto Store Files</a>.""",
    }
]

app = FastAPI(
    title = "OpenAI implementation",
    description = description,
    version = "0.0.1",
    openapi_tags=tags_metadata,
)

app.include_router(openai_uploads.router)
app.include_router(openai_vector_store_file.router)