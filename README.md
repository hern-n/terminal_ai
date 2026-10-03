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
- Conexión a internet
- Claves API para Groq, Cerebras y Google Gemini

### Instalación por Sistema Operativo

---

#### 🪟 Windows

**Método 1: Usando Python oficial**

1. **Instalar Python**:
   - Descarga Python 3.8+ desde [python.org](https://www.python.org/downloads/)
   - Durante la instalación, marca "Add Python to PATH"

2. **Verificar instalación**:
   ```cmd
   python --version
   pip --version
   ```

3. **Clonar el proyecto**:
   ```cmd
   git clone https://github.com/tu-usuario/terminal_ai.git
   cd terminal_ai
   ```

4. **Crear entorno virtual (recomendado)**:
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

5. **Instalar dependencias**:
   ```cmd
   pip install -r requirements.txt
   ```

**Método 2: Usando Windows Package Manager (winget)**
```cmd
winget install Python.Python.3.11
git clone https://github.com/tu-usuario/terminal_ai.git
cd terminal_ai
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**Método 3: Usando Chocolatey**
```cmd
choco install python git
git clone https://github.com/tu-usuario/terminal_ai.git
cd terminal_ai
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

#### 🐧 Linux (Ubuntu/Debian)

1. **Instalar Python y herramientas básicas**:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv git
   ```

2. **Verificar instalación**:
   ```bash
   python3 --version
   pip3 --version
   ```

3. **Clonar el proyecto**:
   ```bash
   git clone https://github.com/tu-usuario/terminal_ai.git
   cd terminal_ai
   ```

4. **Crear y activar entorno virtual**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

5. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

**Para otras distribuciones Linux:**

- **Fedora/CentOS/RHEL**:
  ```bash
  sudo dnf install python3 python3-pip git
  ```

- **Arch Linux**:
  ```bash
  sudo pacman -S python python-pip git
  ```

---

#### 🍎 macOS

**Método 1: Usando Homebrew (recomendado)**

1. **Instalar Homebrew** (si no lo tienes):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Instalar Python**:
   ```bash
   brew install python@3.11 git
   ```

3. **Verificar instalación**:
   ```bash
   python3 --version
   pip3 --version
   ```

4. **Clonar el proyecto**:
   ```bash
   git clone https://github.com/tu-usuario/terminal_ai.git
   cd terminal_ai
   ```

5. **Crear y activar entorno virtual**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

6. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

**Método 2: Usando MacPorts**
```bash
sudo port install python311 py311-pip git
git clone https://github.com/tu-usuario/terminal_ai.git
cd terminal_ai
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Método 3: Descarga directa desde python.org**
- Descarga Python 3.8+ desde [python.org](https://www.python.org/downloads/macos/)
- Sigue los pasos similares a Windows pero usando `python3` y `pip3`

---

#### 🐧 Docker (Universal)

1. **Crear Dockerfile** (si no existe):
   ```dockerfile
   FROM python:3.11-slim
   
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   
   COPY . .
   CMD ["python", "src/local.py"]
   ```

2. **Construir y ejecutar**:
   ```bash
   docker build -t terminal-ai .
   docker run --rm -it -e GROQ_API_KEY=tu_key -e CEREBRAS_API_KEY=tu_key -e GOOGLE_API_KEY=tu_key terminal-ai
   ```

---

### Configuración de Variables de Entorno

**Método 1: Archivo .env (Recomendado)**
```bash
# Crea un archivo .env en la raíz del proyecto
# Groq API
GROQ_API_KEY=tu_groq_api_key

# Cerebras API
CEREBRAS_API_KEY=tu_cerebras_api_key

# Google Gemini API
GOOGLE_API_KEY=tu_google_api_key
```

**Método 2: Variables de entorno del sistema**

**Windows (cmd)**:
```cmd
set GROQ_API_KEY=tu_groq_api_key
set CEREBRAS_API_KEY=tu_cerebras_api_key
set GOOGLE_API_KEY=tu_google_api_key
```

**Windows (PowerShell)**:
```powershell
$env:GROQ_API_KEY="tu_groq_api_key"
$env:CEREBRAS_API_KEY="tu_cerebras_api_key"
$env:GOOGLE_API_KEY="tu_google_api_key"
```

**Linux/macOS**:
```bash
export GROQ_API_KEY=tu_groq_api_key
export CEREBRAS_API_KEY=tu_cerebras_api_key
export GOOGLE_API_KEY=tu_google_api_key
```

**Para hacer permanentes las variables:**
- **Linux/macOS**: Añadir al archivo `~/.bashrc`, `~/.zshrc` o `~/.profile`
- **Windows**: Panel de Control > Sistema > Variables de entorno

### Obtener Claves API

1. **Groq API Key**:
   - Regístrate en [console.groq.com](https://console.groq.com/)
   - Crea una nueva API key en la sección de API Keys

2. **Cerebras API Key**:
   - Regístrate en [cerebras.ai](https://cerebras.ai/)
   - Obtén tu API key desde el dashboard

3. **Google Gemini API Key**:
   - Ve a [ai.google.dev](https://ai.google.dev/)
   - Crea un proyecto y genera una API key en Google AI Studio

### Verificación de Instalación

Después de instalar, ejecuta una prueba:

```bash
# Si usas entorno virtual, asegúrate de que esté activado
python src/local.py
```

Si todo está configurado correctamente, deberías ver una respuesta de uno de los agentes de IA.

## 🚀 Uso

### Uso Básico

```bash
python src/local.py
```

El script realizará una consulta de demostración (Fibonacci en Python) y mostrará la respuesta del siguiente agente disponible.

### Modo Interactivo

Para usar el asistente en modo interactivo:

```bash
# Ejecuta el script en modo interactivo
python src/local.py --interactive

# Luego puedes hacer preguntas directamente:
> ¿Cómo funciona un algoritmo de búsqueda binaria?
> Explica los principios SOLID en programación
> Ayúdame a optimizar este código Python...
```

### Integración como Módulo

```python
from agents import groqAgent, cerebrasAgent, geminiAgent
from src.local import ask_agents

# Realizar una pregunta
for chunk in ask_agents("¿Cómo se implementa merge sort en Python?"):
    print(chunk, end="")
```

### Uso Avanzado

```python
import asyncio
from src.local import ask_agents_async

# Uso asíncrono para múltiples consultas
async def main():
    questions = [
        "¿Qué es la programación funcional?",
        "Explica los patrones de diseño",
        "¿Cómo funciona el machine learning?"
    ]
    
    tasks = [ask_agents_async(q) for q in questions]
    results = await asyncio.gather(*tasks)
    
    for i, result in enumerate(results):
        print(f"Question {i+1}: {result}")

asyncio.run(main())
```

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

### Problemas Comunes de Instalación

#### Python no encontrado
**Windows**:
```cmd
# Asegúrate que Python está en el PATH
where python
# Si no aparece, reinstala Python marcando "Add Python to PATH"
```

**Linux/macOS**:
```bash
# Verifica la instalación
which python3
# Si no aparece, instala con el gestor de paquetes correspondiente
```

#### Error de permisos
**Linux/macOS**:
```bash
# Usa un entorno virtual para evitar permisos globales
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Windows** (ejecutar como administrador):
```cmd
pip install -r requirements.txt --user
```

#### Problemas con dependencias específicas

**Error con compilación C en Linux**:
```bash
sudo apt install python3-dev build-essential
pip install -r requirements.txt
```

**Error en macOS con Xcode**:
```bash
xcode-select --install
pip install -r requirements.txt
```

### Errores de Ejecución

#### Error: "API Key no encontrada"
- Verifica que el archivo `.env` existe en la raíz del proyecto
- Confirma las claves están escritas correctamente
- Prueba exportando las variables manualmente:
  ```bash
  export GROQ_API_KEY=tu_key
  python src/local.py
  ```

#### Error: "module not found"
```bash
# Asegúrate de estar en el entorno virtual
# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

# Reinstala dependencias
pip install -r requirements.txt
```

#### El agente no responde
- Verifica tu conexión a internet
- Comprueba que las claves API son válidas y tienen saldo/límite disponible
- Revisa los logs de error del SDK correspondiente
- Prueba con un solo agente para aislar el problema

#### Respuesta vacía o truncada
- Intenta aumentar `max_completion_tokens` en el cliente del agente
- Verifica que la pregunta está bien formulada
- Revisa los límites de la API del proveedor

### Problemas Específicos por Sistema Operativo

#### Windows
- **Error de SSL**: Actualiza certificados con Windows Update
- **Firewall corporativo**: Configura proxy si es necesario:
  ```cmd
  set HTTPS_PROXY=http://proxy.company.com:port
  set HTTP_PROXY=http://proxy.company.com:port
  ```

#### Linux
- **Error de librerías faltantes**:
  ```bash
  sudo apt install libssl-dev libffi-dev
  ```

#### macOS
- **Problemas con certificados**:
  ```bash
  /Applications/Python\ 3.11/Install\ Certificates.command
  ```

### Depuración Avanzada

#### Habilitar modo debug
```bash
# Variable de entorno para ver logs detallados
export PYTHONPATH=$PYTHONPATH:$(pwd)
export DEBUG=1
python src/local.py
```

#### Verificar conectividad con APIs
```bash
# Test de conexión básico
curl -H "Authorization: Bearer $GROQ_API_KEY" https://api.groq.com/v1/models
```

#### Limpiar caché de pip
```bash
pip cache purge
pip install -r requirements.txt --no-cache-dir
```

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

## 🔧 Configuración Avanzada

### Variables de Entorno Adicionales

```bash
# Configuración de timeouts
REQUEST_TIMEOUT=30
STREAM_TIMEOUT=60

# Configuración de logging
LOG_LEVEL=INFO
LOG_FILE=terminal_ai.log

# Configuración de límites
MAX_RETRIES=3
RETRY_DELAY=1
```

### Configuración por Agente

Puedes personalizar cada agente modificando sus archivos correspondientes:

**Groq** (`src/agents/groq_client.py`):
```python
temperature=0.7
max_tokens=1000
model="mixtral-8x7b-32768"
```

**Cerebras** (`src/agents/cerebras_client.py`):
```python
temperature=0.7
max_tokens=1000
model="llama3.1-70b"
```

**Gemini** (`src/agents/gemini_client.py`):
```python
temperature=0.7
max_output_tokens=1000
model="gemini-pro"
```

### Configuración del Archivo de Estado

El archivo `data.json` puede contener configuración adicional:

```json
{
    "current_agent": 1,
    "rotation_mode": "round_robin",
    "agent_weights": {
        "groq": 0.4,
        "cerebras": 0.3,
        "gemini": 0.3
    },
    "fallback_enabled": true
}
```

## 📊 Rendimiento y Monitoreo

### Métricas Disponibles

El sistema puede registrar las siguientes métricas:
- Tiempo de respuesta por agente
- Número de tokens consumidos
- Tasa de error por proveedor
- Rotación de agentes

### Scripts de Monitoreo

```python
# monitoreo.py
import json
import time
from src.local import get_agent_stats

def monitor_performance():
    while True:
        stats = get_agent_stats()
        print(f"Stats: {json.dumps(stats, indent=2)}")
        time.sleep(60)
```

## 🧪 Testing

### Ejecutar Tests

```bash
# Instalar dependencias de desarrollo
pip install pytest pytest-asyncio

# Ejecutar tests básicos
pytest tests/

# Ejecutar tests con coverage
pytest --cov=src tests/

# Ejecutar tests de integración
pytest tests/integration/
```

### Tests Manuales

```bash
# Test de conectividad con APIs
python -c "
from src.agents.groq_client import GroqAgent
agent = GroqAgent()
print('Groq:', agent.test_connection())
"

# Test de rotación de agentes
python src/test_rotation.py
```

## 🚀 Despliegue

### Como Servicio Sistemático

**systemd (Linux)**:
```ini
# /etc/systemd/system/terminal-ai.service
[Unit]
Description=Terminal AI Assistant
After=network.target

[Service]
Type=simple
User=youruser
WorkingDirectory=/path/to/terminal_ai
Environment=PATH=/path/to/venv/bin
ExecStart=/path/to/venv/bin/python src/local.py
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable terminal-ai
sudo systemctl start terminal-ai
```

### Como API REST

```python
# api_server.py
from fastapi import FastAPI
from src.local import ask_agents

app = FastAPI()

@app.post("/ask")
async def ask_question(question: str):
    response = ""
    for chunk in ask_agents(question):
        response += chunk
    return {"response": response}
```

## 🤝 Contribuciones

### Flujo de Trabajo

1. Fork el repositorio
2. Crear una rama para tu feature
3. Hacer commits con mensajes descriptivos
4. Crear Pull Request

### Guía de Estilo

- Usar Python 3.8+
- Seguir PEP 8
- Agregar tests para nuevas funcionalidades
- Documentar cambios en README.md

### Estructura de Archivos

```
terminal_ai/
├── src/
│   ├── local.py                 # Script principal
│   └── agents/
│       ├── __init__.py
│       ├── groq_client.py       # Agente Groq
│       ├── cerebras_client.py   # Agente Cerebras
│       └── gemini_client.py     # Agente Gemini
├── tests/                       # Tests unitarios y de integración
├── docs/                        # Documentación adicional
├── scripts/                     # Scripts de utilidad
├── data.json                    # Archivo de persistencia del estado
├── requirements.txt             # Dependencias del proyecto
├── .env.example                 # Ejemplo de configuración
├── .gitignore                   # Archivos ignorados por git
└── README.md                    # Este archivo
```

## 📝 Changelog

### v1.0.0 (Enero 2026)
- Versión inicial
- Soporte para 3 agentes de IA
- Rotación automática
- Streaming de respuestas

---

**Última actualización**: Febrero 2026
**Versión**: 1.0.0
**Python**: 3.8+
