from sqlalchemy.orm import Session
from app.services.risk_engine import validate_order
from app.services.alpaca_client import AlpacaPaperClient
from app import models
from app.config import settings

def execute_orders(db:Session, run_id:int, orders:list[dict]):
    client=AlpacaPaperClient(); out=[]
    for o in orders:
        rr=validate_order(o['symbol'],o['side'],o['notional_usd'])
        po=models.ProposedOrder(run_id=run_id,symbol=o['symbol'],side=o['side'],notional_usd=o['notional_usd'],approved=rr.approved)
        db.add(po); db.flush()
        if not rr.approved:
            db.add(models.RiskRejection(run_id=run_id,symbol=o['symbol'],reason=rr.reason)); out.append({'status':'rejected','reason':rr.reason}); continue
        if settings.dry_run:
            out.append({'status':'dry_run'}); continue
        res=client.submit_order(o['symbol'],o['side'],o['notional_usd'])
        db.add(models.ExecutedOrder(proposed_order_id=po.id,external_id=res['id'],status=res['status']))
        out.append({'status':'submitted','id':res['id']})
    db.commit(); return out
