from pydantic import BaseModel
from typing import Literal

class ProposedOrderSchema(BaseModel):
    symbol: str
    side: Literal['buy','sell']
    notional_usd: float
    confidence: float = 0.5
    rationale: str = ''
    risk_notes: str = ''
