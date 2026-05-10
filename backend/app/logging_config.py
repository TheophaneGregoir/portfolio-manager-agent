import logging, json, sys
class JsonFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({"level":record.levelname,"msg":record.getMessage(),"name":record.name})
def setup_logging():
    h=logging.StreamHandler(sys.stdout); h.setFormatter(JsonFormatter()); r=logging.getLogger(); r.handlers=[h]; r.setLevel(logging.INFO)
