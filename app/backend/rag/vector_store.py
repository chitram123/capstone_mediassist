import faiss
import numpy as np
import pickle
import os

BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../../"
        )
    )

def update_faiss_index(embeddings):

    dimension = 384

    vector_store_path = os.path.join(
        BASE_DIR,
        "vector_store",
        "faiss_index"
    )

    # Load existing FAISS if available
    if os.path.exists(vector_store_path):

        index = faiss.read_index(vector_store_path)
        print("Existing FAISS index loaded.")

    else:

        index = faiss.IndexFlatL2(dimension)
        print("New FAISS index created.")

    # Append new embeddings
    index.add(embeddings)

    # Save updated FAISS
    faiss.write_index(
        index,
        vector_store_path
    )

    print(f"Total vectors in FAISS: {index.ntotal}")

    return index

def save_chunks(text_chunks):

    chunks_path = os.path.join(
        BASE_DIR,
        "vector_store",
        "chunks.pkl"
    )

    # Load existing chunks if available
    if os.path.exists(chunks_path):

        with open(chunks_path, "rb") as f:
            existing_chunks = pickle.load(f)

        print("Existing chunks loaded.")

    else:

        existing_chunks = []
        print("Creating new chunks file.")

    # Append new chunks
    existing_chunks.extend(text_chunks)

    # Save updated chunks
    with open(chunks_path, "wb") as f:

        pickle.dump(
            existing_chunks,
            f
        )

    print(f"Total chunks saved: {len(existing_chunks)}")



