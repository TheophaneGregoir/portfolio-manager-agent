from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import models
router=APIRouter(prefix='/orders')
@router.get('')
def orders(db:Session=Depends(get_db)): return [{'id':o.id,'status':o.status} for o in db.query(models.ExecutedOrder).all()]
@router.get('/{id}')
def order(id:int, db:Session=Depends(get_db)): o=db.get(models.ExecutedOrder,id); return {'id':o.id,'status':o.status} if o else {}
