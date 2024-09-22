from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.1")
template = """
Answer the question below
Here is the conversation history: {context}

Question: {question}
Answer: 
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def get_response(context, question):
    return chain.invoke({"context": context, "question": question})
