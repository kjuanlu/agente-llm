import sys
import requests
import base64
import os
import json

# Verificar argumento
if len(sys.argv) < 2:
    print("Uso: python test_llava.py /ruta/a/la/imagen.jpg")
    exit(1)

image_path = sys.argv[1]

if not os.path.isfile(image_path):
    print(f"❌ No se encontró el archivo: {image_path}")
    exit(1)

# Codificar imagen
with open(image_path, 'rb') as f:
    image_base64 = base64.b64encode(f.read()).decode('utf-8')

# Preguntar prompt
prompt = input("¿Qué quieres preguntarle a la imagen?: ")

# Enviar a Ollama
response = requests.post(
    'http://localhost:11434/api/generate',
    json={
        'model': 'llava',
        'prompt': prompt,
        'images': [image_base64],
        'stream': True
    },
    stream=True
)

# Mostrar respuesta
print("\n🧠 Respuesta del modelo:")
for line in response.iter_lines():
    if line:
        try:
            data = json.loads(line.decode('utf-8'))
            print(data.get('response', ''), end='', flush=True)
        except json.JSONDecodeError as e:
            print("\n⚠️ Error procesando línea JSON:", line.decode('utf-8'))
