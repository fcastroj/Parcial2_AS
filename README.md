# API de Gestión de Tareas
## Parcial 2 - Arquitectura de Software 
## Felipe Castro Jaimes - Universidad EAFIT

# 🧱 API de Gestión de Tareas — Arquitectura de Software (FastAPI + Docker)

Este proyecto implementa una **API REST** para la gestión de tareas (To-Do API) desarrollada en **Python (FastAPI)** y desplegada con **Docker**.  
El diseño sigue **principios SOLID**, una **arquitectura por capas** inspirada en **Clean Architecture / Hexagonal**, y utiliza patrones de diseño como **Repository** y **Service**.

---

## 🚀 Objetivo

Construir una API REST sencilla de gestión de tareas que:
- Liste tareas (`GET /tasks`)
- Cree tareas (`POST /tasks`)
- Permita verificar el estado del servicio (`GET /health`)
- Sea fácilmente extensible y siga buenas prácticas de diseño.

---

## ⚙️ Tecnologías utilizadas

- **Lenguaje:** Python 3.11  
- **Framework:** FastAPI  
- **Servidor:** Uvicorn  
- **Contenedor:** Docker  
- **Gestión de dependencias:** `requirements.txt`  
- **Persistencia:** En memoria (lista Python)

---

## 🏗️ Arquitectura del proyecto

El proyecto está organizado siguiendo una **arquitectura por capas**, inspirada en **Clean Architecture** y **Hexagonal Architecture**.

```bash
   app/
   ├── domain/
   │ └── task.py # Entidad principal (Task)
   ├── application/
   │ ├── services/
   │ │ └── task_service.py # Lógica de negocio (casos de uso)
   │ └── ports/
   │ └── task_repository.py # Interfaz (abstracción del repositorio)
   ├── adapters/
   │ ├── http/
   │ │ └── fastapi_app.py # Capa de transporte HTTP (FastAPI)
   │ └── persistence/
   │ └── memory_task_repository.py # Implementación en memoria del repositorio
   ├── requirements.txt
   └── Dockerfile
   └── test_app.py #Archivo de pruebas para API
```

---


### Instrucciones de ejecución

1. **Construir imagen Docker**
   ```bash
   docker build -t tareas-api .
   docker run -d -p 8000:8000 tareas-api

2. **Ejecución de pruebas**
   ```bash
   pytest -v

