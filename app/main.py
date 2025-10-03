from fastapi import FastAPI
from app.routes import sample

app = FastAPI(title="Notes MVP API", version="0.1.0")

# Health/root endpoint
@app.get("/", tags=["health"])
def root():
    return {"status": "ok", "message": "Notes MVP is running"}

# Include the notes router (prefix is defined in the router)
app.include_router(sample.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
