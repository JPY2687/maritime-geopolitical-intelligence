# Data sources

Scraper modules normalize JSON arrays into `MaritimeEvent` records. Feed
objects must include `source`, `title`, and `description`; `occurred_at`,
`location`, and `impact_score` are optional. The scraper supplies the event
category for its source module. Feed URLs are passed to scraper constructors,
not stored in the repository.

The built-in canal scraper is synthetic and intended only to exercise the
pipeline shape. Add a source adapter, terms-of-use review, and data validation
before collecting or presenting real-world operational data.
