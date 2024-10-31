# AI Used Car Recommendation Chatbot

## Project Description
This project is a proof-of-concept demonstration of an AI-powered chatbot that recommends used cars to users based on their preferences. The chatbot leverages OpenAI's GPT-4 model and LangChain to provide personalized car recommendations in a conversational manner.

The cars available for recommendation are listed in the `cars.json` file. The chatbot performs Retrieval Augmented Generation (RAG) on the `cars.json` file to create a vector store for efficient data retrieval. If the `db` folder does not exist when the application is first run, the RAG process will initialize the vector store.

## Project Requirements
- Python 3.11
- Poetry (Dependency Management)
- OpenAI API Key

## Installation Process

### Clone the Repository

```bash
git clone https://github.com/yourusername/car-recommender-chatbot.git
cd car-recommender-chatbot
```

### Install Poetry

If you haven't installed Poetry yet, you can install it using the following command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Or refer to the official [Poetry installation guide](https://python-poetry.org/docs/) for alternative methods.

### Install Project Dependencies

Use Poetry to install the required dependencies:

```bash
poetry install
```

### Set Up Environment Variables

Rename the `.env.example` file to `.env` and add your OpenAI API key:

```bash
mv .env.example .env
```

Open the `.env` file in a text editor and insert your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Running the Application
After completing the installation and setup, you can run the chatbot with the following command:

```bash
poetry run python main.py
```

This will start the chatbot, and you can begin interacting with it in your terminal.

## Prompts

### Contextualize Question System Prompt (`contextualize_q_system_prompt`)

**Purpose**: To reformulate the user's question by incorporating the entire chat history. This ensures that references to previous interactions are understood in context, enabling more accurate searches in the vector store.

**Function**: Before performing a search, the chatbot rewrites the user's query as a standalone question that can be understood without additional context.

### Question Answering System Prompt (`qa_system_prompt`)

**Purpose**: To act as a helpful assistant that directly answers the user's questions and provides car recommendations.

**Function**: Guides the chatbot to use retrieved car information to generate concise and relevant responses, focusing on recommending cars based on the user's stated preferences.

## Additional Information

### Data Processing:
- The chatbot reads car data from the `cars.json` file.
- It converts each car's information into natural language descriptions.
- These descriptions are used to create embeddings via OpenAI's embedding models.
- The embeddings are stored in a vector store using Chroma for efficient retrieval.

### Retrieval Augmented Generation (RAG):
- RAG enhances the chatbot's ability to provide accurate and contextually relevant recommendations.
- It combines large language models with external knowledge sources (the car data) during response generation.

### Example Questions:
Upon starting the chatbot, you will see an introduction message with example questions you can ask:

```vbnet
Welcome to Sallies Used Cars recommendation chatbot. Here is a list of questions you can ask the chatbot for a good recommendation:
1. Do you have any cars running on gasoline fuel type?
2. What are the prices and makes of cars you have available from 2020?
3. Can you tell me if you have any hatchbacks?
4. I am looking for a Sedan.
5. I am looking for a nice car from 2020 with heated seats.
```

## Contributing
This is just a demo, for portfolio purposes.

## License
This project is licensed under the MIT License.
