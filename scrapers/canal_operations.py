from datetime import datetime, timezone

from intelligence.models import MaritimeEvent
from scrapers.base import BaseScraper


class ExampleCanalOperationsScraper(BaseScraper):
    """Return synthetic data to demonstrate the scraper interface."""

    def scrape(self) -> list[MaritimeEvent]:
        return [
            MaritimeEvent(
                source="synthetic-example",
                category="canal_operation",
                title="Demonstration canal operations event",
                description="Synthetic example only; no real-world incident is reported.",
                location="Suez Canal (example)",
                occurred_at=datetime.now(timezone.utc),
                impact_score=0.0,
            )
        ]
