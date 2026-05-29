# Copilot Instructions

## Commands
- Backend (from `backend/`):
  - Install: `pip install -r requirements.txt`
  - Run API: `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`
  - Tests: `python -m pytest`
  - Single test: `python -m pytest tests/test_smoke.py`
- Observability dashboard (from `observability-dashboard/`):
  - Dev: `npm run dev`

## Architecture
- Aletheia is an LLM gateway; this repo currently includes a minimal FastAPI backend and a placeholder dashboard.
- The backend lives in `backend/app`; `app.main:app` defines the FastAPI app and exposes `/health`.
- `docker-compose.yml` provisions a Postgres service and loads values from `.env` for local development.
- The observability dashboard is a separate Node project in `observability-dashboard/` with a scaffold-only `src/`.

## Conventions
- Backend code stays in `backend/app` and tests live in `backend/tests` with pytest-style naming.
- Environment configuration follows `.env.example` keys (APP_*, POSTGRES_*, DATABASE_URL).
- Commit messages must start with one of: `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`, `ci:` followed by a short imperative description.
- Make small, incremental changes. Break down large features into multiple smaller changes. Avoid making sweeping changes across many files in a single commit.
- Provide a detailed summary of every change post implementation, including the motivation, what was changed, and any relevant context or trade-offs. This helps reviewers understand the rationale behind your changes and provides a clear record for future reference.
