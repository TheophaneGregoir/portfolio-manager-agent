from dataclasses import dataclass
from app.config import settings

@dataclass
class RiskResult:
    approved: bool
    reason: str = ""

def validate_order(symbol:str, side:str, notional:float, orders_today:int=0, turnover_today:float=0)->RiskResult:
    allowed={s.strip() for s in settings.allowed_symbols.split(',') if s.strip()}
    if symbol not in allowed: return RiskResult(False, 'forbidden symbol')
    if notional>settings.max_order_notional_usd: return RiskResult(False, 'oversized order')
    if orders_today>=settings.max_orders_per_day: return RiskResult(False, 'max orders/day exceeded')
    if turnover_today+notional>settings.max_daily_turnover_usd: return RiskResult(False, 'daily turnover exceeded')
    if side not in {'buy','sell'}: return RiskResult(False,'invalid side')
    return RiskResult(True,'approved')
