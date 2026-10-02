from collections import Counter

from intelligence.models import MaritimeEvent


def summarize_events(events: list[MaritimeEvent]) -> dict[str, int]:
    """Return a simple count of normalized events by category."""
    return dict(Counter(event.category for event in events))
