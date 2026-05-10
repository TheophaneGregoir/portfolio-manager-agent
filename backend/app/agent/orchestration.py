from sqlalchemy.orm import Session
from app.agent.portfolio_agent import run_portfolio_agent
from app import models
from app.services.execution import execute_orders
from app.services.emailer import send_email

def run_once(db:Session, dry_run:bool=False):
    run=models.AgentRun(summary='started',dry_run=dry_run); db.add(run); db.flush()
    decision=run_portfolio_agent(); db.add(models.AgentDecision(run_id=run.id,payload=str(decision))); db.commit()
    results=execute_orders(db,run.id,decision.get('proposed_orders',[]))
    send_email(db,'[Paper Portfolio Agent] Run completed',str(results))
    return {'run_id':run.id,'decision':decision,'results':results}
