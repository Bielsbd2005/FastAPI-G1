# Notes MVP API

> Pequeña API REST construida con FastAPI para gestionar notas.

Este repositorio contiene una aplicación mínima que permite crear, listar, obtener, actualizar y borrar notas en memoria. Está pensada como ejemplo didáctico o punto de partida para un proyecto más completo.

## Características

- API REST con FastAPI
- Almacenamiento en memoria (lista Python) — no persistente
- Esquemas de validación con Pydantic
- Tests básicos con pytest

## Estructura del proyecto

```
app/
  main.py            # Entrypoint de FastAPI
  requirements.txt   # Dependencias del proyecto
  models/
    item.py          # Modelos Pydantic (Note, NoteCreate)
  routes/
    sample.py        # Router con endpoints /api/notes
  tests/
    test_notes.py    # Tests para las rutas de notas
    test_sample.py   # Tests adicionales / ejemplo
```

## Tecnologías

- Python
- FastAPI
- Pydantic
- Uvicorn (servidor ASGI)
- pytest (tests)

## Requisitos

- Python 3.8+ (compatible con versiones recientes)

## Instalación (Windows PowerShell)

1. Crear y activar un entorno virtual (recomendado):

```powershell
# Crear el virtualenv
python -m venv .venv
# Activarlo
.\venv\Scripts\Activate.ps1
```

2. Instalar dependencias:

```powershell
pip install -r .\app\requirements.txt
```

## Ejecutar la aplicación

En desarrollo con autoreload usando uvicorn:

```powershell
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Luego abre en el navegador:

- Documentación interactiva (Swagger): http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc

También hay un endpoint de salud en la raíz:

```http
GET /
Response: { "status": "ok", "message": "Notes MVP is running" }
```

## Endpoints principales (/api/notes)

Base path: `/api/notes`

- POST /api/notes/ — Crear una nota

  - Body JSON: { "title": "Mi título", "content": "Texto de la nota" }
  - Respuesta 201: objeto Note con campos `id` y `created_at`.

- GET /api/notes/ — Listar todas las notas

  - Respuesta 200: lista de objetos Note

- GET /api/notes/{id} — Obtener una nota por id

  - Respuesta 200: objeto Note o 404 si no existe

- PUT /api/notes/{id} — Actualizar una nota (reemplazo)

  - Body JSON: { "title": "Nuevo título", "content": "Nuevo contenido" }
  - Respuesta 200: objeto Note actualizado o 404 si no existe

- DELETE /api/notes/{id} — Borrar una nota
  - Respuesta 204 No Content o 404 si no existe

Ejemplo con PowerShell (crear nota):

```powershell
$body = @{title = 'Prueba'; content = 'Contenido de prueba'} | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/api/notes/ -Body $body -ContentType 'application/json'
```

Ejemplo con curl (alternativa):

```bash
curl -X POST "http://127.0.0.1:8000/api/notes/" -H "Content-Type: application/json" -d '{"title":"Prueba","content":"Contenido"}'
```

## Tests

Ejecutar tests con pytest desde la raíz del proyecto:

```powershell
pytest -q
```

Los tests usando `httpx` simulan peticiones a la app y validan comportamiento básico.
