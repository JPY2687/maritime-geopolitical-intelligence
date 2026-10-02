from fastapi import FastAPI

from config.settings import get_settings
from intelligence.models import MaritimeEvent
from scrapers.canal_operations import ExampleCanalOperationsScraper

app = FastAPI(title=get_settings().app_name)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/v1/events", response_model=list[MaritimeEvent])
def list_events() -> list[MaritimeEvent]:
    return ExampleCanalOperationsScraper().scrape()
