# Paper Portfolio Manager Agent

**This repository is intentionally limited to Alpaca paper trading.**

## Architecture Diagram

```text
APScheduler -> PortfolioAgent -> Risk Engine -> Alpaca Paper API
      |               |              |                |
      v               v              v                v
   News RSS       Postgres       Rejections       Executions
      \_______________________________________________/
                         Audit + Email Notifications
```

## Startup
1. Copy `.env.example` to `.env` and fill credentials.
2. Run: `docker compose up -d --build`
3. Check health: `curl http://localhost:8000/health`

## Environment Setup
- Python 3.12, Postgres 16, FastAPI, APScheduler, SQLAlchemy 2.x.
- Key safety envs: `ALLOW_LIVE_TRADING=false`, `ALPACA_BASE_URL=https://paper-api.alpaca.markets`.

## Scheduling
- Controlled by `ENABLE_SCHEDULER` and `AGENT_RUN_CRON`.
- Default targets weekday open-adjacent processing.

## Autonomous Flow
1. Scheduler triggers run.
2. RSS news ingestion.
3. Portfolio sync.
4. Agent analysis.
5. Risk checks.
6. Paper order execution (unless `DRY_RUN=true`).
7. Persist run, decisions, orders, rejections.
8. Send email notifications.

## Docker Commands
- Start: `docker compose up -d --build`
- Logs: `docker compose logs -f backend`
- Stop: `docker compose down`

## Troubleshooting
- If backend exits immediately, verify paper-only env checks.
- Confirm Postgres health and `DATABASE_URL`.
- Confirm SMTP endpoint accessibility.

## Security Considerations
- Hard fail on any live trading configuration.
- Deterministic risk engine gate is non-bypassable.
- All actions are persisted for auditing.

## Paper Trading Behavior
- Only long-equity paper orders for allowed symbols.
- No options, no margin, no shorting, no crypto.
- DRY_RUN stores decisions without submitting paper orders.
