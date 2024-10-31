import os
from dotenv import load_dotenv
import pandas as pd

from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

load_dotenv()

def doRag():
    # Define the directory containing the JSON file and the persistent directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    cars_dir = os.path.join(current_dir, "cars")
    db_dir = os.path.join(current_dir, "db")
    persistent_directory = os.path.join(db_dir, "chroma_db_with_metadata")

    print(f"Cars directory: {cars_dir}")
    print(f"Persistent directory: {persistent_directory}")

    # Path to the cars.json file
    cars_json_path = os.path.join(cars_dir, "cars.json")

    # Check if the Chroma vector store already exists
    if not os.path.exists(persistent_directory):
        print("Persistent directory does not exist. Initializing vector store...")

        # Ensure the cars.json file exists
        if not os.path.exists(cars_json_path):
            raise FileNotFoundError(
                f"The file {cars_json_path} does not exist. Please check the path."
            )

        # Load the car data from the JSON file using pandas
        df = pd.read_json(cars_json_path)

        # Create a list to hold the documents
        documents = []

        # Iterate over each row in the DataFrame and create a description
        for index, row in df.iterrows():
            # Create a natural language description of the car
            car_description = (
                f"The {row['year']} {row['make']} {row['model']} is a {row['type']} "
                f"with a minimum price of ${row['minimum_price']}. "
                f"It runs on {row['fuel_type']} and offers features like {', '.join(row['features'])}."
            )

            # Convert the 'features' list into a string for metadata
            metadata = row.to_dict()
            metadata['features'] = ', '.join(row['features'])

            # Create a Document object with the description and metadata
            doc = Document(
                page_content=car_description,
                metadata=metadata
            )
            print(car_description)

            documents.append(doc)

        # Split the documents into chunks if necessary
        text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)

        # Display information about the split documents
        print("\n--- Document Chunks Information ---")
        print(f"Number of document chunks: {len(docs)}")

        # Create embeddings
        print("\n--- Creating embeddings ---")
        embeddings = OpenAIEmbeddings(
            model="text-embedding-ada-002"
        )
        print("\n--- Finished creating embeddings ---")

        # Create the vector store and persist it
        print("\n--- Creating and persisting vector store ---")
        db = Chroma.from_documents(
            docs, embeddings, persist_directory=persistent_directory
        )
        db.persist()
        print("\n--- Finished creating and persisting vector store ---")

    else:
        print("Vector store already exists. No need to initialize.")

if __name__ == "__main__":
    doRag()
