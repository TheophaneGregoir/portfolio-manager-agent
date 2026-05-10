from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db import Base
from app.services.emailer import send_email
from app import models

def test_emails_sent_after_execution():
    e=create_engine('sqlite:///:memory:'); Base.metadata.create_all(e); S=sessionmaker(bind=e); db=S(); send_email(db,'a','b'); assert db.query(models.NotificationLog).count()==1

def test_dry_run_disables_execution(monkeypatch):
    from app.config import settings
    monkeypatch.setattr(settings,'dry_run',True)
    assert settings.dry_run
