---

# ProBrief Bot

Welcome to ProBrief! This project is designed to create a chatbot that provides information about Shubhkumar Patel’s professional and academic journey using the power of LLMs (Large Language Models) and LangChain. The bot intelligently retrieves relevant data and presents responses tailored to user queries, such as those from recruiters or other interested parties.

## Project Overview

ProBrief utilizes an LLM-driven approach combined with a LangChain agent to deliver accurate responses about Shubhkumar Patel's background. The data is stored in a pipe-separated CSV file where each entry is structured in a question-answer format. When a user submits a query, the following process occurs:

1. **Embedding and Retrieval**: 
   - The query is embedded using Google Generative AI embeddings (via the `GoogleGenerativeAIEmbeddings` model).
   - The system leverages the FAISS (Facebook AI Similarity Search) vector store to perform a similarity search, retrieving the most relevant information from the CSV file.

2. **LLM Refinement with Gemini**:
   - The retrieved data is fed into a large language model, specifically the Gemini LLM (`gemini-1.5-pro-002`), via LangChain’s `LLMChain`.
   - The LLM, guided by a rule-based prompt, crafts a well-structured, professional response based on the retrieved data.

3. **LangChain Agent**:
   - LangChain serves as the integration backbone, enabling seamless interactions between the CSV data, embeddings, and LLM to generate high-quality responses.
   - This approach, known as **Retrieval Augmented Generation (RAG)**, ensures that user queries are met with precise and contextually relevant responses.

## Technologies and Techniques Used

- **LLM (Gemini)**: Used for generating refined, professional responses. The choice of Gemini is due to its ease of access, as it requires only a Google account to obtain an API key from Google AI Studio, making it freely accessible for most users.
- **LangChain**: Enables interaction with LLMs and data sources, creating chains to retrieve and process information effectively.
- **FAISS Vector Store**: Used to perform similarity searches on embeddings to identify relevant pieces of information.
- **Google Generative AI Embeddings**: Provides embeddings for text data, crucial for the retrieval step.
- **CSV Data Storage**: Data is stored in a pipe-separated CSV file with question-answer format for easy retrieval and processing.

## Requirements

- Python 3.7+
- Streamlit for the web interface
- LangChain for LLM and data management
- FAISS for similarity search
- `langchain_google_genai` for Google Generative AI models
- dotenv for environment variable management
- A pipe-separated CSV file containing your data in the format:
  ```
  Question|Answer
  ```

## How to Use

1. **Clone the Repository**:
   ```
   git clone https://github.com/shubh3781/ProBrief-Bot
   cd ProBrief-Bot
   ```

2. **Install Dependencies**:
   Make sure you have all necessary packages installed:
   ```
   pip install -r requirements.txt
   ```

3. **Prepare Your Data**:
   Create a CSV file (`your_file.csv`) with the structure:
   ```
   Question|Answer
   ```
   Replace the content with relevant data.

4. **Run the Application**:
   ```
   streamlit run your_script.py
   ```

5. **Usage**:
   - Enter your Gemini API key when prompted.
   - Ask questions in the text area to get responses about the data provided.

## Why Use Gemini LLM?

- **Free and Easy Access**: Gemini LLM is freely accessible to users with a Google account. API keys can be generated instantly via [Google AI Studio](https://aistudio.google.com/apikey).
- **Strong Capabilities**: It offers powerful generation capabilities for refining retrieved data and producing professional-quality responses.

## Customizing for Different Data

To customize ProBrief for different datasets:
1. Replace the CSV file with a new file containing your data.
2. Ensure your file follows the pipe-separated question-answer format (`Question|Answer`).
3. Modify any embeddings, models, or prompt templates to better suit your data and use case.

## Example Usage

1. **Load Data**:
   The CSV data is loaded using a CSV loader.
2. **Retrieve Relevant Information**:
   FAISS is used to find similar content based on the user’s query.
3. **Generate a Response**:
   Gemini LLM, via LangChain, creates a well-structured response, guided by rules and templates to ensure accuracy and relevance.

---

Enjoy using ProBrief, and make it yours by tailoring it with your data and requirements! For any contributions or issues, please raise them on our GitHub page.

---
