from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.services.news_ingestion import ingest_news
router=APIRouter()
@router.post('/news/ingest')
def ingest(db:Session=Depends(get_db)): return {'ingested': ingest_news(db)}
@router.post('/sync/portfolio')
def sync(): return {'synced': True}
