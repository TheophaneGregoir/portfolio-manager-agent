class AlpacaPaperClient:
    def submit_order(self, symbol:str, side:str, notional:float)->dict:
        return {"id": f"paper-{symbol}-{side}", "status":"submitted"}
