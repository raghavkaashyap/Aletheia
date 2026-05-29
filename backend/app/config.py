from __future__ import annotations

import os
from functools import lru_cache


def _build_database_url() -> str:
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        return database_url

    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT", "5432")
    database = os.getenv("POSTGRES_DB")

    missing = [
        name
        for name, value in {
            "POSTGRES_USER": user,
            "POSTGRES_PASSWORD": password,
            "POSTGRES_HOST": host,
            "POSTGRES_DB": database,
        }.items()
        if not value
    ]
    if missing:
        raise RuntimeError(
            "Missing required database settings: " + ", ".join(missing)
        )

    return f"postgresql+psycopg://{user}:{password}@{host}:{port}/{database}"


@lru_cache(maxsize=1)
def get_database_url() -> str:
    return _build_database_url()
