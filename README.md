# Maritime Supply Chain Intelligence Stack

A starter stack for collecting maritime and geopolitical signals, exposing normalized events through a REST API, and displaying them in a lightweight dashboard. Included event data is clearly marked as synthetic; configure real JSON feeds before using this project for operational intelligence.

## Prerequisites

- Python 3.12 or newer
- Docker and Docker Compose (for the containerized stack)

## Quick start

### Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -m database.init_db
uvicorn api.main:app --reload
```

The API is available at <http://localhost:8000>, interactive docs at
<http://localhost:8000/docs>, and the synthetic example events at
<http://localhost:8000/api/v1/events>. The local default database is SQLite.

### Run with Docker Compose

```bash
cp .env.example .env
docker compose up --build
```

Open <http://localhost:8080> for the dashboard and <http://localhost:8000/docs>
for the API documentation. Compose starts PostgreSQL, Redis, the API, and an
Nginx-served dashboard. Set `POSTGRES_PASSWORD` in `.env` to a strong local
password before exposing the Compose services beyond your machine.

## Architecture

```text
JSON feeds -> scrapers -> Pydantic event schema -> intelligence -> REST API
                                            |                    |
                                      PostgreSQL               Dashboard
```

- `scrapers/`: reusable JSON-feed base and modules for geopolitical events,
  maritime incidents, and canal operations.
- `intelligence/`: normalized event schema and analysis entry point.
- `api/`: FastAPI health and events endpoints.
- `database/`: SQLAlchemy models, engine/session configuration, and schema
  initialization command.
- `dashboard/`: static event dashboard served by Nginx, proxying API requests.
- `config/`: environment-based application settings.
- `tests/`: API and scraper unit tests.
- `docs/`: development and data-source notes.

The starter API serves a synthetic canal event so it works without external
feeds or database data. JSON-feed scrapers accept a feed URL and expect a JSON
array of objects matching the event schema. The database schema is initialized
by `python -m database.init_db`; persistent ingestion and scheduling are left
as extension points.

## Configuration

Copy `.env.example` to `.env` and set values as needed:

| Variable | Purpose | Default |
| --- | --- | --- |
| `APP_NAME` | API title | `Maritime Supply Chain Intelligence` |
| `DATABASE_URL` | SQLAlchemy connection URL | local SQLite |
| `REDIS_URL` | Redis connection URL | local Redis |
| `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD` | Compose PostgreSQL credentials | local development values |

Do not commit `.env` or production credentials.

## Tests

```bash
python -m unittest discover -s tests -v
```

GitHub Actions runs this test command on pushes and pull requests.

## Contributing

Create focused tests for new scrapers, event processing, and API behavior.
Keep source-specific parsing isolated in scraper modules and convert results
to the shared `MaritimeEvent` schema. Clearly identify sample or unverified
data, and document any new configuration variables in `.env.example`.
