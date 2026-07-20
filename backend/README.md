# Backend

Minimal FastAPI scaffold for the Aletheia gateway.

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Database migrations

```bash
alembic -c alembic.ini upgrade head
```

## Gateway errors

Provider adapter failures return HTTP `502` with a stable response body:

```json
{
  "detail": {
    "error": "provider_error",
    "message": "Provider request failed"
  }
}
```

The public error message is intentionally generic so provider exception details
do not leak credentials, prompts, or upstream response payloads.
