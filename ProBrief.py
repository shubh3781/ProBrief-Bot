import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def main():
    st.set_page_config(
        page_title="ProBrief",
        page_icon="sp.png"
    )

    # Display image as a header with text
    col1, col2 = st.columns([1, 30])
    with col1:
        st.image("sp.png", width=30)
    with col2:
        st.markdown("<h2 style='margin-top:-20px;'>ProBrief</h2>", unsafe_allow_html=True)

    # Adding custom CSS for background and styling
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #2E5A87;
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .stTextArea textarea {
            animation: fadeIn 2s ease-in;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.header("Everything About Shubh by ProBrief")

    # Input API key
    api_key_input = st.text_input("Enter your GeminiAPI key:", type="password")
    if st.button("Set API Key"):
        if api_key_input:
            os.environ["gemini_api_key"] = api_key_input
            st.success("API Key set successfully.")
        else:
            st.error("Please enter a valid API key.")

    # Ensure API key is available
    Api_key = os.getenv("gemini_api_key")
    if not Api_key:
        st.warning("Please enter an API key to proceed.")
        return

    # Load data and initialize embeddings
    loader = CSVLoader(file_path="Shubh_Bot.csv", encoding="utf-8", csv_args={'delimiter': '|'})
    dataset = loader.load()
    myembedmodel = GoogleGenerativeAIEmbeddings(google_api_key=Api_key, model="models/embedding-001")
    db = FAISS.from_documents(documents=dataset, embedding=myembedmodel)

    def retrieve_data(query):
        similar_response = db.similarity_search(query)
        entire_data = [doc.page_content for doc in similar_response]
        return entire_data

    myllm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-002", temperature=0, google_api_key=Api_key)

    SPtemplate = """
You are a professional assistant representing [Shubhkumar Patel], capable of providing accurate and comprehensive responses about his professional and academic background based on stored data. 
You are expected to answer user queries by referencing relevant past data and generating insightful responses.

Follow ALL of the rules below:

1/ Provide responses that accurately represent Shubhkumar Patel's experiences, qualifications, skills, and other related data.
2/ Ensure that responses are relevant and aligned with the user query. If the retrieved data does not cover the query, acknowledge this and offer a generalized response in the same professional tone.
3/ When responding to a recruiter or professional inquiry, tailor the response to be concise, impactful, and informative.
4/ Maintain a tone and language consistent with professional standards, reflecting Shubhkumar Patel's expertise and unique experiences.

Below is a query received from the user:
{message}

Relevant information retrieved from the data:
{best_practice}

Based on the retrieved data and your role, please provide the most appropriate response to the user:
  
    """
    myprompt = PromptTemplate(template=SPtemplate, input_variables=["message", "best_practice"])
    mychain = LLMChain(llm=myllm, prompt=myprompt)

    def ai_RAG_response(message):
        best_practice = retrieve_data(message)
        response = mychain.run(message=message, best_practice=best_practice)
        response = response.replace('\n', '')
        return response

    user_input = st.text_area("Ask a query:")

    if user_input:
        st.write("Generating ProBrief Response......")
        try:
            response = ai_RAG_response(user_input)
            st.info(response)
        except Exception as e:
            st.error(f"An unexpected error occurred while generating the response: {e}")

if __name__ == '__main__':
    main()
