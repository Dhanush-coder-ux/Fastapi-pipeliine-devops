from sqlalchemy.ext.asyncio import async_sessionmaker,create_async_engine
from sqlalchemy.ext.declarative import declarative_base
import os
DB_URL = os.getenv("DB_URL","postgresql+asyncpg://postgres:password@localhost/fastapi_db")
ENGINE = create_async_engine(DB_URL)
SessionLocal = async_sessionmaker(ENGINE)
BASE = declarative_base()

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
       await db.close()    
