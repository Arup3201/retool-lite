from fastapi import FastAPI

app = FastAPI()

@app.get('/health')
def health():
    return {"name": "retool-lite", "status": "running"}