# main.py
from fastapi import FastAPI
from pydantic import BaseModel # Pydantic se usa para validar datos de entrada
from langchain_ollama import OllamaLLM as Ollama 

app = FastAPI()

# Modelo por defecto
MODEL_NAME = "deepseek-coder-v2"
llm = Ollama(model=MODEL_NAME)

#Pydantic
#estructura esperada del JSON de entrada.
#{ "prompt": "Hola, ¿qué es Python?" }
class Query(BaseModel):
    prompt: str

@app.post("/ask") # Decorador de ruta HTTP "Asocia esta función a una ruta HTTP POST en /ask
async def ask_model(query: Query):
    try:
        result = llm.invoke(query.prompt)
        return {"response": result}
    except Exception as e:
        return {"error": str(e)}
