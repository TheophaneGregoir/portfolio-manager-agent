from app.agent.guardrails import enforce_structure

def run_portfolio_agent()->dict:
    result={"summary":"Deterministic local run","portfolio_analysis":"Paper portfolio checked","market_analysis":"Recent RSS reviewed","proposed_orders":[],"no_trade_reason":"No high conviction signal"}
    return enforce_structure(result)
