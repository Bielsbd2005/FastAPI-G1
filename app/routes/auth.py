from fastapi import APIRouter, HTTPException, Request, status
from pydantic import BaseModel


router = APIRouter(prefix="/api/session", tags=["session"])


class SessionPayload(BaseModel):
    username: str


def get_current_username(request: Request) -> str:
    """Return the username stored in the session or raise 401."""
    username = request.session.get("username")
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No has iniciado sesión",
        )
    return username


@router.get("/", status_code=status.HTTP_200_OK)
def get_session(request: Request):
    """Return the active session username."""
    return {"username": get_current_username(request)}


@router.post("/", status_code=status.HTTP_200_OK)
def start_session(payload: SessionPayload, request: Request):
    """Start a session using a plain username."""
    username = payload.username.strip()
    if not username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El nombre es obligatorio",
        )
    request.session["username"] = username
    return {"username": username}


@router.delete("/", status_code=status.HTTP_200_OK)
def end_session(request: Request):
    """Clear the session."""
    request.session.clear()
    return {"message": "Sesión cerrada"}
