import unittest

from scrapers.canal_operations import ExampleCanalOperationsScraper
from intelligence.analysis import summarize_events


class ScraperTests(unittest.TestCase):
    def test_example_scraper_emits_normalized_synthetic_event(self) -> None:
        events = ExampleCanalOperationsScraper().scrape()

        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].category, "canal_operation")
        self.assertEqual(summarize_events(events), {"canal_operation": 1})
