> [!IMPORTANT]
> **Grupo 1**
> 
> **Integrantes:** Ouissal, Fernanda Osorio, Pol García y Biel García


# Proyecto de aplicación de notas con FastAPI
En el estado actual, el proyecto desarrollado con FastAPI implementa una API REST funcional para registrar notas. Utiliza SQLite como base de datos y cuenta con una interfaz HTML/CSS sencilla para probar el flujo completo de creación y visualización de notas!!

# Objetivo del proyecto
El objetivo principal del proyecto es construir una aplicación web ligera y modular que permita gestionar notas de manera eficiente mediante una arquitectura basada en API REST. Buscamos servir como una base de aprendizaje y práctica para el desarrollo backend con FastAPI, la integración de bases de datos y el uso de interfaces web minimalistas para probar funcionalidades end-to-end.
A medio plazo, el proyecto pretende evolucionar hacia una aplicación más completa, incorporando autenticación de usuarios, persistencia avanzada, adición de categorías de notas, filtrado de notas, buscador...

---
# Avanze realizado 
Actualmente, el proyecto cuenta con una estructura funcional que cubre todo el flujo básico de una aplicación:
* Creación, lectura, actualización y eliminación de notas.
* Persistencia local en base de datos SQLite.
* Interfaz web minimalista para probar las operaciones principales.
* Validación de datos con Pydantic v2 y manejo de errores controlado.
* Pruebas iniciales automatizadas con pytest para los endpoints principales.
Este punto marca el cierre de la primera fase del desarrollo (MVP funcional), garantizando que la base técnica está lista para futuras ampliaciones.

## Funcionalidades clave
- API REST en `/api/notes`.
- Persistencia con SQLite (archivo `notes.db` en la raíz del proyecto).
- Interfaz web sencilla en `http://127.0.0.1:8080/app` para crear, listar y eliminar notas.
- Esquemas de validación con Pydantic v2.
- Suite básica de pruebas con pytest.

## Próximos pasos
- Autenticación: registro e inicio de sesión de usuarios.
- Organización: categorías, etiquetas y filtros para las notas.
- Búsqueda: buscador rápido por título o contenido.
- Interfaz: diseño más claro e interactivo, con mensajes y sesiones.
- Experiencia: paginación, favoritos y posibles modos visuales.

---
# Como probar nuestra aplicación

## Requisitos
> [!IMPORTANT]
> Asegúrate de tener Python 3.9 o superior instalado antes de continuar.
> Puedes verificarlo con:
> ```powershell
> python --version
> ```

> [!TIP]
> Se recomienda usar un entorno virtual para evitar conflictos con otras dependencias de tu sistema.
> ```powershell
> # Crear y activar un entorno virtual recomendado
> python -m venv .venv
> .\venv\Scripts\Activate.ps1
> ```

## Ejecución rápida

### - Paso 1: Instalar dependencias
```powershell
pip install -r .\app\requirements.txt
```

### - Paso 2: Ejecutar servidor
```powershell
uvicorn app.main:app --reload --host 127.0.0.1 --port 8080
```

> [!IMPORTANT]
> Asegúrate de ejecutar los siguientes comandos desde la raíz del proyecto, donde se encuentra la carpeta app/.

### - Paso 3: Navegar mediante los accesos **(RECOMENDADO EL /APP CON EL FRONTED)**
  - Frontend PMV: <http://127.0.0.1:8080/app>
  - Documentación interactiva: <http://127.0.0.1:8080/docs>
  - Redoc: <http://127.0.0.1:8080/redoc>

--- 

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
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8080/api/notes/ -Body $body -ContentType 'application/json'
```

## Tests

```powershell
pytest -q
```

Las pruebas utilizan `TestClient` para validar los endpoints principales.
