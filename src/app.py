from fastapi import FastAPI
from helper import process_input

app = FastAPI(title="Medical Chatbot")

@app.get("/")
def home():
    return {"message": "Welcome to the Medical Chatbot API!"}

@app.get("/ask")
def ask_bot(question: str):
    response = process_input(question)
    return {"question": question, "response": response}
