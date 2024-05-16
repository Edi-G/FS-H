import streamlit as st
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
import openai
from llama_index.core import SimpleDirectoryReader
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI

openai.api_key = st.secrets.openai_key
llm = OpenAI(model="gpt-4-turbo", temperature=0.4)

st.title('🐟 FSH')

# Initialize chat history
if "messages" not in st.session_state.keys(): # Initialize the chat message history
    st.session_state.messages = [
        {"role": "assistant", "content": "Still meg et spørsmål om UIA sitt FS system!"}
    ]

@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Laster inn kunnskapsbasen. Dette kan ta noen minutter."):
        reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
        docs = reader.load_data()
        index = VectorStoreIndex.from_documents(docs)
        return index

index = load_data()

if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_plus_context",
                                                            llm=llm,
                                                            system_prompt =(
                                                                "As an expert on the FS system at the University of Agder, it is crucial that ,"
                                                                " you always respond in the query's language. Your primary responsibility is to "
                                                                " provide detailed answers based on the knowledgebase. When providing "
                                                                " instructions from the article body, ensure that they are structured in a clear and "
                                                                " organized manner so that the user can easily follow them. Additionally, make sure "
                                                                " that each response includes the URL from the knowledgebase for the relevant UIA "
                                                                " ServiceNow guidance referenced in the query. This will help avoid referencing "
                                                                " incorrect or non-existent links."
                                                                ),
                                                            verbose=True)

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history

