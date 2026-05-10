from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.agent.orchestration import run_once
from app import models
from app.config import settings
router=APIRouter(prefix='/agent')
@router.get('/runs')
def runs(db:Session=Depends(get_db)): return [{'id':r.id,'summary':r.summary} for r in db.query(models.AgentRun).all()]
@router.get('/runs/{id}')
def run(id:int, db:Session=Depends(get_db)): r=db.get(models.AgentRun,id); return {'id':r.id,'summary':r.summary} if r else {}
@router.post('/run-once')
def run_one(db:Session=Depends(get_db)): return run_once(db, settings.dry_run)
