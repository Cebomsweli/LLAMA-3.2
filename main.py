from langchain_ollama import OllamaLLM #Imported from ollama
from langchain_core.prompts import ChatPromptTemplate # To easily assembly chats

model=OllamaLLM(model="llama3.2") #The model i am working with

template="""
 Answer the question below.
 
 Here is the conversation history: {context}
 Question: {question}
 Answer:
"""
result=model.invoke(input="")
prompt=ChatPromptTemplate.from_template(template)
chain=prompt|model

def handle_conversation():
    context=""
    print("Welcome to the AI ChatBot!, Type 'exit' to quit.")
    while True:
        user_input=input("You: ")
        if user_input.lower()=="exit":
            break
        
        result=chain.invoke({"context": context,"question": user_input})
        print("Bot: ",result)
        #To ensure that the bot can refer to history
        context +=f"\nUser:{user_input}\nAI: {result}"

if __name__=="__main__":
    handle_conversation()