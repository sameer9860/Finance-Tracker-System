from pydantic import BaseModel
from typing import List

class AnalyticsResponse(BaseModel):
    labels: List[str]
    values: List[float]
