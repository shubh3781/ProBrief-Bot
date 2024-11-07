
---

# ProBrief Bot

ProBrief is an interactive chatbot application designed to provide instant responses about Shubhkumar Patel’s professional and academic background. By leveraging state-of-the-art natural language processing capabilities, ProBrief offers accurate, real-time responses tailored to user queries, helping streamline engagement with recruiters and other interested parties.

## Table of Contents
- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [How to Use](#how-to-use)
- [Application Architecture](#application-architecture)
- [Code Explanation](#code-explanation)
- [Conclusion](#conclusion)

---

## Introduction

ProBrief is designed to automate the process of sharing detailed information about Shubhkumar Patel's professional journey. It eliminates the need for direct communication or scheduling by providing immediate, accurate responses to queries, making it easier for recruiters and other professionals to connect without delays.

## Problem Statement

In professional networking and recruitment, efficiently presenting one's background and experience is crucial. Time zones, availability, and response delays can create friction. ProBrief addresses this problem by offering a chatbot that instantly retrieves and shares relevant information about Shubhkumar Patel, enhancing accessibility and engagement without requiring his immediate presence.

## Features

- **User-friendly Interface**: Easy-to-use interface powered by Streamlit.
- **Real-time Responses**: Instant responses tailored to user queries.
- **AI-Driven Insights**: Integrates LangChain for query processing.
- **Data Retrieval and Similarity Search**: Utilizes FAISS for efficient similarity search.
- **Custom Styling and Aesthetics**: Interactive and visually appealing design using Streamlit customizations.

## Technologies Used

- **Programming Language**: Python
- **Framework**: Streamlit
- **Language Model**: Google Generative AI (Gemini)
- **Libraries**: LangChain, FAISS, dotenv, LangChain Community Document Loaders
- **Embeddings**: Google Generative AI Embeddings

## Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd ProBrief
    ```

2. **Install Dependencies**:
    Ensure you have Python installed. Run the following command to install required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    Start the Streamlit app with:
    ```bash
    streamlit run ProBrief.py
    ```

## How to Use

1. **Enter API Key**:
   - Enter your Gemini API key in the input field to authenticate and access AI capabilities.

2. **Ask Queries**:
   - Use the text area to ask questions related to Shubhkumar Patel’s background.
   - Click the submit button to receive a response.

3. **View Responses**:
   - The chatbot will generate and display relevant responses based on available data.

## Application Architecture

1. **Data Loading and Preprocessing**:
   - Data about Shubhkumar Patel’s background is loaded from a CSV file using LangChain's `CSVLoader`.
   
2. **Embedding Generation**:
   - Data is embedded using Google Generative AI embeddings for efficient similarity search.

3. **Vector Store Creation**:
   - FAISS is used as a vector store for fast and accurate similarity searches.

4. **LLM Interaction**:
   - LangChain's `LLMChain` and `PromptTemplate` generate responses based on user queries and retrieved data.

5. **Custom Styling and Design**:
   - The Streamlit interface is customized with a background color and animations to enhance user experience.

## Code Explanation

### Key Components

1. **`main()` Function**:
   - Sets up the Streamlit page, header, and user input elements.
   - Handles API key input and validation.

2. **Data Retrieval**:
   - Uses `CSVLoader` to load data.
   - Embeds data using Google Generative AI embeddings and stores it in a FAISS vector store.

3. **Response Generation**:
   - The `ai_RAG_response` function handles user input and generates responses using LangChain's `LLMChain`.

4. **User Interaction**:
   - Provides a text area for users to input queries and displays responses using Streamlit.

### Sample Code Snippet

```python
def retrieve_data(query):
    similar_response = db.similarity_search(query)
    entire_data = [doc.page_content for doc in similar_response]
    return entire_data

def ai_RAG_response(message):
    best_practice = retrieve_data(message)
    response = mychain.run(message=message, best_practice=best_practice)
    return response.replace('\n', '')
```

## Conclusion

ProBrief offers a robust solution to the challenges of providing timely, accurate, and detailed professional information. By integrating state-of-the-art AI technologies, it ensures that potential recruiters and interested parties can easily access information about Shubhkumar Patel, fostering better connections and professional visibility.

---
