from apscheduler.schedulers.background import BackgroundScheduler
from app.db import SessionLocal
from app.agent.orchestration import run_once

def start_scheduler():
    s=BackgroundScheduler(timezone='UTC')
    s.add_job(lambda: run_once(SessionLocal()), 'interval', minutes=60, id='agent_run')
    s.start(); return s
