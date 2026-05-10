import feedparser, re
from datetime import datetime
from sqlalchemy.orm import Session
from app import models
from app.config import settings

def ingest_news(db:Session)->int:
    c=0
    for feed in [f.strip() for f in settings.news_rss_feeds.split(',') if f.strip()]:
        parsed=feedparser.parse(feed)
        for e in parsed.entries[:20]:
            url=getattr(e,'link','')
            if not url or db.query(models.NewsItem).filter_by(url=url).first(): continue
            text=(getattr(e,'title','')+' '+getattr(e,'summary',''))
            tickers=','.join(sorted(set(re.findall(r'\b[A-Z]{1,5}\b', text))))
            db.add(models.NewsItem(url=url,title=getattr(e,'title',''),source=feed,summary=getattr(e,'summary',''),published_at=datetime.utcnow(),tickers=tickers)); c+=1
    db.commit(); return c
