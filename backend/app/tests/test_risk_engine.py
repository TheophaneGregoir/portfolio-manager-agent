from app.services.risk_engine import validate_order

def test_reject_forbidden_symbols(): assert not validate_order('AAPL','buy',10).approved

def test_reject_oversized_orders(): assert not validate_order('VT','buy',10_000).approved
