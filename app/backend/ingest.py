import os
from app.backend.rag.document_loader import load_doc
from app.backend.rag.chunking import create_chunks
from app.backend.rag.embeddings import create_embeddings
from app.backend.rag.vector_store import (
    update_faiss_index,
    save_chunks
)


def ingest_document(file_path):

    #load doc
    documents = load_doc(file_path)
    
    #create chunks
    chunks = create_chunks(documents)

    # Get uploaded document name
    document_name = os.path.basename(file_path)

    # Store text for embeddings
    text_chunks = []

    # Store chunk metadata
    chunk_records = []

    for chunk in chunks:
        
        text_chunks.append(chunk.page_content)
        chunk_records.append(
        {
            "document": document_name,
            "page": chunk.metadata.get("page", "Unknown"),
            "text": chunk.page_content
        }
    )

    # Create embeddings
    embeddings = create_embeddings(text_chunks)

    # Create vector store
    update_faiss_index(embeddings)

    # Save chunks
    save_chunks(chunk_records)

    return len(text_chunks)