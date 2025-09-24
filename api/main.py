import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize the Groq model
llm = ChatGroq(
    api_key=groq_api_key,
    model_name="llama-3.3-70b-versatile",  # or "llama3-8b-8192", etc.
    temperature=0 # temp 0=low creativity and 1 is super high creativity <3
)

# Persistent memory using ConversationBufferMemory
memory = ConversationBufferMemory(return_messages=True) # true=llm gets full memory false=llm gets no memory thus useless <3

# Conversation Chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True # true=llm background tasks also printed false=not printed
)

def chat(input_message:str):
    response = conversation.predict(input=input_message)
    # messages = memory.chat_memory.messages
    return response

