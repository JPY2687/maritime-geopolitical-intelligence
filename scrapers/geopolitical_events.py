from scrapers.base import JsonFeedScraper


class GeopoliticalEventsScraper(JsonFeedScraper):
    def __init__(self, feed_url: str) -> None:
        super().__init__(feed_url, "geopolitical")
