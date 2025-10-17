# Notes MVP

Pequeño proyecto con FastAPI que ahora ofrece una experiencia mínima pero funcional para registrar notas: API REST, base de datos SQLite y una vista HTML/CSS para probar el flujo end-to-end.

## Funcionalidades clave

- API REST en `/api/notes` con operaciones CRUD completas.
- Persistencia con SQLite (archivo `notes.db` en la raíz del proyecto).
- Interfaz web sencilla en `http://127.0.0.1:8000/app` para crear, listar y eliminar notas.
- Esquemas de validación con Pydantic v2.
- Suite básica de pruebas con pytest.

## Estructura del proyecto

```
app/
  main.py             # Arranque de FastAPI, mounting de estáticos y frontend
  requirements.txt    # Dependencias de la app
  database.py         # Motor SQLAlchemy y sesión
  models/
    item.py           # Modelos Pydantic (Note, NoteCreate)
    note_model.py     # Modelo SQLAlchemy (tabla notes)
  routes/
    sample.py         # Endpoints /api/notes usando la base de datos
  static/
    css/styles.css    # Estilos del PMV
  templates/
    index.html        # Página HTML con JS para consumir la API
  tests/
    test_notes.py     # Pruebas principales de la API
    test_sample.py    # Ejemplos adicionales
```

## Requisitos

- Python 3.9 o superior.

## Instalación rápida (PowerShell)

```powershell
# Crear y activar un entorno virtual recomendado
python -m venv .venv
.\venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r .\app\requirements.txt
```

## Ejecutar el servidor

```powershell
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

- Frontend PMV: <http://127.0.0.1:8000/app>
- Documentación interactiva: <http://127.0.0.1:8000/docs>
- Redoc: <http://127.0.0.1:8000/redoc>

## API `/api/notes`

| Método | Ruta              | Descripción                |
| ------ | ----------------- | -------------------------- |
| POST   | `/api/notes/`     | Crear una nota             |
| GET    | `/api/notes/`     | Listar todas las notas     |
| GET    | `/api/notes/{id}` | Recuperar una nota puntual |
| PUT    | `/api/notes/{id}` | Actualizar título/nota     |
| DELETE | `/api/notes/{id}` | Eliminar una nota          |

Ejemplo rápido con PowerShell:

```powershell
$body = @{title = 'Prueba'; content = 'Contenido'} | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/api/notes/ -Body $body -ContentType 'application/json'
```

## Tests

```powershell
pytest -q
```

Las pruebas utilizan `TestClient` para validar los endpoints principales.
