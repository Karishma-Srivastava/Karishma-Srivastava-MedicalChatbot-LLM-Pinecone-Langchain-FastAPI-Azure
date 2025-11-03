from fastapi import FastAPI
from chatbot.chatbot_logic import get_medical_response

app = FastAPI(title="Medical Chatbot")

@app.get("/")
def home():
    return {"message": "Welcome to the Medical Chatbot API!"}

@app.get("/ask")
def ask_bot(question: str):
    response = get_medical_response(question)
    return {"question": question, "response": response}
