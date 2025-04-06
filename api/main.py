from fastapi import FastAPI
from api.routers.auth import auth
from api.models import user
from api.db import engine
from api.models.users import Base

app = FastAPI()

@app.get("/v1/health")
def health():
    return {"status": "OK"}

@app.get("/v1/metrics")
def metrics():
    return {
        "version": "1.0.0",
        "uptime": "15m",
        "cpu_usage": 75.2,
        "memory_usage": 80.5,
        "disk_usage": 95.3
    }
    # Add more metrics as needed
    
@app.get("/v1/hand-scan")
def hand_scan():
    pass

app.include_router(auth.router)
@app.on_event("startup") 
async def on_startup(): 
    async with engine.begin() as conn: 
        await conn.run_sync(Base.metadata.create_all)
