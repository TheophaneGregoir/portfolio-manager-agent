FROM python:3.12-slim
RUN pip install fastapi uvicorn
WORKDIR /app
RUN printf '%s
' "from fastapi import FastAPI\napp=FastAPI()\n@app.get('/health')\ndef h(): return {'status':'ok'}" > main.py
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8081"]
