from datetime import datetime, timezone
from typing import Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field


class MaritimeEvent(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    source: str
    category: Literal["geopolitical", "maritime_incident", "canal_operation"]
    title: str
    description: str
    location: str | None = None
    occurred_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    impact_score: float = Field(default=0.0, ge=0.0, le=1.0)

    model_config = ConfigDict(from_attributes=True)
