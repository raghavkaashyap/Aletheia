from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(title="Aletheia Gateway")


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "aletheia-backend",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
