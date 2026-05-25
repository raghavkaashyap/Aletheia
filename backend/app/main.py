from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import SQLAlchemyError

from app.db import check_connection, get_engine

app = FastAPI(title="Aletheia Gateway")


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "aletheia-backend",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/health/db")
def health_db() -> dict[str, str]:
    engine = get_engine()
    try:
        check_connection(engine)
    except SQLAlchemyError as exc:
        raise HTTPException(
            status_code=503,
            detail="Database unavailable",
        ) from exc

    return {
        "status": "ok",
        "service": "aletheia-backend",
        "database": "postgres",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
