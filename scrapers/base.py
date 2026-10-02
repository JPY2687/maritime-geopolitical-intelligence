import json
from abc import ABC, abstractmethod
from urllib.request import urlopen

from intelligence.models import MaritimeEvent


class BaseScraper(ABC):
    @abstractmethod
    def scrape(self) -> list[MaritimeEvent]:
        """Collect and normalize events from a data source."""


class JsonFeedScraper(BaseScraper):
    def __init__(self, feed_url: str, category: str) -> None:
        self.feed_url = feed_url
        self.category = category

    def scrape(self) -> list[MaritimeEvent]:
        with urlopen(self.feed_url, timeout=10) as response:
            payload = json.load(response)
        if not isinstance(payload, list):
            raise ValueError("JSON feed must contain an array of event objects")
        return [
            MaritimeEvent.model_validate({**event, "category": self.category})
            for event in payload
        ]
