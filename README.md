# Agente LLM con FastAPI + Ollama

Este proyecto es un microservicio basado en FastAPI que expone un endpoint para interactuar con modelos LLM locales (como DeepSeek o Mistral) a través de Ollama.

---

## 🚀 Requisitos

- Python 3.12
- Docker + Docker Compose
- Ollama instalado y corriendo en el host
- Git

---

## 🐧 Instalación en local (WSL/Linux/macOS)

```bash
git clone git@github.com:TU_USUARIO/agente-llm.git
cd agente-llm
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

---

## 💻 Instalación en Windows

> Requiere [Docker Desktop](https://www.docker.com/products/docker-desktop/) con **WSL 2 integrado** y **Ollama instalado en Windows**.

1. Clona el repositorio (Git Bash, PowerShell o SourceTree):

    ```bash
    git clone git@github.com:TU_USUARIO/agente-llm.git
    ```

2. Abre el proyecto con VSCode o entra con PowerShell:

    ```bash
    cd agente-llm
    ```

3. Asegúrate de que Ollama está ejecutándose en Windows:

    ```bash
    ollama serve
    ```

4. Ejecuta el contenedor con Docker:

    ```bash
    docker compose up --build
    ```

Accede a la API en: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📦 Endpoints

### POST `/ask`

Envía un prompt al modelo LLM.

#### 📥 Ejemplo de request

```json
{
  "prompt": "Escribe un script en Python que calcule la serie de Fibonacci"
}
```

#### 📤 Ejemplo de respuesta

```json
{
  "response": "Aquí tienes un ejemplo de código en Python..."
}
```

---

## ⚙️ Variables de entorno

- `OLLAMA_HOST` – Dirección del servidor Ollama (por defecto: `host.docker.internal:11434` en Docker)

---

## 🧠 Modelo usado

- Modelo por defecto: `deepseek-coder-v2:latest`
- Puedes cambiarlo fácilmente en `main.py`

---

## 🧪 To Do

- [ ] Añadir tests
- [ ] Mejorar manejo de errores
- [ ] Exponer más funcionalidades de Ollama

---

## 🐍 Entorno virtual perdido o ausente

Si la carpeta `.venv/` no está en el proyecto (por ejemplo, al clonar desde GitHub), puedes recrearla fácilmente:

### En WSL / Linux / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### En Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

---

## 💡 Notas

- Usa claves SSH para autenticarte con GitHub desde WSL o Windows.
- Puedes trabajar directamente desde VSCode o SourceTree en esta ruta:
  ```
  \\wsl.localhost\Ubuntu\home\tu_usuario\agente-llm\
  ```
