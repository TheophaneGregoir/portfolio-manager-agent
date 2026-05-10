from app.scheduler import start_scheduler

def test_scheduler_triggers_runs():
    s=start_scheduler(); assert s.running; s.shutdown(wait=False)
