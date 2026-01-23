# Terminal AI Assistant

Un asistente inteligente para la terminal que utiliza múltiples agentes de IA gratuitos para responder preguntas y proporcionar soluciones en el terminal.

## 📋 Descripción

Terminal AI Assistant es un proyecto que integra varios proveedores de IA gratuitos (Groq, Cerebras, Google Gemini) y los llama en rotación para procesar consultas. El sistema distribuye las preguntas entre los agentes disponibles de manera equilibrada, proporcionando respuestas de streaming directamente en la terminal.

## 🎯 Características

- **Múltiples Agentes de IA**: Integración con 3 proveedores gratuitos:
  - **Groq**: API rápida y eficiente
  - **Cerebras**: Procesamiento potente de IA
  - **Google Gemini**: Modelo avanzado de Google
  
- **Rotación Automática**: Los agentes se llaman en orden rotativo para distribuir la carga
- **Streaming de Respuestas**: Las respuestas se entregan en tiempo real mediante streaming
- **Persistencia de Estado**: Mantiene el seguimiento del agente actual en `data.json`
- **Sin Costo**: Utiliza APIs gratuitas

## 🏗️ Estructura del Proyecto

```
terminal_ai/
├── src/
│   ├── local.py                 # Script principal
│   └── agents/
│       ├── __init__.py
│       ├── groq_client.py       # Agente Groq
│       ├── cerebras_client.py   # Agente Cerebras
│       └── gemini_client.py     # Agente Gemini
├── data.json                    # Archivo de persistencia del estado
├── requirements.txt             # Dependencias del proyecto
└── README.md                    # Este archivo
```

## 📦 Instalación

### Requisitos Previos
- Python 3.8+
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. Clona o descarga el proyecto:
```bash
cd terminal_ai
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Configura las variables de entorno (`.env`):
```bash
# Groq API
GROQ_API_KEY=tu_groq_api_key

# Cerebras API
CEREBRAS_API_KEY=tu_cerebras_api_key

# Google Gemini API
GOOGLE_API_KEY=tu_google_api_key
```

## 🚀 Uso

### Uso Básico

```bash
python src/local.py
```

El script realizará una consulta de demostración (Fibonacci en Python) y mostrará la respuesta del siguiente agente disponible.

### Integración en tu código

```python
from agents import groqAgent, cerebrasAgent, geminiAgent
from src.local import ask_agents

# Realizar una pregunta
for chunk in ask_agents("¿Cómo se implementa merge sort en Python?"):
    print(chunk, end="")
```

## 🔄 Cómo Funciona

1. **Carga del Estado**: El programa lee `data.json` para saber cuál fue el último agente utilizado
2. **Rotación**: El siguiente agente en la lista se selecciona automáticamente
3. **Consulta**: La pregunta se envía al agente seleccionado
4. **Streaming**: La respuesta se entrega mediante streaming de texto
5. **Persistencia**: El estado se actualiza en `data.json` para la próxima consulta

## 🤖 Agentes Disponibles

### GroqAgent
- **Modelo**: moonshotai/kimi-k2-instruct-0905
- **Características**: Rápido, eficiente, ideal para consultas simples
- **Archivo**: [src/agents/groq_client.py](src/agents/groq_client.py)

### CerebrasAgent
- **Características**: Procesamiento potente, ideal para problemas complejos
- **Archivo**: [src/agents/cerebras_client.py](src/agents/cerebras_client.py)

### GeminiAgent
- **Características**: Modelo avanzado de Google, versátil
- **Archivo**: [src/agents/gemini_client.py](src/agents/gemini_client.py)

## 📝 Archivo de Configuración

El archivo `data.json` almacena el índice del agente actual:

```json
{
    "current_agent": 1
}
```

Este valor se incrementa automáticamente cada vez que se realiza una consulta, permitiendo la rotación entre agentes.

## 🔧 Configuración

Puedes personalizar el comportamiento modificando:

- **Temperatura**: En cada cliente de agente (controla la creatividad)
- **max_completion_tokens**: Longitud máxima de la respuesta
- **top_p**: Núcleo de muestreo para diversidad
- **Orden de agentes**: Modifica la lista `agents` en [src/local.py](src/local.py)

## 📚 Dependencias Principales

- `groq`: Cliente SDK de Groq
- `cerebras_cloud_sdk`: SDK de Cerebras
- `google-genai`: API de Google Generative AI
- `python-dotenv`: Manejo de variables de entorno

Ver [requirements.txt](requirements.txt) para la lista completa.

## 🐛 Solución de Problemas

### Error: "API Key no encontrada"
- Verifica que el archivo `.env` existe y contiene las claves correctas
- Asegúrate de que las variables de entorno están configuradas correctamente

### El agente no responde
- Verifica tu conexión a internet
- Comprueba que las claves API son válidas y tienen saldo/límite disponible
- Revisa los logs de error del SDK correspondiente

### Respuesta vacía o truncada
- Intenta aumentar `max_completion_tokens` en el cliente del agente
- Verifica que la pregunta está bien formulada

## 🔐 Seguridad

- **Nunca** hagas commit de tu `.env` con las claves API
- Asegúrate de que `.env` está en `.gitignore`
- Usa credenciales separadas para desarrollo y producción

## 📄 Licencia

Este proyecto es de código abierto. Siéntete libre de usarlo y modificarlo.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si encuentras errores o tienes sugerencias, por favor reporta un issue o abre un pull request.

## ✉️ Contacto

Para preguntas o sugerencias, abre un issue en el repositorio.

---

**Última actualización**: Enero 2026
