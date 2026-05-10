from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import models
router=APIRouter(prefix='/portfolio')
@router.get('/current')
def current(db:Session=Depends(get_db)): return {'latest_snapshot': db.query(models.PortfolioSnapshot).order_by(models.PortfolioSnapshot.id.desc()).first() is not None}
@router.get('/history')
def history(db:Session=Depends(get_db)): return {'count': db.query(models.PortfolioSnapshot).count()}
