# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_ollama import OllamaLLM as Ollama #from langchain_community.llms import Ollama

app = FastAPI()

# Modelo por defecto
MODEL_NAME = "deepseek-coder-v2:16b"
llm = Ollama(model=MODEL_NAME)

class Query(BaseModel):
    prompt: str

@app.post("/ask")
async def ask_model(query: Query):
    try:
        result = llm.invoke(query.prompt)
        return {"response": result}
    except Exception as e:
        return {"error": str(e)}
