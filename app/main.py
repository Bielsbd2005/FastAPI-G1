import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from app.database import Base, ensure_owner_column, engine
from app.models import note_model  # noqa: F401 - ensure models are registered
from app.routes import auth, sample

app = FastAPI(title="Notes MVP API", version="0.1.0")

# Ensure database tables exist on startup
Base.metadata.create_all(bind=engine)
ensure_owner_column(engine)

# Serve static assets (CSS, JS) from the /static directory when available
static_dir = Path(__file__).parent / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Path to the HTML MVP page
html_entrypoint = Path(__file__).parent / "templates" / "index.html"

SESSION_SECRET = os.getenv("SESSION_SECRET", "change-me")
app.add_middleware(
    SessionMiddleware,
    secret_key=SESSION_SECRET,
    session_cookie="notes_session",
)

# Health/root endpoint
@app.get("/", tags=["health"])
def root():
    return {"status": "ok", "message": "Notes MVP is running"}


@app.get("/app", include_in_schema=False)
def get_app():
    if not html_entrypoint.exists():
        return {"detail": "Frontend not found"}
    return FileResponse(html_entrypoint)


# Include the notes router (prefix is defined in the router)
app.include_router(auth.router)
app.include_router(sample.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)
