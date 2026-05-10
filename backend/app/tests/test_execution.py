from app.services.execution import execute_orders
from app.db import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import app.models as models

def test_auto_submits_valid_paper_orders(monkeypatch):
    engine=create_engine('sqlite:///:memory:'); Base.metadata.create_all(engine); S=sessionmaker(bind=engine); db=S(); db.add(models.AgentRun(summary='x')); db.commit()
    out=execute_orders(db,1,[{'symbol':'VT','side':'buy','notional_usd':1}]); assert out[0]['status'] in {'submitted','dry_run'}

def test_stores_rejected_orders():
    engine=create_engine('sqlite:///:memory:'); Base.metadata.create_all(engine); S=sessionmaker(bind=engine); db=S(); db.add(models.AgentRun(summary='x')); db.commit()
    out=execute_orders(db,1,[{'symbol':'BAD','side':'buy','notional_usd':1}]); assert out[0]['status']=='rejected'
