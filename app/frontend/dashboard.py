import os
import pickle
import pandas as pd
import streamlit as st


RAW_DATA_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../data/raw_data"
    )
)

VECTOR_STORE = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../vector_store"
    )
)

RESULT_FILE = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../backend/evaluation/evaluation_results/rag_evaluation_results.csv"
    )
)

def show_dashboard():

    st.title("📊 MediAssist AI Dashboard")

    st.divider()

    # -------------------------------
    # Knowledge Base
    # -------------------------------

    uploaded_documents = 0
    indexed_chunks = 0

    if os.path.exists(RAW_DATA_DIR):
        uploaded_documents = len(os.listdir(RAW_DATA_DIR))

    chunk_file = os.path.join(
        VECTOR_STORE,
        "chunks.pkl"
    )

    if os.path.exists(chunk_file):

        with open(chunk_file, "rb") as f:

            chunks = pickle.load(f)

        indexed_chunks = len(chunks)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Uploaded PDFs",
        uploaded_documents
    )

    c2.metric(
        "Indexed Chunks",
        indexed_chunks
    )

    c3.metric(
        "Embedding Model",
        "MiniLM"
    )

    c4.metric(
        "Vector DB",
        "FAISS"
    )

    st.divider()

    # -------------------------------
    # Evaluation Metrics
    # -------------------------------

    st.subheader("Evaluation Summary")

    if os.path.exists(RESULT_FILE):

        evaluation_df = pd.read_csv(RESULT_FILE)

        if evaluation_df.empty:
            st.warning("Evaluation file is empty.")

        else:
        

            accuracy = round(evaluation_df["Accuracy"].mean(), 2)

            faithfulness = round(evaluation_df["Faithfulness"].mean(), 2)

            groundedness = round(evaluation_df["Groundedness"].mean(), 2)

            hallucination = round(evaluation_df["Hallucination"].mean(), 2)

            response = round(evaluation_df["Response_Time(sec)"].mean(), 2)

            col1,col2,col3,col4,col5 = st.columns(5)

            col1.metric(
                "Accuracy",
                accuracy
            )

            col2.metric(
                "Faithfulness",
                faithfulness
            )

            col3.metric(
                "Groundedness",
                groundedness
            )

            col4.metric(
                "Hallucination",
                hallucination
            )

            col5.metric(
                "Avg Response (sec)",
                response
            )

    else:

        st.info(
            "Run evaluation to view metrics."
        )

    st.divider()

    # -------------------------------
    # System Health
    # -------------------------------

   
     # -------------------------------
    # AI Information
    # -------------------------------

    st.subheader("Project Information")

    info_df = pd.DataFrame(
        {
            "Component": [
                "Framework",
                "LLM",
                "Embedding Model",
                "Vector Database",
                "OCR Engine",
                "Evaluation Framework"
            ],
            "Technology": [
                "LangGraph",
                "Groq GPT-OSS-120B",
                "all-MiniLM-L6-v2",
                "FAISS",
                "Tesseract OCR",
                "LLM-as-Judge"
            ]
        }
    )

    st.dataframe(
        info_df,
        hide_index=True,
        use_container_width=True
    )

    # -------------------------------
    # Uploaded Documents
    # -------------------------------

    st.subheader("Knowledge Base Files")

    if uploaded_documents:

        files = sorted(
            os.listdir(
                RAW_DATA_DIR
            )
        )

        documents_df = pd.DataFrame(
        {
        "Document": files
        }
        )

        st.dataframe(
        documents_df,
        use_container_width=True,
        hide_index=True
        )

    else:

        st.info(
            "No documents uploaded."
        )

    st.divider()

    # -------------------------------
    # Recent Evaluation
    # -------------------------------

    st.subheader("Recent Evaluation Results")

    if os.path.exists(RESULT_FILE):

        evaluation_df = pd.read_csv(RESULT_FILE)

        st.dataframe(
        evaluation_df[
            [
                "Question",
                "Overall_Score",
                "Confidence"
            ]
        ].tail(10),
        use_container_width=True,
        hide_index=True
        )
    else:

        st.info(
            "No evaluation results available."
        )

    st.divider()

   