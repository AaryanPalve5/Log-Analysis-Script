import os
import logging
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# Function to query RAG model with dynamic user input
def query_rag(question: str) -> str:
    PROMPT_TEMPLATE = """
    You are an assistant providing analysis based on the log and result data.

    Related Data:
    {context}

    Please answer the question based on the provided data.

    Question:

    {question}
    """
    try:
        # Reading data from sample.log and log_analysis_results.csv
        log_file = "sample.log"
        csv_file = "log_analysis_results.csv"
        
        log_context = ""
        csv_context = ""

        # Reading the log file for context
        with open(log_file, "r", encoding="utf-8") as f:
            log_context = f.read()

        # Reading the CSV results for context
        with open(csv_file, "r", encoding="utf-8") as f:
            csv_context = f.read()

        # Combining both sources of context
        full_context = log_context + "\n" + csv_context

        # Set up the embedding function for the Google Generative AI model
        db = Chroma(
            persist_directory="chroma_stock",
            embedding_function=GoogleGenerativeAIEmbeddings(
                model="models/embedding-001"
            ),
            collection_name="log_data",
        )

        db.add_texts([full_context])

        # Perform similarity search and generate context for the question
        results = db.similarity_search_with_score(question, k=len(db.get()["ids"]))
        context_text = " ".join([doc.page_content for doc, _score in results])

        # Format the prompt with the gathered context and user question
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context_text, question=question)

        # Use Google Gemini to get the answer
        model = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash", api_key=os.getenv("GOOGLE_API_KEY")
        )
        response = model.invoke(prompt)
        
        if hasattr(response, "content"):
            return response.content.strip()
        return str(response).strip()

    except Exception as e:
        logging.error(f"Error in query_rag: {e}")
        return "An error occurred while processing the query."

# Main function to allow dynamic terminal input
def main() -> None:
    print("Welcome to the Log Query Bot! Type 'exit' to quit.")
    
    while True:
        # Get user input dynamically
        question = input("Enter your query: ").strip()

        if question.lower() == 'exit':
            print("Exiting the chat. Goodbye!")
            break
        
        # Get the response from the Gemini model based on user input
        response = query_rag(question=question)
        print(f"Response: {response}")

if __name__ == "__main__":
    main()
