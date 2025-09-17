from sqlalchemy.ext.asyncio import async_sessionmaker,create_async_engine
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os
load_dotenv()
DB_URL = os.environ.get("NEON_DB_URL")
if not DB_URL:
    raise ValueError("DB_URL environment variable is not set!")
ENGINE = create_async_engine(DB_URL)
SessionLocal = async_sessionmaker(ENGINE)
BASE = declarative_base()

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
       await db.close()    
