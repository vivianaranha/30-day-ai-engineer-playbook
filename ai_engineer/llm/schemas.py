from pydantic import BaseModel, Field
class TicketAnalysis(BaseModel):
    category: str
    priority: str
    summary: str
    confidence: float = Field(ge=0, le=1)
