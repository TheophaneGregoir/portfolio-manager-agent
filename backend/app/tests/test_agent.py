import pytest
from app.config import settings, validate_paper_only

def test_refuses_live_endpoint(monkeypatch):
    monkeypatch.setattr(settings,'alpaca_base_url','https://api.alpaca.markets')
    with pytest.raises(RuntimeError): validate_paper_only()

def test_refuses_allow_live_trading(monkeypatch):
    monkeypatch.setattr(settings,'allow_live_trading',True)
    with pytest.raises(RuntimeError): validate_paper_only()
