import streamlit as st
import requests
import time
import os
from dashboard import show_dashboard


API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000"
)

# Page Config
st.set_page_config(
    page_title="MediAssist AI",
    layout="wide"
)

#chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
#uploaded document
if "uploaded_doc" not in st.session_state:
    st.session_state.uploaded_doc = None

#fetching files from
RAW_DATA_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../data/raw_data"
    )
)
#title 
st.markdown("""
<style>
.block-container {
                padding-top: 1.2rem;
            color:#0F4C81;

}
</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <h1 style='text-align: center;'>
        MediAssist AI
    </h1>
    """,
    unsafe_allow_html=True
)

st.divider()

###radio buttons##
# ----------------------------------
# Navigation
# ----------------------------------

if "page" not in st.session_state:
    st.session_state.page = "💬 Chat"

left, center, right = st.columns([6, 3, 1])

with center:

    page = st.segmented_control(
        "",
        ["💬 Chat", "📊 Dashboard"],
        default=st.session_state.page,
        selection_mode="single"
    )

    if page != st.session_state.page:
        st.session_state.page = page
        st.rerun()

st.divider()
#####

if st.session_state.page == "💬 Chat":
    # 30% / 70% Layout

    left_col, right_col = st.columns([3, 7])

    # ==================================================
    # LEFT PANEL
    # ==================================================
    with left_col:
        with st.container(border=True):

            # -----------------------------
            # Upload Documents
            # -----------------------------
            st.markdown(
            """
            <h4 style='text-align: left;'>
            Upload Documents
            </h4>
            """,
            unsafe_allow_html=True
            )

            uploaded_file = st.file_uploader(
                "Choose File",
                type=["pdf", "docx", "txt"]
            )

            if (uploaded_file is not None
                and uploaded_file.name != st.session_state.uploaded_doc
                ):
                
                files = {
                    "file": (
                        uploaded_file.name,
                        uploaded_file,
                        uploaded_file.type
                    )
                }

                response = requests.post(
                f"{API_URL}/upload",
                files=files
                )

                if response.status_code == 200:
                    st.session_state.uploaded_doc = uploaded_file.name
                    success_message = st.empty()
                    success_message.success(
                        "Document uploaded successfully"
                    )
                    time.sleep(3)
                    success_message.empty()

            st.divider()

            # -----------------------------
            # Uploaded Documents
            # -----------------------------
            st.markdown(
            """
            <h4 style='text-align: left;'>
            Uploaded Documents
            </h4>
            """,
            unsafe_allow_html=True
            )

            uploaded_files = []

            if os.path.exists(RAW_DATA_DIR):
                uploaded_files = sorted(
                    os.listdir(RAW_DATA_DIR)
                )

            if uploaded_files:

                for index, file_name in enumerate(
                    uploaded_files,
                    start=1
                ):

                    st.write(
                        f"{index}. {file_name}"
                    )

            else:
                st.write(
                    "No documents uploaded"
                )

            st.divider()

            # -----------------------------
            # Medical Image Analysis
            # -----------------------------
            st.markdown(
            """
            <h4 style='text-align: left;'>
            Medical Image Analysis
            </h4>
            """,
            unsafe_allow_html=True
            )

            uploaded_image = st.file_uploader(
                "Upload Prescription / Lab Report",
                type=["png", "jpg", "jpeg"],
                key="medical_image"
            )

            if uploaded_image is not None:

                st.image(
                    uploaded_image,
                    caption="Uploaded Image",
                    use_container_width=True
                )

                if st.button(
                    "Analyze Image",
                    key="analyze_image"
                ):

                    with st.spinner("Analyzing image..."):

                        files = {
                            "file": (
                                uploaded_image.name,
                                uploaded_image.getvalue(),
                                uploaded_image.type
                            )
                        }

                        response = requests.post(
                            f"{API_URL}/analyze-image",
                            files=files
                        )

                        if response.status_code == 200:

                            result = response.json()

                            st.success(
                                "Analysis completed successfully."
                            )

                            st.markdown(
                                "#### Medical Report Summary"
                            )

                            st.session_state["prescription_context"] = result["ocr_text"]
                            st.session_state["prescription_file"] = uploaded_image.name


                            st.success(
                            "Prescription uploaded successfully. You can now ask questions about it."
                            )

                            with st.expander(
                                "View OCR Extracted Text"
                            ):
                                st.write(
                                    result["ocr_text"]
                                )

                        else:

                            st.error(
                                "Failed to analyze image."
                            )

            st.divider()

            # -----------------------------
            # Sources
            # -----------------------------
            st.markdown(
            """
            <h6 style='text-align: left;'>
            Sources
            </h6>
            """,
            unsafe_allow_html=True
            )

            st.markdown("""
            <small>
            1. RAG on External Data<br>
            2. Multimodal Image<br>
            3. Database
            </small>
            """, unsafe_allow_html=True)

    # ==================================================
    # RIGHT PANEL
    # ==================================================
    # ==================================================
    # RIGHT PANEL
    # ==================================================
    with right_col:

        if st.session_state.chat_history:

            history_container = st.container(
                border=True,
                height=520
            )

            with history_container:
            # -----------------------------
            # Conversation History
            # -----------------------------
                st.markdown(
                """
                <h4>
                Conversation History
                </h4>
                """,
                unsafe_allow_html=True
                )

                #if st.session_state.chat_history:
                for chat in st.session_state.chat_history:

                    st.markdown(
                    f"**You:** {chat['question']}"
                    )

                    st.markdown(
                    f"**MediAssist:** {chat['answer']}"
                    )

                    st.caption(
                    f"📄 Source: {chat['source']}"
                    )

                    st.divider()

                
            st.markdown("---")
        else:
                    st.markdown(
                    """
                    <div style="text-align:center;padding:50px;">
                    <h2>👋 Welcome to MediAssist AI</h2>

                    <p>Ask questions about:</p>

                    📄 Uploaded Documents<br>
                    🖼️ Medical Prescriptions<br>
                    🗄️ Patient Records
                    </div>
                    """,
                    unsafe_allow_html=True
                    )

            # -----------------------------
            # Ask Question
            # -----------------------------
        st.write(
                "Ask questions about uploaded documents"
        )

        col1, col2 = st.columns([5, 1])

        with col1:
            question = st.text_input(
            "",
            placeholder="Ask about documents, patients or prescriptions...",
            label_visibility="collapsed"
            )

        with col2:
            ask_clicked = st.button(
            "Ask",
            use_container_width=True
            )

        if ask_clicked:

            if question.strip() == "":

                st.warning(
                        "Please enter a question"
                    )

            else:

                response = requests.post(
                    f"{API_URL}/chat",
                    json={
                        "question": question,
                        "prescription_context": st.session_state.get(
                        "prescription_context",
                        ""
                        ),
                        "prescription_file": st.session_state.get(
                        "prescription_file",
                                ""
                        )
                        }
                    )

                if response.status_code == 200:

                    result = response.json()

                    st.session_state.chat_history.append(
                        {
                            "question": question,
                            "answer": result["answer"],
                            "source": result["source"]
                        }
                    )

                    st.rerun()

                else:

                    st.error(
                            "Failed to get response from chatbot"
                    )
        ###

else:
    #from dashboard import show_dashboard

    show_dashboard()