from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite database stored in the project root
SQLALCHEMY_DATABASE_URL = "sqlite:///./notes.db"

# For SQLite we need check_same_thread disabled to share the connection
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


def get_db():
    """Yield a database session per request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def ensure_owner_column(engine):
    """
    Ensure the notes table has an owner column.

    SQLite doesn't add new columns automatically when models change, so we
    alter the table when running against an existing database.
    """
    with engine.begin() as connection:
        columns = {
            row[1] for row in connection.execute(text("PRAGMA table_info(notes);"))
        }
        if "owner" not in columns:
            connection.execute(
                text(
                    "ALTER TABLE notes "
                    "ADD COLUMN owner VARCHAR(100) NOT NULL DEFAULT 'anonymous'"
                )
            )
