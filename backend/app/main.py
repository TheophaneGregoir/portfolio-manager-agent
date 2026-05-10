from fastapi import FastAPI
from app.config import validate_paper_only, settings
from app.db import Base, engine
from app.logging_config import setup_logging
from app.api.health import router as health_router
from app.api.portfolio import router as portfolio_router
from app.api.orders import router as orders_router
from app.api.agent import router as agent_router
from app.api.news import router as news_router
from app.scheduler import start_scheduler

setup_logging()
validate_paper_only()
Base.metadata.create_all(bind=engine)
app=FastAPI(title='Paper Portfolio Agent')
app.include_router(health_router)
app.include_router(portfolio_router)
app.include_router(orders_router)
app.include_router(agent_router)
app.include_router(news_router)

@app.on_event('startup')
def startup():
    if settings.enable_scheduler:
        start_scheduler()
