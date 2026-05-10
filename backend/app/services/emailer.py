from sqlalchemy.orm import Session
from app import models

def send_email(db:Session, subject:str, body:str):
    db.add(models.NotificationLog(subject=subject, body=body)); db.commit()
