from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str = ""
    openai_model: str = "gpt-5"
    alpaca_api_key: str = ""
    alpaca_secret_key: str = ""
    alpaca_base_url: str = "https://paper-api.alpaca.markets"
    allow_live_trading: bool = False
    database_url: str = "sqlite:///./local.db"
    enable_scheduler: bool = True
    agent_run_cron: str = "35 9 * * 1-5"
    dry_run: bool = False
    max_order_notional_usd: float = 100
    max_daily_turnover_usd: float = 300
    max_orders_per_day: int = 5
    allowed_symbols: str = "VT,VTI,VEA,VWO,BND"
    news_rss_feeds: str = ""
    smtp_host: str = "localhost"
    smtp_port: int = 25
    smtp_user: str = ""
    smtp_password: str = ""
    email_from: str = ""
    email_to: str = ""

    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()

def validate_paper_only() -> None:
    if settings.allow_live_trading:
        raise RuntimeError("ALLOW_LIVE_TRADING=true is forbidden")
    if "paper-api.alpaca.markets" not in settings.alpaca_base_url:
        raise RuntimeError("Only Alpaca paper endpoint is allowed")
