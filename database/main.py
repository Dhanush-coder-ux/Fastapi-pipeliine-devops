from sqlalchemy.ext.asyncio import async_sessionmaker,create_async_engine
from sqlalchemy.ext.declarative import declarative_base
DB_URL = "postgresql+asyncpg://neondb_owner:npg_fEXwsG8uQ5tq@ep-delicate-grass-a138r5uz-pooler.ap-southeast-1.aws.neon.tech/neondb"
ENGINE = create_async_engine(DB_URL)
SessionLocal = async_sessionmaker(ENGINE)
BASE = declarative_base()

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
       await db.close()    
